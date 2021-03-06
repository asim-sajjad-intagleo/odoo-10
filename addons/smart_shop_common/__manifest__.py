# -*- coding: utf-8 -*-
{
    'name': 'Smart Shop Common',
    'version': '10.0.1.0',
    'author': 'OdooGap',
    'summary': 'DigitalTown .SHOP',
    'description': 'Provides an high level overview of .SHOP product',
    'website': 'https://www.odoogap.com',
    'category': 'Website',
    'depends': [
        'smart_shop_oauth',
        'contacts',
        'product',
        'website_sale',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/ir_config_parameter_data.xml',
        'data/res_partner_data.xml',
        'data/res_users_data.xml',
        'data/website_data.xml',
        'views/res_company_view.xml',
        'views/res_partner_view.xml',
        'views/website.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
