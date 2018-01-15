# -*- coding: utf-8 -*-
from odoo.addons.auth_oauth.controllers.main import OAuthLogin
from odoo.http import request


class DigitalTownOAuthLogin(OAuthLogin):
    def list_providers(self):
        env = request.env
        providers = super(DigitalTownOAuthLogin, self).list_providers()
        if providers:
            digitaltown = env['auth.oauth.provider'].sudo().search([
                ('id', '=', env.ref('smart_shop_oauth.auth_oauth_provider_digitaltown').id),
            ], limit=1)
            if digitaltown:
                for provider in providers:
                    # Replace response_type token with code if DigitalTown OAuth
                    if provider['auth_endpoint'] == digitaltown[0].auth_endpoint:
                        provider['auth_link'] = provider['auth_link'].replace('response_type=token',
                                                                              'response_type=code')
        return providers
