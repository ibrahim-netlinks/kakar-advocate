# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from openerp.exceptions import ValidationError,UserError


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    emp_hourly_cost = fields.Float('Hourly Cost')


class ProjectCases(models.Model):
    _description = "Timesheet Invoice Inherit Project"
    _inherit = 'project.project'

    fee_type = fields.Selection([('hourly', 'Hourly Fee'), ('flat', 'Flat Fee')], string='Fee Type')
    flat_cost = fields.Float('Flat Cost')


class ProjectMemberCosts(models.Model):
    _name = 'project.member.costs'
    _description = 'Model To Define/Override Employees Case/Project Cost On Hourly Basis'

    user_id = fields.Many2one('res.users', string='Member')
    project_id = fields.Many2one('project.project', string='Member')
    emp_hourly_cost = fields.Float('Hourly Cost')


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    _description = 'Analytic Line'
    _order = 'date desc'

    @api.model
    def create(self, vals):
        emp_obj = self.env['hr.employee']
        emp_overriden_cost_obj = self.env['project.member.costs']
        emp_cost = 0.0
        if vals.get('project_id'):
            emp_id = emp_obj.search([('user_id', '=', vals.get('user_id'))], limit=1)
            member_id = emp_overriden_cost_obj.search([('user_id', '=', vals.get('user_id'))], limit=1)

            if member_id:
                emp_cost = member_id.emp_hourly_cost
            else:
                emp_cost = emp_id.emp_hourly_cost
            if not emp_cost or (not emp_id.emp_hourly_cost and not member_id.emp_hourly_cost):
                raise ValidationError('Please configure Employee Hourly Cost Either In Employee Profile Or In Cases (Projects)')
            project = self.env['project.project'].browse(vals.get('project_id'))
            vals['account_id'] = project.analytic_account_id.id
            vals['amount'] = emp_cost
        return super(AccountAnalyticLine, self).create(vals)

    @api.multi
    def write(self, vals):
        emp_obj = self.env['hr.employee']
        emp_overriden_cost_obj = self.env['project.member.costs']
        emp_cost = 0.0
        if vals.get('project_id'):
            emp_id = emp_obj.search([('user_id','=',vals.get('user_id'))],limit=1)
            member_id = emp_overriden_cost_obj.search([('user_id','=',vals.get('user_id'))], limit=1)
            if member_id:
                emp_cost = member_id.emp_hourly_cost
            else:
                emp_cost = emp_id.emp_hourly_cost
            if not emp_cost or (not emp_id.emp_hourly_cost and not member_id.emp_hourly_cost):
                raise ValidationError('Please configure Employee Hourly Cost Either In Employee Profile Or In Cases (Projects)')
            project = self.env['project.project'].browse(vals.get('project_id'))
            vals['account_id'] = project.analytic_account_id.id
            vals['amount'] = emp_cost
        return super(AccountAnalyticLine, self).write(vals)
