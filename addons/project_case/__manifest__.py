# -*- coding: utf-8 -*-
# NETLINKS Copyright.

{
    'name': 'Extended Project',
    'version': '0.1',
    'website': 'https://www.odoo.com/page/project-management',
    'category': 'Project',
    'sequence': 10,
    'summary': 'Modification in Main Project Module',
    'depends': [
        'base',
        'hr',
        'project',
        'timesheet_invoice'
    ],
    'description': """
Modification in Main Project Module
=====================================================
    """,
    'data': [
        'views/project_cases_view.xml',
        'views/case_category_view.xml',
        'views/project_case_menus_view.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
