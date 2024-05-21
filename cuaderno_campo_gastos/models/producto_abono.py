from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ProductoFitosanitario(models.Model):
    _inherit = 'product.template'
    
    
    abono_id = fields.Many2one(
        string='Abono',
        comodel_name='cc.abonos',
    )
    
    es_abono = fields.Boolean(
        string='Es abono',
        default=False,
        help='Indica si el producto es un tipo de abono'
    )
    
    nitrogeno = fields.Integer(
        string='N',
        default=0,
        help='Cantidad de Nitrógeno en Kg',
        related='abono_id.nitrogeno'
    )
    
    fosforo = fields.Integer(
        string='P',
        default=0,
        help='Cantidad de Fósforo en Kg',
        related='abono_id.fosforo'
    )
    
    potasio = fields.Integer(
        string='K',
        required=True,
        help='Cantidad de Potasio en Kg',
        related='abono_id.potasio'
    )
    
    magnesio = fields.Integer(
        string='Mg',
        required=True,
        help='Cantidad de Magnesio en Kg',
        related='abono_id.magnesio'
    )
    
    azufre = fields.Integer(
        string='S',
        required=True,
        help='Cantidad de Azufre en Kg',
        related='abono_id.azufre'
    )
    
    calcio = fields.Integer(
        string='Ca',
        required=True,
        help='Cantidad de Calcio en Kg',
        related='abono_id.calcio'
    )
    
    