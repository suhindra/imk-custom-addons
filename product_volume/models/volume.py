# -*- coding: utf-8 -*-

from odoo import api, models, fields
import logging

_logger = logging.getLogger(__name__)


class ProductDimensionsVolume(models.Model):
    _inherit = 'product.template'

    JOINS = [('glue', 'Glue'), ('stitch', 'Stitch'), ('lepas', 'Lepas')]
    FLUTES = [('bf', 'BF'), ('cf', 'CF'), ('bcf', 'BCF')]
    join = fields.Selection(string="Join", selection=JOINS, required=True)
    flute = fields.Selection(string="Flute", selection=FLUTES, required=True)

    length = fields.Char(string="Length")
    breadth = fields.Char(string="Breadth")
    height = fields.Char(string="Height")
    length_sheet = fields.Char(string="Length Sheet")
    breadth_sheet = fields.Char(string="Breadth Sheet")
    wide = fields.Char(string="Sheet Size")
    inner_size = fields.Char(string="Inner Size")
    kw1 = fields.Char(string="KW 1")
    kw2 = fields.Char(string="KW 2")
    kw3 = fields.Char(string="KW 3")
    kw4 = fields.Char(string="KW 4")
    kw5 = fields.Char(string="KW 5")

    @api.onchange('length','breadth','height') 
    def onchange_l_b_h(self):
        self.volume = float(self.length if self.length else 0) * float(self.breadth if self.breadth else 0) * float(self.height if self.height else 0)

    @api.onchange('length','breadth')
    def onchange_l_b(self):
        self.wide = float(self.length if self.length else 0) * float(self.breadth if self.breadth else 0)

    @api.onchange('length','breadth','height','kw1','kw2','kw3','kw4','kw5') 
    def onchange_l_b_h_kw(self):
        self._origin
        _logger.info(self._origin.attribute_line_ids)
        for val in self.attribute_line_ids:
            _logger.info('FYI: This is happening')
            _logger.info(val)
            self.inner_size  = '1'