from odoo import models, fields, api

class Maquinaria(models.Model):
    _name = 'cc.maquinaria'
    _description = 'Maquinaria'
    _inherit = ['mail.thread', 'mail.activity.mixin',]

    name = fields.Char(
        string='Nº inscripción',
        size=12,
        help='Número de registro el ROMA',
        required=True,
        tracking=True,
    )

    marca = fields.Char(
        string='Marca',
        required=True,
        help='Escriba la marca',
        tracking=True,
    )

    modelo = fields.Char(
        string='Modelo',
        help='Escriba el modelo',
        required=True,
        tracking=True,
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
        required=True,
        tracking=True,
    )

    estado = fields.Boolean(
        string='Estado',
        tracking=True,
    )
    
    fecha_adquisicion = fields.Date(
        string='Fecha de adquisicion',
        default=fields.Date.context_today,
        tracking=True,
    )

    fecha_inspeccion = fields.Date(
        string='Fecha de inspección',
        default=fields.Date.context_today,
        tracking=True,
    )

    resultado = fields.Selection(
        string='Resultado inspección',
        selection=[
            ('1', 'Favorable'),
            ('2', 'Desfavorable')
        ],
        tracking=True,
    )

    cultivo = fields.One2many(
        'cc.cultivos',
        'maquinaria',
        string='Cultivo',
        required=False,
        tracking=True,
    )

