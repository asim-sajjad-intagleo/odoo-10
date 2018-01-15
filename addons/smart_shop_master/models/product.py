# -*- coding: utf-8 -*-
from odoo import models, fields, _


class ProductTemplate(models.Model):
    _order = 'country_id desc'
    _order = 'state_id asc'
    _inherit = 'product.template'

    external_product = fields.Boolean(string=_('External Product'), readonly=True, default=False)
    store_name = fields.Char(string=_('Store Name'), readonly=True)
    store_url = fields.Char(string=_('Store URL'), readonly=True)
    store_product_id = fields.Integer(string=_('Store Product ID'), readonly=True, index=True)
    city_name = fields.Char(string=_('City Name'), required=True)
    latitude = fields.Float(string=_('Latitude'), required=False)
    longitude = fields.Float(string=_('Longitute'), required=False)
    site_id = fields.Integer(string=_('Site Id'), required=False)
    state_id = fields.Many2one('res.country.state', string=_('State Id'), required=False)
    country_id = fields.Many2one('res.country', string=_('Country Id'), required=False)

