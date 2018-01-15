# -*- coding: utf-8 -*-
import werkzeug

from odoo import http
from odoo.http import request


class WebsiteOpenStore(http.Controller):
    @http.route(['/open-store'], type='http', auth='public', website=True)
    def open_store(self, **kw):
        env = request.env
        param = 'accessToken'

        # If accessToken and it's the first time
        if param in kw and env['ir.config_parameter'].sudo().get_param('store_is_open', '') == '0':
            ResUsers = env['res.users']
            # Get DigitalTown OAuth user info with the accessToken
            validation = ResUsers.request_oauth_user_info(kw[param])
            if validation:
                # Get DigitalTown OAuth provider
                digitaltown = env['auth.oauth.provider'].get_digitaltown_oauth_provider()
                if digitaltown:
                    params = {'access_token': kw[param]}
                    user = ResUsers.sudo().search([('id', '=', env.ref('smart_shop_common.res_users_client').id)],
                                                  limit=1)
                    # Update user info
                    ResUsers.update_oauth_user_info(user[0], digitaltown.id, validation, params)
                    # Update first time flag
                    env['ir.config_parameter'].sudo().set_param('store_is_open', '1')

                    # Commit changes, if the authenticate fails, the user is still updated/created
                    env.cr.commit()

                    # Authenticate user
                    request.session.authenticate(env.cr.dbname, validation['email'], kw[param])

        return werkzeug.utils.redirect('/')
