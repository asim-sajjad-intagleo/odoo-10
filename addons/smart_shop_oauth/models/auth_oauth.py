# -*- coding: utf-8 -*-
from odoo import fields, models, _
import requests

from odoo.exceptions import UserError
import json
import urllib2
import webbrowser


class AuthOAuthProvider(models.Model):
    _inherit = 'auth.oauth.provider'

    client_secret = fields.Char(string=_('Client Secret'))

    def get_digitaltown_oauth_provider(self):
        return self.env['auth.oauth.provider'].sudo().search([
            ('id', '=', self.env.ref('smart_shop_oauth.auth_oauth_provider_digitaltown').id),
        ], limit=1)

    def create_digitaltown_oauth_client(self, access_token, uuid, subdomain_name):
        url = 'https://v1-sso-api.digitaltown.com/api/users/clients'
        params = {
            'userID': uuid,
            'name': subdomain_name,
            'redirect': 'https://%s/auth_oauth/signin' % subdomain_name,
        }
        headers = {'Authorization': 'Bearer %s' % access_token}

        f = requests.post(url=url, params=params, headers=headers)
        response = f.content
        response = json.loads(response)

        if response.get('error'):
            raise UserError(_('Could not create the client: %s') % response)

        return response
        # url = 'https://v1-sso-api.digitaltown.com/api/users/clients'
        # response = {'id': '3xwvdyzkel4dqk9ogqj51npr8',
        #             'secret': 'M59C9WWKbqwOhfWpSrTT4GoahS4QH9sWZ0fpExaV'}
        # # url = 'https://v1-sso-api.digitaltown.com/oauth/authorize'
        # # url = 'https://api.digitaltown.com/sso/token'
        # # params = {
        # #     'userID': uuid,
        # #     'name': subdomain_name,
        # #     'redirect': 'https://%s/auth_oauth/signin' % subdomain_name,
        # # }
        # # params = {
        # #     'client_id': 'vdgjle3q2r9l8d48756xopbzw',
        # #     'client_secret': 'zjk1E7aNlPVEoeHzE93yb9zdaPBSMoGC3uSAmRzh',
        # #     'grant_type': 'authorization_code',
        # #     'code': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImNkMDY0YTIwOWE1MzEwZmM0NjJmYTAwZWRiZTNjZWFiMTQxOTBhNzNmNzMwYTg0YzM1YzhiNGJkZjZkYWQxZDkyMjYwZjgxNTJlNmZjZGE1In0.eyJhdWQiOiIxMTkiLCJqdGkiOiJjZDA2NGEyMDlhNTMxMGZjNDYyZmEwMGVkYmUzY2VhYjE0MTkwYTczZjczMGE4NGMzNWM4YjRiZGY2ZGFkMWQ5MjI2MGY4MTUyZTZmY2RhNSIsImlhdCI6MTUxMTg1NjUwMiwibmJmIjoxNTExODU2NTAyLCJleHAiOjE1NDMzOTI1MDIsInN1YiI6IjM1MDM1YWY2LWM5ZjAtMTFlNy1iZmQwLTBhM2RiN2M5ZjdkMiIsInNjb3BlcyI6WyJJRCJdfQ.p_8odXA5DfVM4H-tNXGmAoboma41AuBfde7MU7urnfNJzlVGgLSbjrklyinWrUkLfGIGQ6ADHaoMsMYnNykd6YG66TZNxMV3KceyJFtZdg4g0JQUKt7UySPCfnSqF0OuV4IrPG5zvi3oofTX0g0j14j4_8vTTKPlZXDHJO1r3dj1Z6s9o8bk_FbNNI_saTzbAnzUkZwekF0MrKyFN-zPYoXp5Yrif7RlNZBnk8-bvg8TV99kqVYXxPZqp3eTuwiGOrgaOAjJt9me4Q6DaVPNz4w2Fk7Nb_LngUCosNaCCFBkc0ugQSDsCR_l70sh5-WannpB3W7vg965AIjpkt2EZehjbiSOMvJvU9Uwwkfv87HTfGl6wZTDquP7D4V9gAM8sTzPlpejYiZlxYfUEwgoQfLQPFyi78W3oWFq21e9GIgc20_k5WIGSqQK02IN-dSQlJKd8bfeEU-_hoLdWjBXRxqwkmymfProYiavNrOoV4T7zc6h1Ti2e9pfSZkwRCDSSSKW4huL5PXVURsJMko_KQYo37V2X3E-MCAQO6mVIqy9lJTyXOixgNLJl4bNR9YMY-KJrWEqYH2fRC0zmDNE_37qKR1kF6nt-mvVU75m07egiMapPmnr5VYGU7hoa2xpEfl5O6h5MWBV-SRdVFHZonTEq59p7o2hBJgkUzbcMx0',
        # #     'response_type': 'code',
        # #     'redirect_uri': 'https://mahad.london.shop/auth_oauth/signin',
        # #     'scope': 'email',
        # #
        # # }
        # # headers = {'Authorization': 'Bearer %s' % access_token}
        # h = webbrowser.open('https://v1-sso-api.digitaltown.com/oauth/authorize?scope=email&client_id=3xwvdyzkel4dqk9ogqj51npr8&redirect_uri=http://test.abc:8069&response_type=code', new=2)
        # # headers = {'content-type': 'application/x-www-form-urlencoded'}
        # # req = urllib2.Request('https://v1-sso-api.digitaltown.com/oauth/authorize?scope=email&client_id=3xwvdyzkel4dqk9ogqj51npr8&redirect_uri=http://test.abc:8069&response_type=code')
        # # response = urllib2.urlopen(req)
        # # # f = requests.post(url=url, params=params)
        # # # f = requests.get('https://v1-sso-api.digitaltown.com/oauth/authorize?scope=email&client_id=3xwvdyzkel4dqk9ogqj51npr8&redirect_uri=https://example2.abc&response_type=code')
        # # # response = f.content
        # # response = json.loads(response)
        # #
        # # if response.get('error'):
        # #     raise UserError(_('Could not create the client: %s') % response)
        #
        # return response
