# -*- coding: utf-8 -*-
{
    'name': "cuaderno_campo_gastos",

    'summary': "Gestión de gastos imputados al cuaderno de campo",
    
    "version": "17.0.1.0.0",

    'description': """
        Módulo para la gestión de gastos relativa al cuaderno de campo de una explotación agrícola
    """,

    'author': "Chema Fernández",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    'application': True,
    # Check
    'category': 'Uncategorized',
    'version': '0.1',
    
    # any module necessary for this one to work correctly
    'depends': ['base','cuaderno_campo',],

    # always loaded
    'data': [
        'views/producto_fitosanitario.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],

}   