# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2021 Merveille ZEBAZE
#    (<http://merveillezebaze.pythonanywhere.com>).
#
#
##############################################################################
{
    'name': 'Turnover Report ',
    "version": "11.0.1.0.0",
    'category': 'Warehouse',
    "summary": "Allows you to have the turnover of your company in excel and pdf file",
    'license':'AGPL-3',
    'description': """
    this module allows you to have the turnover of your company in excel and pdf file
""",
    'author' : 'Merveille ZEBAZE',
    'website' : 'http://merveillezebaze.pythonanywhere.com',
    'depends': ['stock'],
    "maintainers": ["Merveille ZEBAZE"],
    "license": "AGPL-3",
    'data': [
        'wizard/print_turnover_report_view.xml',
        'wizard/print_turnover_pdf.xml',
        'wizard/print_turnover_report_pdf.xml',
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2:
