from odoo import models, fields, api

class Variedades(models.Model):
    _name='cc.variedades'
    _description='Variedades'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
    
    especie = fields.Char(
        string='Especie',
        required=True,
        help='Escriba la especie a sembrar. Ej. Cebolla',
        tracking=True,
    )
    
    name = fields.Char(
        string='Variedad',
        required=True,
        help='Escribe la variedad a sembrar',
        tracking=True,
    )
    
    propiedad = fields.Many2one(
        string='Propiedad',
        comodel_name='res.partner',
        help='Propiedad de la licencia de la semilla',
        tracking=True,
    )
    
    proveedor=fields.Many2one(
        string='Proveedor',
        comodel_name='res.partner',
        help='Empresa que vende la semilla',
        tracking=True,
    )
    
    cultivo = fields.One2many(
        string='cultivo',
        comodel_name='cc.cultivos',
        inverse_name='variedad',
        tracking=True,
    )
    
    num_cultivos = fields.Integer(
        string='Número de cultivos',
        compute='_compute_num_cultivos',
        tracking=True,
    )
    
    #Campos calculados
    def _compute_num_cultivos(self):
        for record in self:
            record.num_cultivos = len(record.cultivo)
        
    #Acciones smart button
    def action_view_cultivos(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cultivos',
            'res_model': 'cc.cultivos',
            'view_mode': 'tree,form',
            'domain': [('variedad', '=', self.id)],
        }
    
