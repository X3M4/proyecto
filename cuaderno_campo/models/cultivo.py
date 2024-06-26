from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Cultivo(models.Model):
    _name = 'cc.cultivos'
    _description = 'Cultivos'
    _inherit = ['mail.thread', 'mail.activity.mixin',]

    name = fields.Char(
        string='Código',
        required=True,
        help = 'Escribe el código para parcela. Este código podría ser usado como identificador de origen en la trazabilidad',
        tracking=True,
    )

    parcela = fields.Many2one(
        comodel_name='cc.parcelas',
        string='Parcela',
        required=False,
        tracking=True,
    )
    
    superficie_disponible = fields.Float(
        string='Superficie disponible en la parcela',
        required=True,
        help='Superficie completa de la parcela',
        related='parcela.superficie_libre',
        tracking=True,
    )

    variedad = fields.Many2one(
        comodel_name='cc.variedades',
        string='Especie/Variedad',
        required=False,
        tracking=True,)

    superficie_cultivada = fields.Float(
        string='Superficie',
        required=True,
        help = 'Superficie que ocupa la variedad sembrada',
        tracking=True,
    )

    maquinaria = fields.Many2one(
        'cc.maquinaria',
        string='Maquinaria de tiro',
        required=False,
        tracking=True,
    )

    fecha_siembra = fields.Date(
        string='Fecha de siembra',
        help='Fecha estimada de siembra',
        tracking=True,
    )

    fecha_cosecha = fields.Date(
        string='Fecha de cosecha',
        help = 'Fecha estimada de cosecha',
        tracking=True,
    )

    cosecha_estimada= fields.Integer(
        string='Cosecha prevista',
        required = False,
        help='Peso de la cosecha estimada en Kg',
        tracking=True,
    )
    
    
    numero_abonados = fields.Integer(
        string='numero_abonados',
        compute = '_calculate_number_abononados',
    )
    
    
    numero_tratamientos = fields.Integer(
        string='numero_tratamientos',
        compute = '_calculate_number_tratamientos',
    )
    
    

    @api.constrains('superficie_cultivada')
    def _check_superficie_cultivada(self):
        for record in self:
            if record.superficie_disponible < 0:
                raise ValidationError('La superficie cultivada no puede ser mayor que la superficie de la parcela')
    
    @api.constrains('fecha_siembra', 'fecha_cosecha')
    def _check_fechas(self):
        for record in self:
            if record.fecha_siembra > record.fecha_cosecha:
                raise ValidationError('La fecha de siembra no puede ser posterior a la fecha de cosecha')
    
    @api.onchange('parcela')
    def _onchange_parcela(self):
        self.superficie_disponible = self.parcela.superficie_libre
    
    def _calculate_number_abononados(self):
        abonados_ids = self.env['cc.abonados'].search([('cultivos_ids', '=', self.id)])
        self.numero_abonados = len(abonados_ids)
    
    def _calculate_number_tratamientos(self):
        tratamientos_ids = self.env['cc.tratamientos'].search([('cultivos_ids', '=', self.id)])
        self.numero_tratamientos = len(tratamientos_ids)
    
        
    def action_view_abonos(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cultivos',
            'res_model': 'cc.abonados',
            'view_mode': 'tree,form',
            'domain': [('cultivos_ids', '=', self.id)],
        }
        
    def action_view_tratamientos(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cultivos',
            'res_model': 'cc.tratamientos',
            'view_mode': 'tree,form',
            'domain': [('cultivos_ids', '=', self.id)],
        }
    


