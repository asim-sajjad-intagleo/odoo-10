# -*- coding: utf-8 -*-
{
    'name': 'Smart Shop Create Store',
    'version': '10.0.1.0',
    'author': 'OdooGap',
    'summary': 'DigitalTown .SHOP',
    'description': 'Provides an high level overview of .SHOP product',
    'website': 'https://www.odoogap.com',
    'category': 'Website',
    'depends': [
        'smart_shop_common',
    ],
    'data': [
        'data/ir_config_parameter_data.xml',
        'data/mail_template_data.xml',
        'views/homepage.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
