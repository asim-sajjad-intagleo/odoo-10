# -*- coding: utf-8 -*-
{
    'name': 'Smart Shop OAuth',
    'version': '10.0.1.0',
    'author': 'OdooGap',
    'summary': 'DigitalTown SSO',
    'description': 'Provides OAuth using DigitalTown SSO',
    'website': 'https://www.odoogap.com',
    'category': 'Website',
    'depends': [
        'auth_oauth',
    ],
    'data': [
        'data/auth_oauth_provider_data.xml',
        'data/auto_signup_data.xml',
        'views/signup.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
