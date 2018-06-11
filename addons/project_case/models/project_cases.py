# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID, _


class ProjectCases(models.Model):
    _description = "Cases/Project"
    _inherit = 'project.project'

    case_ref_no = fields.Char('Case Reference')
    use_tasks = fields.Boolean(string='Use Tasks', default=True, help="Check this box to manage internal activities through this project")
    case_budget = fields.Float('Budget')
    start_date = fields.Date('Start Date')
    description = fields.Html('Description')

    # Relational Fields
    case_category_id = fields.Many2one('case.category', string='Case Category', required=True)
    user_id = fields.Many2one('res.users', string='Case Manager', default=lambda self: self.env.user)

    @api.model
    def create(self, vals):
        result = super(ProjectCases, self).create(vals)
        result.update({'case_ref_no': self.env['ir.sequence'].next_by_code('case_ref_no')})
        return result
