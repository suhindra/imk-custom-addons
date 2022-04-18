from openerp import api, fields, models
import openerp.addons.decimal_precision as dp
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_po = fields.Char(required=True, string='Customer PO')
    customer_shipment_date = fields.Date(required=True, default=fields.Date.context_today, string='Customer Shipment Date')

    @api.multi
    def _prepare_invoice(self):
        self.ensure_one()
        invoice_vals = super(SaleOrder, self)._prepare_invoice()
        invoice_vals['customer_po'] = self.customer_po
        return invoice_vals

    @api.multi
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for do_pick in self.picking_ids:
            do_pick.write({'customer_po': self.customer_po})
        purchases = self.env['purchase.order'].search([('origin','=', self.name)])
        for purchase_item in purchases:
            purchase_item.write({
                'customer_po': self.customer_po,
                'sale_ord_id': self.id
                })
        return res

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # joint = fields.Selection('Joint', related='product_id.joint', store=True)
    JOINS = [('glue', 'Glue'), ('stitch', 'Stitch'), ('lepas', 'Lepas')]
    FLUTES = [('bf', 'BF'), ('cf', 'CF'), ('bcf', 'BCF')]
    join = fields.Selection(string="Join", selection=JOINS,  related='product_id.join', store=True, readonly=True)
    flute = fields.Selection(string="Flute", selection=FLUTES,  related='product_id.flute', store=True, readonly=True)
    wide = fields.Char(string="Sheet Size", related='product_id.wide', store=True, readonly=True)
    weight = fields.Float(string="Weight", related='product_id.weight', store=True, readonly=True)
    

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    customer_po = fields.Char(string='Customer PO')


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    # joint = fields.Selection('Joint', related='product_id.joint', store=True)
    JOINS = [('glue', 'Glue'), ('stitch', 'Stitch'), ('lepas', 'Lepas')]
    FLUTES = [('bf', 'BF'), ('cf', 'CF'), ('bcf', 'BCF')]
    join = fields.Selection(string="Join", selection=JOINS,  related='product_id.join', store=True, readonly=True)
    flute = fields.Selection(string="Flute", selection=FLUTES,  related='product_id.flute', store=True, readonly=True)
    wide = fields.Char(string="Sheet Size", related='product_id.wide', store=True, readonly=True)
    weight = fields.Float(string="Weight", related='product_id.weight', store=True, readonly=True)
    
    