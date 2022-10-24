# coding: utf-8

from openerp import models, fields, api, _
import logging
_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    customer_po = fields.Char(string='Customer PO')

    @api.multi
    def print_sj(self):
        return self.env.ref('imk_custom_report.report_surat_jalan_menu').report_action(self)

    @api.multi
    def print_sttb(self):
        return self.env.ref('imk_custom_report.report_tanda_terima_barang_menu').report_action(self)