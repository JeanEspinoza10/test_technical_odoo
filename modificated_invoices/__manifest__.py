# -*- coding: utf-8 -*-
{
    'name': "modificated_invoices",
    'summary': """""",
    'description': """
        Modificated Invoices
    """,
    'author': "Jean Espinoza",
    'website': "https://portafolio.jespinoza.site/",
    'category': 'Technical Test',
    'version': '0.1',
    'depends': ['base', 'account'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'security/user_groups.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
