# -*- coding: utf-8 -*-
{
    'name': "modificated_payscreen",
    'summary': """""",
    'description': """
       Modificate the Payscreen
    """,
    'author': "Jean Espinoza",
    'website': "https://portafolio.jespinoza.site/",
    'category': 'Technical Test',
    'version': '0.1',
    'depends': ['base','point_of_sale'],
    'data': [
        'views/views.xml'
    ],
    'assets': {
    'point_of_sale.assets': [
        'modificated_payscreen/static/src/xml/PaymentScreen_modificated.xml',
        'modificated_payscreen/static/src/xml/CodeOperation.xml',
        'modificated_payscreen/static/src/js/Generate_code_operation.js',
        'modificated_payscreen/static/src/js/PaymentScreen_modificated.js'
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
