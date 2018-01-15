# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

PARAMS = [
    'website_id',
    'website_name',
    'google_maps_api_key',
    'google_analytics_key',
    'social_twitter',
    'social_facebook',
    'social_github',
    'social_linkedin',
    'social_youtube',
    'social_googleplus',
    'favicon',
]


class StoreConfigSettings(models.Model):
    _name = 'store.config.settings'
    _description = 'Website Settings'
    _rec_name = 'website_name'

    def _default_website(self):
        return self.env['website'].search([], limit=1)

    website_id = fields.Many2one('website', string=_('website'), default=_default_website, required=True)
    website_name = fields.Char(string=_('Website Name'), related='website_id.name')
    google_maps_api_key = fields.Char(string=_('Google Maps API Key'))
    google_analytics_key = fields.Char('Google Analytics Key', related='website_id.google_analytics_key')
    social_twitter = fields.Char(related='website_id.social_twitter')
    social_facebook = fields.Char(related='website_id.social_facebook')
    social_github = fields.Char(related='website_id.social_github')
    social_linkedin = fields.Char(related='website_id.social_linkedin')
    social_youtube = fields.Char(related='website_id.social_youtube')
    social_googleplus = fields.Char(related='website_id.social_googleplus')
    favicon = fields.Binary(string=_('Favicon'), related='website_id.favicon')

    @api.model
    def create(self, vals):
        settings = super(StoreConfigSettings, self).create(vals)
        self.set_config_parameter(settings)
        return settings

    @api.multi
    def write(self, vals):
        settings = super(StoreConfigSettings, self).write(vals)
        for rec in self:
            self.set_config_parameter(rec)
        return settings

    @api.multi
    def unlink(self):
        settings = super(StoreConfigSettings, self).unlink()
        for rec in self:
            self.set_config_parameter(rec)
        return settings

    def set_config_parameter(self, rec):
        for param in PARAMS:
            if param == 'google_maps_api_key':
                self.env['ir.config_parameter'].sudo().set_param('google_maps_api_key',
                                                                 (self.google_maps_api_key or '').strip(),
                                                                 groups=['base.group_system'])
            else:
                self.env['ir.config_parameter'].sudo().set_param(param, getattr(rec, param, False))
