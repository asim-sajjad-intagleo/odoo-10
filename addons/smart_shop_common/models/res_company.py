# -*- coding: utf-8 -*-
from odoo import models, fields, _


class ResCompany(models.Model):
    _inherit = 'res.company'

    opening_hours = fields.Char(string=_('Opening Hours'))
