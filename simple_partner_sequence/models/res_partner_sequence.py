# -*- coding: utf-8 -*-
# CopyrightÂ© 2016 ICTSTUDIO <http://www.ictstudio.eu>
# License: AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)

from openerp import models, fields

class ResPartnerSequence(models.Model):
    _name = 'res.partner.sequence'

    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country',
        required=True
    )
    sequence_id = fields.Many2one(
        comodel_name='ir.sequence',
        string='Sequence',
        required=True
    )