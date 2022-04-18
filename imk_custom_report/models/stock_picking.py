# coding: utf-8

from openerp import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    customer_po = fields.Char(required=True, string='Customer PO')