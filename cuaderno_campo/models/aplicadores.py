from odoo import models, api, fields


class cc_aplicadores(models.Model):
    _name = 'cc.aplicadores'
    
    name = fields.Char(
        string='Nombre y apellidos',
        required=True,
        help='Escriba el nombre y apellidos de la persona inscrita en el ROPO'
        
    )
    
    numero_inscripcion = fields.Char(
        string='Nº inscripción ROPO',
        help="Escriba el número de inscripción en el ROPO")

    dni_nif = fields.Char(
        string='DNI/NIF',
        size=9,
        required=True,
        help="Escriba el número de DNI o NIF"
    )

    carnet = fields.Selection(
        string='Carnet',
        selection=[
            ('1', 'Básico'),
            ('2', 'Cualificado'),
            ('3', 'Fumigador'),
            ('4', 'Piloto')
        ]
    )

    asesor = fields.Boolean(
        string='Asesor',
    )
