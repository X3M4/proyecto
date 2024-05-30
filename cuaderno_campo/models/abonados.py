from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Abonos(models.Model):
    _name = 'cc.abonados'
    _description = 'Abonos'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    
    name = fields.Char(
        string='Nombre',
        help='Nombre del abonado',
        tracking=True,
        compute='_compute_name',
    )
    
    
    abono_id = fields.Many2one(
        string='Abono',
        comodel_name='product.template',
        ondelete='restrict',
    )
    
    
    cantidad = fields.Integer(
        string='Kg/ha',
        help='Cantidad de abono en Kg',
        tracking=True,
    )
    
    cultivos_ids = fields.Many2many(
        string='Cultivos',
        comodel_name='cc.cultivos',
    )
    
    
    aplicador_id = fields.Many2one(
        string='Aplicador',
        comodel_name='cc.aplicadores',
        ondelete='restrict',
    )
    
    maquina_id = fields.Many2one(
        string='Maquina',
        comodel_name='cc.maquinaria',
        ondelete='restrict',
    )
    
    #Campos calculados
    @api.depends('abono_id', 'cantidad')
    def _compute_name(self):
        for record in self:
            record.name = f'{record.abono_id.name} - {record.cantidad} Kg/ha'
    
    @api.constrains('cantidad')
    def _check_cantidad(self):
        for record in self:
            if record.cantidad < 0:
                raise ValidationError('La cantidad de abono no puede ser negativa.')
    
    
    
    
    