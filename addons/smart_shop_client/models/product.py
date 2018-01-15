# -*- coding: utf-8 -*-
import xmlrpclib

from odoo import models, api
from odoo.addons.website.models.website import slug


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def create(self, vals):
        product = super(ProductTemplate, self).create(vals)
        if 'website_published' in vals and vals['website_published']:
            # Create product on master instance if website_published=True
            self.synchronize_product_on_master_instance(False, product)
        return product

    @api.multi
    def write(self, vals):
        product = super(ProductTemplate, self).write(vals)
        for rec in self:
            if rec.website_published:
                # Update product on master instance if website_published=True
                rec.synchronize_product_on_master_instance(False, rec)
            else:
                # Delete product on master instance if website_published=False
                rec.synchronize_product_on_master_instance(True, rec)
        return product

    @api.multi
    def unlink(self):
        product = super(ProductTemplate, self).unlink()
        for rec in self:
            # Delete product on master instance
            rec.synchronize_product_on_master_instance(True, rec)
        return product

    # TODO: update product with more fields
    def synchronize_product_on_master_instance(self, unlink, product):
        """
        Synchronize product with the master instance after create / update / delete. Executing this method after and
        not before insures a rollback if the xml-rpc call is not successful
        """

        # Credentials
        db_name = self.env.ref('smart_shop_common.master_db_name').value
        user = self.env.ref('smart_shop_common.master_xmlrpc_user').value
        pwd = self.env.ref('smart_shop_common.master_xmlrpc_pwd').value
        protocol = self.env.ref('smart_shop_common.master_xmlrpc_protocol').value
        host = self.env.ref('smart_shop_common.master_xmlrpc_host').value
        port = self.env.ref('smart_shop_common.master_xmlrpc_port').value

        # XML-RPC authentication
        com = xmlrpclib.ServerProxy('%s://%s:%s/xmlrpc/common' % (protocol, host, port))
        uid = com.login(db_name, user, pwd)
        sock = xmlrpclib.ServerProxy('%s://%s:%s/xmlrpc/object' % (protocol, host, port))

        # Check if product exists
        result = sock.execute_kw(db_name, uid, pwd, 'product.template', 'search_read', [[
            ['external_product', '=', True], ['store_product_id', '=', product.id]
        ]], {'fields': ['id'], 'limit': 1})

        web_base_url = self.env['ir.config_parameter'].get_param('web.base.url')

        if result:
            if unlink:
                # Delete product
                sock.execute_kw(db_name, uid, pwd, 'product.template', 'unlink', [[result[0]['id']]])
            else:
                # Update product
                sock.execute_kw(db_name, uid, pwd, 'product.template', 'write', [[result[0]['id']], {
                    'store_url': '%s/shop/product/%s' % (web_base_url, slug(product)),
                    'name': product.name,
                    'description_sale': product.description_sale,
                    'state_id': product.state_id.id,
                    'country_id': product.country_id.id,
                    'city_name': product.city_name,
                    'site_id': product.site_id,
                    'longitude': product.longitude,
                    'latitude': product.latitude,
                }])
        else:
            # Create product
            sock.execute_kw(db_name, uid, pwd, 'product.template', 'create', [{
                'external_product': True,
                'store_name': self.env.ref('smart_shop_client.store_name').value,
                'store_product_id': product.id,
                'store_url': '%s/shop/product/%s' % (web_base_url, slug(product)),
                'name': product.name,
                'description_sale': product.description_sale,
                'state_id': product.state_id.id,
                'country_id': product.country_id.id,
                'city_name': product.city_name,
                'site_id': product.site_id,
                'longitude': product.longitude,
                'latitude': product.latitude,

            }])