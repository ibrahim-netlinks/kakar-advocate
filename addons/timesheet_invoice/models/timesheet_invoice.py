# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    emp_hourly_cost = fields.Float('Hourly Cost')


class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'
    _description = 'Analytic Line'
    _order = 'date desc'
    
    @api.model
    def create(self, vals):
        if vals.get('project_id'):
            project = self.env['project.project'].browse(vals.get('project_id'))
            vals['account_id'] = project.analytic_account_id.id
            print "project.analytic_account_id.id::::::::::::::::::", project.analytic_account_id.id
        return super(AccountAnalyticLine, self).create(vals)

    @api.multi
    def write(self, vals):
        if vals.get('project_id'):
            project = self.env['project.project'].browse(vals.get('project_id'))
            vals['amount'] = project.analytic_account_id.id
            print "project.analytic_account_id.id::::::::::::::::::", project.analytic_account_id.id
        return super(AccountAnalyticLine, self).write(vals)
    
