from odoo import models, fields, api

class Tratamientos(models.Model):
    _name = 'cc.tratamientos'
    description = 'Tratamientos'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
    
    name = fields.Char(
        string='Nombre',
        compute = '_compute_name',
        tracking=True,
    )
    
    plaga_id = fields.Many2one(
        string='Plaga',
        comodel_name='cc.plagas',
        ondelete='restrict',
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
    
    cultivos_ids = fields.Many2many(
        string='Cultivos',
        comodel_name='cc.cultivos',
        tracking=True,
    )
    
    
    lineas_tratamiento_ids = fields.One2many(
        string='Lineas de Tratamiento',
        comodel_name='cc.lineas.tratamiento',
        inverse_name='tratamiento_id',
        tracking=True,
    )
    
    
    aplicador_id = fields.Many2one(
        string='Aplicador',
        comodel_name='cc.aplicadores',
    )
    
    
    
    
    #Campos calculados
    @api.depends('tipo')
    def _compute_name(self):
            for record in self:
                record.name = str(record.plaga_id.name) + '-' + str(fields.Date.today())
    
    
class LineasTratamiento(models.Model):
    _name = 'cc.lineas.tratamiento'
    _description = 'Lineas de tratamiento'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
    
    
    
    tratamiento_id = fields.Many2one(
        string='Tratamiento',
        comodel_name='cc.tratamientos',
    )
    
    
    producto_ids = fields.Many2one(
        string='Productos',
        comodel_name='product.template',
        
    )
    
    
    dosis = fields.Float(
        string='Dosis',
        required=True,
        help = 'Dosis del tratamiento'
    )
    
    
    fecha = fields.Date(
        string='Fecha',
        default=fields.Date.context_today,
    )
    
    aplicador_ids = fields.One2many(
        string='Aplicadores',
        comodel_name='cc.aplicadores',
        inverse_name='linea_tratamiento_id',
    )