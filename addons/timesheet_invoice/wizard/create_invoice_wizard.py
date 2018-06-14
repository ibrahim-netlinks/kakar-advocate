from openerp import models, fields, api, _
from datetime import date, datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from openerp.exceptions import ValidationError, UserError


class CreateTimesheetInvoice(models.TransientModel):
    _name = "create.timesheet.invoice"

    timesheet_line_ids = fields.Many2many('account.analytic.line')

    def calc_timesheet_invoice(self):
        context = dict(self.env.context)
        project_obj = self.env['project.project']
        timesheet_obj = self.env['account.analytic.line']
        invoice_account_obj = self.env['account.invoice']
        project_id = project_obj.browse(context.get('project_active_id'))
        if project_id.state not in ['approved', 'closed']:
            raise ValidationError('You are only alowed to create '
                'invoice in Approved Or Closed Stages'
            )
        flat_timesheet_id = timesheet_obj.search([('project_id', '=', project_id.id)])
        if not flat_timesheet_id:
            raise ValidationError("At least add one timesheet for this project")
        timesheet_ids = context.get('fee_type') and flat_timesheet_id[0] or self.timesheet_line_ids
        partner_id = context.get('fee_type') and flat_timesheet_id[0].partner_id or timesheet_ids[0].partner_id
        user_id = context.get('fee_type') and flat_timesheet_id[0].user_id or timesheet_ids[0].user_id
        invoice_line_vals = []

        if not timesheet_ids:
            raise ValidationError("No timesheet found for this project")

        if context.get('fee_type'):
            timesheet_ids = timesheet_ids[0]

        for timesheet_line in timesheet_ids:
            invoice_line_vals.append((0, 0, {
                'create_date': datetime.now().strftime(DF),
                'create_uid': self._uid,
                'write_date': datetime.now().strftime(DF),
                'write_uid': self._uid,
                'price_unit': context.get('fee_type') and project_id.flat_cost or timesheet_line.amount,
                'currency_id': timesheet_line.currency_id.id,
                'partner_id': timesheet_line.partner_id.id,
                'company_id': timesheet_line.company_id.id,
                'account_id': timesheet_line.account_id.id,
                'name': context.get('fee_type') and 'Fee: ' + project_id.name or timesheet_line.name,
                'quantity': context.get('fee_type') and 1 or timesheet_line.unit_amount
            }))
        return {
            'name': _('Account Invoice'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'account.invoice',
            'view_id': self.env.ref('account.invoice_form').id,
            'type': 'ir.actions.act_window',
            'context': {
                    'default_active': True,
                'default_partner_id': partner_id.id,
                'default_date_invoice': date.today().strftime(DF),
                'default_user_id': user_id.id,
                'default_invoice_line_ids': invoice_line_vals,
            }
        }
