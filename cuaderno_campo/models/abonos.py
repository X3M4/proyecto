from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Abonos(models.Model):
    _name = 'cc.abonos'
    _description = 'Abonos'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    
    name = fields.Char(
        string='Nombre',
        help='Nombre del abonado',
        tracking=True,
    )
    
    origen = fields.Selection(
        string='Tipo',
        selection=[
            ('1', 'Orgánico'),
            ('2', 'Mineral'),
            ('3', 'Orgánico/Mineral'),
        ],
        default='1',
        tracking=True,
    )
    
    tipo = fields.Selection(
        string='Forma',
        selection=[
            ('1', 'Granulado'),
            ('2', 'Microgranulado'),
            ('3', 'Polvo'),
            ('4', 'Líquido'),
        ],
        default='1',
        tracking=True,
    )
    
    fabricante = fields.Many2one(
        comodel_name='res.partner',
        string='Fabricante',
        tracking=True,
    )
    
    nitrogeno = fields.Integer(
        string='Nitrógeno',
        default=0,
        help='Cantidad de Nitrógeno en Kg',
        tracking=True,
    )
    
    fosforo = fields.Integer(
        string='Fósforo',
        default=0,
        help='Cantidad de Fósforo en Kg',
        tracking=True,
    )
    
    potasio = fields.Integer(
        string='Potasio',
        required=True,
        default=0,
        help='Cantidad de Potasio en Kg',
        tracking=True,
    )
    
    calcio = fields.Integer(
        string='Calcio',
        help='Cantidad de Calcio en Kg',
        default=0,
        tracking=True,
    )
    
    azufre = fields.Integer(
        string='Azufre',
        help='Cantidad de Azufre en Kg',
        default=0,
        tracking=True,
    )
    
    magnesio = fields.Integer(
        string='Magnesio',
        help='Cantidad de Magnesio en Kg',
        default=0,
        tracking=True,
    )
    
    @api.constrains('nitrogeno', 'fosforo', 'potasio', 'calcio', 'azufre', 'magnesio')
    def _check_abonado(self):
        for record in self:
            if record.nitrogeno < 0 or record.fosforo < 0 or record.potasio < 0:
                raise ValidationError('La cantidad de abonado no puede ser negativa')
    
    