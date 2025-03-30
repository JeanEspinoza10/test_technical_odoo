# -*- coding: utf-8 -*-
{
    'name': "currency_converter",
    'summary': """""",
    'description': """
        Module use for converting currencies.
    """,
    'author': "Jean Espinoza",
    'website': "https://portafolio.jespinoza.site/",
    'category': 'Technical Test',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/currency_converter_view.xml',
        
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
