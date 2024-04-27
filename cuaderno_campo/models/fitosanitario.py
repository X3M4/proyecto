from odoo import models, api, fields

    
class cc_fitosanitario(models.Model):
    _name = 'cc.fitosanitario'
       
    num_registro = fields.Char(
        string='Nº Registro',
        required=True,
        help = 'Nº de registro del fitosanitario'
    )  
    
    name = fields.Char(
        string='Nombre',
        required=True,
        help = 'Nombre comercial'
    )
       
    titular = fields.Char(
        string='titular',
        required=True,
        help = 'Distribuidora del producto'
    )  
    
    fabricante = fields.Char(
        string='Fabricante',
        help='Fabricante del producto'
    )
      
    fabrica = fields.Char(
        string='Fábrica',
        help='Centro de fabricación'
    )
      
    formulado = fields.Char(
        string='Formulado',
        required=True,
        help='Principios activos'
    )
      
    estado = fields.Selection(
        string='Estado',
        selection=[
            ('1', 'Vigente'), 
            ('2', 'Cancelado')
        ],
        required=True
    )
    
    fecha_caducidad = fields.Date(
        string='Caducidad',
        default=fields.Date.context_today,
        help='Fecha de caducidad del fitosanitario'
    )
    
    fecha_inscripcion = fields.Date(
        string='Fecha inscripción',
        default=fields.Date.context_today,
        help='Fecha de inscripción del fitosanitario'
    )
    
    fecha_renovacion = fields.Date(
        string='Fecha de renovación',
        default=fields.Date.context_today,
        help='Fecha de renovación del fitosanitario'
    )
    
    fecha_modificacion = fields.Date(
        string='Fecha de modificación',
        default=fields.Date.context_today,
        help='Fecha de modificación del registro'
    )
    
    fecha_limite_venta = fields.Date(
        string='Fecha límite de venta',
        default=fields.Date.context_today,
        help='Fecha de límite de venta del fitosanitario'
    )
    
    fecha_autorizacion = fields.Date(
        string='Fecha de autorización',
        default=fields.Date.context_today,
        help='Fecha de autorización del fitosanitario'
    )