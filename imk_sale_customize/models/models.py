from openerp import api, fields, models
import openerp.addons.decimal_precision as dp
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_po = fields.Char(required=True, string='Customer PO')
    customer_shipment_date = fields.Date(required=True, default=fields.Date.context_today, string='Customer Shipment Date')


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        if self.product_id.product_template_attribute_value_ids:
            self.product_template_attribute_value_ids = [(6, 0, self.product_id.attribute_line_ids.ids)]
