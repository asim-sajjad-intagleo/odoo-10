# -*- coding: utf-8 -*-
from odoo import models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def create_admin_user(self, name, login, oauth_uid):
        ResUsers = self.env['res.users']

        # Create User with default groups and oauth credentials
        user = ResUsers.create({
            'name': name,
            'login': login,
            'email': login,
            'oauth_uid': oauth_uid,
            'oauth_provider_id': self.env.ref('smart_shop_oauth.auth_oauth_provider_digitaltown').id,
        })

        # Update user with admin groups
        user.update({
            'groups_id': [(4, self.env.ref('base.group_erp_manager').id)],
        })
        user.update({
            'groups_id': [(4, self.env.ref('base.group_system').id)],
        })

        return True
