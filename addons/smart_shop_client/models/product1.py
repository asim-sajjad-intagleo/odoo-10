
import xmlrpclib
# from odoo import models, api
# from odoo.addons.website.models.website import slug


protocol = 'http'
host = 'localhost'
# host = 'test.abc'
port = 8069

# XML-RPC authentication
com = xmlrpclib.ServerProxy('%s://%s:%s/xmlrpc/common' % (protocol, host, port))
db_name = 'test.abc'
user = 'admin'
pwd = 'admin'
uid = com.login(db_name, user, pwd)
# host = 'test.abc'
sock = xmlrpclib.ServerProxy('%s://%s:%s/xmlrpc/object' % (protocol, host, port))
sock.execute_kw(db_name, uid, pwd, 'product.template', 'create', [{

    'name': 'mahad1',

            }])