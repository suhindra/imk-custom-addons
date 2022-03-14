# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import timedelta
from odoo.tools import float_is_zero


class purchase_order_wizard(models.TransientModel):
	_name = 'purchaseorder.wiz'
	_description = "purchase order wizard"

	partner_id = fields.Many2one('res.partner', string='Vendor')
	scheduled_date = fields.Datetime(string='Scheduled Date')
	purchase_order_ids = fields.One2many('purchase.wiz', 'sale_wiz_id',string='purchase order Create')

	@api.model
	def default_get(self, vals):
		terns = []
		active_ids = self._context.get('active_ids')
		terns_obj = self.env['sale.order'].browse(active_ids)
		precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
		if not terns_obj.order_line:
			raise UserError(_("Please add valid sale order lines...!"))
		for rec in terns_obj.order_line:
			if rec.display_type == 'line_section':
				continue
			if rec.display_type == 'line_note':
				continue
			terns.append((0, 0, {
				'product_id': rec.product_id.id,
				'product': rec.product_id.id,
				'description': rec.name,
				'product_uom_qty': rec.product_uom_qty,
				'price_unit': rec.price_unit,
				'product_uom': rec.product_uom.id,
				'price_subtotal': rec.price_subtotal,
				}))
		res = super(purchase_order_wizard, self).default_get(vals)
		res.update({'purchase_order_ids': terns})
		return res

	@api.multi
	def create_po(self):
		po_object = self.env['purchase.order']
		result = []
		active_ids = self._context.get('active_ids')
		so_obj = self.env['sale.order'].browse(active_ids)

		now = fields.Datetime.now()
		now_5_date = now - timedelta(minutes = 1)

		if self.scheduled_date:
			if self.scheduled_date < now_5_date:
				raise UserError(_("Please enter valid scheduled date...!"))

		for line in self.purchase_order_ids:
			result.append((0, 0, {  'product_id': line.product_id,
				'name': line.description,
				'product_qty': line.product_uom_qty,
				'date_planned': self.scheduled_date,
				'product_uom': line.product_uom.id,
				'price_unit': line.price_unit,
				}))

		po_order = po_object.create({'partner_id': self.partner_id.id,
									'order_line': result,
									'origin':so_obj.name,
									'payment_term_id':self.partner_id.property_supplier_payment_term_id.id,
									'date_planned':self.scheduled_date,
									'sale_ord_id': so_obj.id})
		context = dict(self.env.context or {})
		return {
			'name': _('Purchase Order'),
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': 'purchase.order',
			'view_id': self.env.ref('purchase.purchase_order_form').id,
			'res_id': po_order.id,
			'type': 'ir.actions.act_window',
			'target': 'self',
			}


class purchase_wiz(models.TransientModel):
	_name = 'purchase.wiz'
	_description = "purchase order wizard lines"

	sale_wiz_id = fields.Many2one('purchaseorder.wiz')
	product = fields.Many2one('product.product',string='product')
	product_uom = fields.Many2one('uom.uom')
	product_id = fields.Integer(string='Product')
	description = fields.Char(string='Description')
	product_uom_qty = fields.Float(string='quantity')
	price_unit = fields.Float(string='Price Unit')
	price_subtotal = fields.Float(string='Price Subtotal')
