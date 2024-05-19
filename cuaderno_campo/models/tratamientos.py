from odoo import models, fields, api

class Tratamientos(models.Model):
    _name = 'cc.tratamientos'
    description = 'Tratamientos'
    
    name = fields.Char(
        string='Nombre',
        compute = '_compute_name',
    )
    
    plaga_id = fields.Many2one(
        string='Plaga',
        comodel_name='cc.plagas',
        ondelete='restrict',
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
    )
    
    cultivos_ids = fields.Many2many(
        string='Cultivos',
        comodel_name='cc.cultivos',
    )
    
    
    lineas_tratamiento_ids = fields.One2many(
        string='Lineas de Tratamiento',
        comodel_name='cc.lineas.tratamiento',
        inverse_name='tratamiento_id',
    )
    
    #Campos calculados
    @api.depends('tipo')
    def _compute_name(self):
            for record in self:
                record.name = str(record.plaga_id.name) + '-' + str(fields.Date.today())
    
    
class LineasTratamiento(models.Model):
    _name = 'cc.lineas.tratamiento'
    description = 'Lineas de tratamiento'
    
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