# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2021 Normalis Consulting (Merveille ZEBAZE) 
#    (<http://normalis.consulting>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
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
    'author' : 'Normalis Consulting (Merveille ZEBAZE) ',
    'website' : 'http://normalis.consulting',
    'depends': ['stock'],
    #'images': ['static/description/banner.jpg'],
    'data': [
        'wizard/print_turnover_report_view.xml',
        'wizard/print_turnover_pdf.xml',
        'wizard/print_turnover_report_pdf.xml',
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2:
