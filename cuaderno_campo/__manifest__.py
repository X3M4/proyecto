# -*- coding: utf-8 -*-
{
    'name': "cuaderno de campo",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Chema Fernández",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    'application': True,
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'portal'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/aplicador/aplicadores_view.xml',
        'views/maquinaria/maquinaria_view.xml',
        'views/fitosanitario/fitosanitario_view.xml',
        'views/parcelas/parcelas_view.xml',
        'views/variedades/variedades_view.xml',
        'views/cultivos/cultivo_view.xml',
        'views/plagas/plagas.view.xml',
        'views/tratamientos/tratamientos.xml',
        'views/abonos/abonos_view.xml',
        'views/abonos/abonados_view.xml',
        'views/menus/cuaderno_campo_menus.xml',
        'views/templates.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

