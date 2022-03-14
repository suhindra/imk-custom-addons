from openerp import api, fields, models
import openerp.addons.decimal_precision as dp
import logging
_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = "sale.order"

    customer_po = fields.Char(string='Customer PO')


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_template_attribute_value_ids = fields.Many2many('product.template.attribute.value', relation='product_variant_combination', string="Attribute Values", ondelete='restrict')

    @api.onchange('product_id')
    def product_id_change(self):
        if self.product_id.product_template_attribute_value_ids:
            self.product_template_attribute_value_ids = [(6, 0, self.product_id.product_template_attribute_value_ids.name)]
