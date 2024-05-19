from odoo import models, fields, api

class Maquinaria(models.Model):
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
            ('1', 'Máquinas suspendidas o semisuspendidas'),
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

    cultivo = fields.One2many(
        'cc.cultivos',
        'maquinaria',
        string='Cultivo',
        required=False
    )

