# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class SaleOrder(models.Model):
	_inherit = 'sale.order'

	custom_purchase_count = fields.Integer('Purchase',compute='_compute_custom_purchase_count')	
	custom_manufacture_count = fields.Integer('Manufacture',compute='_compute_custom_manufacture_count')	

	def _compute_custom_purchase_count(self):
		for so in self:
			po = self.env['purchase.order'].search_count([('sale_ord_id','=', so.id)])
			so.custom_purchase_count = po

	@api.multi
	def action_view_custom_purchase(self):
		action = self.env.ref('purchase.purchase_order_tree').read()[0]
		context = dict(self.env.context or {})
		purchases = self.env['purchase.order'].search([('sale_ord_id','=', self.id)])
		return {
			'name': _('Purchase Order'),
			'view_mode': 'tree,form',
			'res_model': 'purchase.order',
			'domain': [('id', 'in', purchases.ids)],
			'type': 'ir.actions.act_window',
			}


	def _compute_custom_manufacture_count(self):
		for so in self:
			po = self.env['mrp.production'].search_count([('origin','like', so.id)])
			so.custom_manufacture_count = po

	@api.multi
	def action_view_custom_manufacture(self):
		action = self.env.ref('mrp.mrp_production_tree_view').read()[0]
		context = dict(self.env.context or {})
		purchases = self.env['mrp.production'].search([('origin','like', self.id)])
		return {
			'name': _('Manufacure Order'),
			'view_mode': 'tree,form',
			'res_model': 'mrp.production',
			'domain': [('id', 'in', purchases.ids)],
			'type': 'ir.actions.act_window',
			}


class PurchaseOrder(models.Model):
	_inherit = 'purchase.order'

	sale_ord_id = fields.Many2one('sale.order', string='Sale Order',readonly=True)
