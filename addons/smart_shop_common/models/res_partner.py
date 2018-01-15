# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    # TODO: synchronize if client changes the opening hours in campany form
    opening_hours = fields.Char(string=_('Opening Hours'), readonly=True)
    is_store = fields.Boolean(string=_('Is Store'), readonly=True, default=False)
    store_name = fields.Char(string=_('Store Name'), readonly=True)

    @api.multi
    def unlink(self):
        if self.is_store:
            raise ValidationError(_('You can\'t delete a store.'))
        return super(ResPartner, self).unlink()
