# -*- coding: utf-8 -*-
from odoo import models, fields, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    xmlrpc_dbname = fields.Char(string=_('XML-RPC Database'), readonly=True)
    xmlrpc_user = fields.Char(string=_('XML-RPC User'), readonly=True)
    xmlrpc_pwd = fields.Char(string=_('XML-RPC Password'), readonly=True)
    xmlrpc_protocol = fields.Char(string=_('XML-RPC Protocol'), readonly=True)
    xmlrpc_host = fields.Char(string=_('XML-RPC Host'), readonly=True)
    xmlrpc_port = fields.Integer(string=_('XML-RPC Port'), readonly=True)
