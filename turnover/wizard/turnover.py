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
from odoo import api, fields, models, _

from odoo.tools.misc import xlwt
import io
import base64
from math import ceil, floor
import itertools
from operator import itemgetter
import operator

class TurnoverReport(models.TransientModel):
    _name = "turnover.report"
    _description = "Stock Inventory Report"
    
    #inventory_date = fields.Datetime('Inventaire à la date', default=lambda self: fields.Datetime.now())
    stock_report_file = fields.Binary('Rapport d\'inventaire')
    file_name = fields.Char('File Name')
    inventory_printed = fields.Boolean('Payment Report Printed')

    @api.multi
    def get_lines(self):

        ctx = dict(self.env.context) or {}
        #ctx.update({'to_date': wizard.inventory_date})
        product_objs = self.env['product.product'].search([], order='name')
        lines=[]
        for product in product_objs:
            #for line in payslip.lines:
            dic={
                   
                    'id':product.id or '',
                    'qty':product.qty_available or '',
                    'rfc':product.default_code or '',
                }
            lines.append(dic)
        n_lines=sorted(lines,key=itemgetter('id'))
        groups = itertools.groupby(n_lines, key=operator.itemgetter('id'))
        lines = [{'id':k,'values':[x for x in v]} for k, v in groups]
        return lines
    
    @api.multi
    def generate_report(self):
        #payslip_ids = self.get_payslip()
        if (not self.env.user.company_id.logo):
            raise UserError(_("You have to set a logo or a layout for your company."))
        elif (not self.env.user.company_id.external_report_layout):
            raise UserError(_("You have to set your reports's header and footer layout."))
       # data = {'date_start': self.inventory_date}
        return self.env.ref('turnover.print_turnover_pdf').report_action(self, data=None)



    @api.multi
    def action_print_turnover_report(self):
        ctx = dict(self.env.context) or {}
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('Inventaire')
        column_heading_style = xlwt.easyxf('font:height 200;font:bold True;')
        
        row = 2
        for wizard in self:
            report_head = 'Rapport du chiffre d\'affaire '
            #if wizard.inventory_date:
             #   report_head += ' (' + wizard.inventory_date + ')'
            worksheet.write_merge(0, 0, 0, 2, report_head, xlwt.easyxf('font:height 300; align: vertical center; align: horiz center;pattern: pattern solid, fore_color black; font: color white; font:bold True;' "borders: top thin,bottom thin"))
            worksheet.write(1, 0, _('Reference Interne'), column_heading_style) 
            worksheet.write(1, 1, _('Produit'), column_heading_style) 
            worksheet.write(1, 2, _('Quantité disponible'), column_heading_style)
            worksheet.write(1, 3, _('Prix de vente'), column_heading_style)
            worksheet.write(1, 4, _('Valeur'), column_heading_style)

            worksheet.col(0).width = 5000
            worksheet.col(1).width = 10000
            worksheet.col(2).width = 5000
            worksheet.row(0).height = 500
            
            #ctx.update({'to_date': wizard.inventory_date})
            product_objs = self.env['product.product'].search([], order='name')
            for product in product_objs:
                #if product.qty_available > 0:
                if product.default_code:
                    worksheet.write(row, 0, product.default_code)
                if product.attribute_value_ids:
                    worksheet.write(row, 1, str(product.name)+"("+str(product.attribute_value_ids.mapped('name'))+")")
                    worksheet.write(row, 3, product.lst_price)
                    worksheet.write(row, 4, product.lst_price*product.qty_available)

                else:
                    worksheet.write(row, 1, product.name)
                    worksheet.write(row, 3, product.list_price)
                    worksheet.write(row, 4, product.list_price*product.qty_available)
                worksheet.write(row, 2, product.qty_available)
                row += 1
            
            fp = io.BytesIO()
            workbook.save(fp)
            excel_file = base64.encodestring(fp.getvalue())
            wizard.stock_report_file = excel_file
            wizard.file_name = 'Rapport d\'inventaire.xls'
            wizard.inventory_printed = True
            fp.close()
            return {
                    'view_mode': 'form',
                    'res_id': wizard.id,
                    'res_model': 'turnover.report',
                    'view_type': 'form',
                    'type': 'ir.actions.act_window',
                    'context': self.env.context,
                    'target': 'new',
            }
    


# vim:expandtab:smartindent:tabstop=2:softtabstop=2:shiftwidth=2:
