from odoo import models, api, fields

    
class Fitosanitario(models.Model):
    _name = 'cc.fitosanitario'
    _description = 'Fitosanitario'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
       
    num_registro = fields.Char(
        string='Nº Registro',
        required=True,
        help = 'Nº de registro del fitosanitario',
        tracking=True,
    )  
    
    name = fields.Char(
        string='Nombre',
        required=True,
        help = 'Nombre comercial',
        tracking=True,
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
        tracking=True,
    )
       
    titular = fields.Char(
        string='titular',
        required=True,
        help = 'Distribuidora del producto',
        tracking=True,
    )  
    
    fabricante = fields.Char(
        string='Fabricante',
        help='Fabricante del producto',
        tracking=True,
    )
      
    fabrica = fields.Char(
        string='Fábrica',
        help='Centro de fabricación',
        tracking=True,
    )
      
    formulado = fields.Char(
        string='Formulado',
        required=True,
        help='Principios activos',
        tracking=True,
    )
      
    estado = fields.Selection(
        string='Estado',
        selection=[
            ('1', 'Vigente'), 
            ('2', 'Cancelado')
        ],
        default = '2',
        tracking=True,
    )
    
    fecha_caducidad = fields.Date(
        string='Caducidad',
        default=fields.Date.context_today,
        help='Fecha de caducidad del fitosanitario',
        tracking=True,
    )
    
    fecha_inscripcion = fields.Date(
        string='Fecha inscripción',
        default=fields.Date.context_today,
        help='Fecha de inscripción del fitosanitario',
        tracking=True,
    )
    
    fecha_renovacion = fields.Date(
        string='Fecha de renovación',
        default=fields.Date.context_today,
        help='Fecha de renovación del fitosanitario',
        tracking=True,
    )
    
    fecha_modificacion = fields.Date(
        string='Fecha de modificación',
        default=fields.Date.context_today,
        help='Fecha de modificación del registro',
        tracking=True,
    )
    
    fecha_limite_venta = fields.Date(
        string='Fecha límite de venta',
        default=fields.Date.context_today,
        help='Fecha de límite de venta del fitosanitario',
        tracking=True,
    )
    
    fecha_autorizacion = fields.Date(
        string='Fecha de autorización',
        default=fields.Date.context_today,
        help='Fecha de autorización del fitosanitario',
        tracking=True,
    )