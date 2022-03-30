# -*- coding: utf-8 -*-

from odoo import api, models, fields
import logging
import re

_logger = logging.getLogger(__name__)


class ProductDimensionsVolume(models.Model):
    _inherit = 'product.template'

    JOINS = [('glue', 'Glue'), ('stitch', 'Stitch'), ('lepas', 'Lepas')]
    FLUTES = [('bf', 'BF'), ('cf', 'CF'), ('bcf', 'BCF')]
    join = fields.Selection(string="Join", selection=JOINS, required=True)
    flute = fields.Selection(string="Flute", selection=FLUTES, required=True)
    slitter = fields.Boolean(string='Slitter');
    slotter = fields.Boolean(string='Slotter');
    die_cut = fields.Boolean(string='Die Cut');
    cetak = fields.Boolean(string='Cetak');
    glue = fields.Boolean(string='Glue');
    stitching = fields.Boolean(string='Stitching');
    length = fields.Char(string="Length")
    breadth = fields.Char(string="Breadth")
    height = fields.Char(string="Height")
    wide = fields.Char(string="Sheet Size")
    kw1 = fields.Char(string="KW 1")
    kw2 = fields.Char(string="KW 2")
    kw3 = fields.Char(string="KW 3")
    kw4 = fields.Char(string="KW 4")
    kw5 = fields.Char(string="KW 5")


    @api.onchange('length','breadth','height','kw1','kw2','kw3','kw4','kw5','flute') 
    def onchange_l_b_h_kw(self):    
        if self.flute == 'bf':
            length_sheet = 2 * (int(self.length if self.length else 0) + int(self.breadth if self.breadth else 0)) + 12 + 10 + 35 
            breadth_sheet = int(self.breadth if self.breadth else 0) + int(self.height if self.height else 0) + 9
            
        if self.flute == 'cf':
            length_sheet = 2 * (int(self.length if self.length else 0) + int(self.breadth if self.breadth else 0)) + 15 + 10 + 35 
            breadth_sheet = int(self.breadth if self.breadth else 0) + int(self.height if self.height else 0) + 13
            
        if self.flute == 'bcf':
            length_sheet = 2 * (int(self.length if self.length else 0) + int(self.breadth if self.breadth else 0)) + 28 + 10 + 40 
            breadth_sheet = int(self.breadth if self.breadth else 0) + int(self.height if self.height else 0) + 22
            
        sheet_size = length_sheet * breadth_sheet / 1000000
        self.wide = sheet_size
        weight = sheet_size * (int(re.sub('\D', '',self.kw1 if self.kw1 else 0)) + (int(re.sub('\D', '',self.kw2 if self.kw2 else 0)) * 1.4) + int(re.sub('\D', '',self.kw3 if self.kw3 else 0)) + (int(re.sub('\D', '',self.kw4 if self.kw4 else 0)) * 1.5) + int(re.sub('\D', '',self.kw5 if self.kw5 else 0))) / 1000
        self.weight = weight        