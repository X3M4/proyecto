from odoo import models, fields, api

class cc_maquinaria(models.Model):
    _name = 'cc.maquinaria'

    name = fields.Char(
        string='Nº inscripción',
        size=12,
        help='Número de registro el ROMA',
        required=True
    )

    marca = fields.Char(
        string='Marca',
        required=True,
        help='Escriba la marca'
    )

    modelo = fields.Char(
        string='Modelo',
        help='Escriba el modelo',
        required=True,
    )

    tipo = fields.Selection(
        string='Tipo',
        selection=[
            ('1', 'Máquinas suspendidas o semisusoendidas'),
            ('2', 'Máquinas remolcadas'),
            ('3', 'Tractores'),
            ('4', 'Remolques'),
            ('5', 'Máquinas automotrices')
        ],
        required=True
    )

    estado = fields.Boolean(
        string='Estado',
    )
    
    fecha_adquisicion = fields.Date(
        string='Fecha de adquisicion',
        default=fields.Date.context_today,
    )

    fecha_inspeccion = fields.Date(
        string='Fecha de inspección',
        default=fields.Date.context_today,
    )

    resultado = fields.Selection(
        string='Resultado inspección',
        selection=[
            ('1', 'Favorable'),
            ('2', 'Desfavorable')
        ],
    )
    '''
    tratamiento = fields.One2many(
        comodel_name='cc.tratamiento',
        inverse_name='maquinaria_1',
        string='Maquinaria 1',
        required=False
    )

    tratamiento_2 = fields.One2many(
        comodel_name='cc.tratamiento',
        inverse_name='maquinaria_2',
        string='Maquinaria 2',
        required=False
    )
    '''
    cultivo = fields.One2many(
        'cc.cultivos',
        'maquinaria',
        string='Cultivo',
        required=False
    )

