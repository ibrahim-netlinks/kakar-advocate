# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, SUPERUSER_ID, _


class CaseCategory(models.Model):
    _name = "case.category"
    _description = "Master Table For Case Categories"

    name = fields.Char('name', required=True)
    sequence = fields.Integer('Sequence')
    active = fields.Boolean('Active', default=True)
