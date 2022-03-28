# -*- coding: utf-8 -*-

from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)


class ProductDimensionsVolume(models.Model):
    _inherit = 'product.template'

    length = fields.Char(string="Length")
    breadth = fields.Char(string="Breadth")
    height = fields.Char(string="Height")
    length_sheet = fields.Char(string="Length Sheet")
    breadth_sheet = fields.Char(string="Breadth Sheet")
    wide = fields.Char(string="Sheet Size")
    inner_size = fields.Char(string="Sheet Size")
    kw1 = fields.Char(string="KW 1")
    kw2 = fields.Char(string="KW 2")
    kw3 = fields.Char(string="KW 3")
    kw4 = fields.Char(string="KW 4")
    kw5 = fields.Char(string="KW 5")

    @api.onchange('length','breadth','height') 
    def onchange_l_b_h(self):
        _logger.info('FYI: This is happening1')
        self.volume = float(self.length if self.length else 0) * float(self.breadth if self.breadth else 0) * float(self.height if self.height else 0)

    @api.onchange('length','breadth')
    def onchange_l_b(self):
        _logger.info('FYI: This is happenin2')
        self.wide = float(self.length if self.length else 0) * float(self.breadth if self.breadth else 0)

    @api.onchange('length','breadth','height','kw1','kw2','kw3','kw4','kw5') 
    def onchange_l_b_h_kw(self):
        for val in self.attribute_line_ids:
            _logger.info('FYI: This is happening')
            _logger.info(val)
            self.inner_size 