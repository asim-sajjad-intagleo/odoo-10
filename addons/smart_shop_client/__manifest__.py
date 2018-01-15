# -*- coding: utf-8 -*-
{
    'name': 'Smart Shop Client',
    'version': '10.0.1.0',
    'author': 'OdooGap',
    'summary': 'DigitalTown .SHOP',
    'description': 'Provides an high level overview of .SHOP product',
    'website': 'https://www.odoogap.com',
    'category': 'Website',
    'depends': [
        'smart_shop_common',
        'website_crm',
        'payment_stripe',
        'account_accountant',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter_data.xml',
        'data/menus.xml',
        'data/payment_stripe_data.xml',
        'data/store_config_settings_data.xml',
        'views/website.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
