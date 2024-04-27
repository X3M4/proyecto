from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class ProductoFitosanitario(models.Model):
    _inherit = 'product.template'
    
    
    fitosanitario_id = fields.Many2one(
        string='Fitosanitario',
        comodel_name='cc.fitosanitario',
    )
        
    es_producto = fields.Boolean(
        string='Es producto',
        default=False,
        help='Indica si el producto es un fitosanitario'
    )
    
    tipo = fields.Selection(
        string='Tipo',
        selection=[
            ('1', 'Herbicida'),
            ('2', 'Insecticida'),
            ('3', 'Fungicida'),
            ('4', 'Acaricida'),
            ('5', 'Nematicida'),
            ('6', 'Bactericida'),
            ('7', 'Otros'),
        ],
        default='7',
        related='fitosanitario_id.tipo'
    )
    
    num_registro = fields.Char(
        string='Nº Registro',
        help = 'Nº de registro del fitosanitario',
        related = 'fitosanitario_id.num_registro'
    )
    
    formulado = fields.Char(
        string='Formulado',
        help='Principios activos',
        related = 'fitosanitario_id.formulado'
    )
    
    fecha_caducidad = fields.Date(
        string='Caducidad',
        help='Fecha de caducidad del fitosanitario',
        related = 'fitosanitario_id.fecha_caducidad'
    )
    
    estado = fields.Selection(
        string='Estado',
        selection=[
            ('1', 'Vigente'), 
            ('2', 'Cancelado')
        ],
        related = 'fitosanitario_id.estado'
    )