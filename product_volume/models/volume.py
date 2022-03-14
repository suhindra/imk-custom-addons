# -*- coding: utf-8 -*-

from odoo import api, models, fields

class ProductDimensionsVolume(models.Model):
    _inherit = 'product.template'

    length = fields.Char(string="Length")
    breadth = fields.Char(string="Breadth")
    height = fields.Char(string="Height")
    wide = fields.Char(string="Wide")
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
