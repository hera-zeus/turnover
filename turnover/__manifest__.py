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
    'version': '0.1',
    'category': 'Warehouse',
    'summary': 'Turnover Report XLS',
    'license':'AGPL-3',
    'description': """
    Back Dated Stock Take Report allows to print stock position corresponding to a specific date in the past.
""",
    'author' : 'Merveille ZEBAZE',
    'website' : 'http://merveillezebaze.pythonanywhere.com/',
    'depends': ['stock'],
    'data': [
        'wizard/print_turnover_report_view.xml',
        'wizard/print_turnover_pdf.xml',
        'wizard/print_turnover_report_pdf.xml',
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2:
