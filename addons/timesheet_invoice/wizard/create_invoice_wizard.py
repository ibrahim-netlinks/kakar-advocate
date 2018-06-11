from openerp import models, fields, api, _
from datetime import date, datetime, timedelta
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DF
from openerp.exceptions import ValidationError, UserError


class CreateTimesheetInvoice(models.TransientModel):
    _name = "create.timesheet.invoice"

    timesheet_line_ids = fields.Many2many('account.analytic.line')

    def calc_timesheet_invoice(self):
        invoice_line_obj = self.env['account.invoice.line']
        invoice_account_obj = self.env['account.invoice']
        timesheet_ids = self.timesheet_line_ids
        partner_id = timesheet_ids[0].partner_id
        user_id = timesheet_ids[0].user_id
        invoice_line_vals = []

        for timesheet_line in timesheet_ids:
            invoice_line_vals.append((0, 0, {
                'create_date': datetime.now().strftime(DF),
                'create_uid': self._uid,
                'write_date': datetime.now().strftime(DF),
                'write_uid': self._uid,
                'price_unit': 123,
                'currency_id': timesheet_line.currency_id.id,
                'partner_id': timesheet_line.partner_id.id,
                'company_id': timesheet_line.company_id.id,
                'account_id': timesheet_line.account_id.id,
                'name': timesheet_line.name,
                'quantity': timesheet_line.unit_amount
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
