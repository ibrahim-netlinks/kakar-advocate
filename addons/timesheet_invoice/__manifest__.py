# -*- coding: utf-8 -*-
# NETLINKS Copyright.

{
    'name': 'Timesheet Invoices',
    'version': '0.1',
    'website': 'https://www.odoo.com/page/project-management',
    'category': 'Project & Invoices',
    'sequence': 10,
    'summary': 'Payment according to timesheet in Project Tasks',
    'depends': [
        'base',
        'project',
    ],
    'description': """
Payment according to timesheet in Project Tasks
=====================================================
    """,
    'data': [
        'wizard/create_invoice_wizard_view.xml',
        'views/timesheet_invoice_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
