# -*- coding: utf-8 -*-
{
    'name': "modificated_sale_order",
    'summary': """""",
    'description': """
       Modificated Sale Order
    """,
    'author': "Jean Espinoza",
    'website': "https://portafolio.jespinoza.site/",
    'category': 'Technical Test',
    'version': '0.1',
    'depends': ['base','sale','stock'],
    'data': [
        'views/configuration_views.xml',
        'security/ir.model.access.csv',
        'data/init_config.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
