from odoo import models, api, fields


class Aplicadores(models.Model):
    _name = 'cc.aplicadores'
    _description = 'Aplicadores'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
    _rec_name = 'name_id'
    
     
    name_id = fields.Many2one(
        string='Nombre',
        comodel_name='res.partner',
        ondelete='restrict',
        tracking=True,
    )
    
    numero_inscripcion = fields.Char(
        string='Nº inscripción ROPO',
        help="Escriba el número de inscripción en el ROPO")

    dni_nif = fields.Char(
        string='DNI/NIF',
        size=9,
        required=True,
        help="Escriba el número de DNI o NIF",
        tracking=True,
    )

    carnet = fields.Selection(
        string='Carnet',
        selection=[
            ('1', 'Básico'),
            ('2', 'Cualificado'),
            ('3', 'Fumigador'),
            ('4', 'Piloto')
        ],
        tracking=True,
    )

    asesor = fields.Boolean(
        string='Asesor',
        tracking=True,
    )
    
    tratamiento_id = fields.Many2one(
        string='Tratamiento',
        comodel_name='cc.tratamientos',
        ondelete='restrict',
        tracking=True,
    )
    
    linea_tratamiento_id = fields.Many2one(
        string='Linea de Tratamiento',
        comodel_name='cc.lineas.tratamiento',
        ondelete='restrict',
        tracking=True,
    )
