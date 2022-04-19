# Copyright 2019 Tecnativa - Pedro M. Baeza
# Copyright 2019 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import api, fields, models, _


class ProductCustomerInfo(models.Model):
    _inherit = "product.supplierinfo"
    _name = "product.customerinfo"
    _description = "Customer Pricelist"

    name = fields.Many2one(
        string='Customer',
        domain=[('customer', '=', True)],
        help="Customer of this product",
    )


    @api.onchange('name') 
    def onchange_name(self):
        self.product_name = self.product_tmpl_id.name
        self.product_code = str() + str("-") + str(self.name.ref) + str("-") + str() #B-0013-003

    @api.model
    def get_import_templates(self):
        return [{
            'label': _('Import Template for Customer Pricelists'),
            'template': '/product_supplierinfo_for_customer/static/xls/'
                        'product_customerinfo.xls'
        }]
