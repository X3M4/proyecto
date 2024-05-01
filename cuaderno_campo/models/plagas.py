from odoo import models, fields, api

class Plaga (models.Model):
    _name = 'cc.plagas'
    _description = 'Plagas'
    
    name = fields.Char(
        string='Nombre',
        required=True,
    )
    
    descripcion = fields.Text(
        string='Descripción',
    )
    
    tipo = fields.Selection(
        string='Tipo',
        selection=[
            ('insecto', 'Insecto'),
            ('hongo', 'Hongo'),
            ('bacteria', 'Bacteria'),
            ('virus', 'Virus'),
            ('otro', 'Otro'),
        ]
    )
    
    sintomas = fields.Text(
        string='Síntomas',
    )
    
    variedades_id = fields.Many2many(
        string='Variedad',
        comodel_name='cc.variedades',
    )
    
    
    num_especies = fields.Integer(
        string='Número de especies',
        compute = '_compute_num_especies',
    )
    
    
    tratamiento_ids = fields.One2many(
        string='Tratamiento',
        comodel_name='cc.tratamientos',
        inverse_name='plaga_id',
    )
    
        
    #Campos calculados
    def _compute_num_especies(self):
        for record in self:
            record.num_especies = len(record.variedades_id)
    
    #Acciones smart button
    def action_view_varieties(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Variedades',
            'res_model': 'cc.variedades',
            'view_mode': 'tree,form',
            'domain': [('plaga_ids', 'in', self.ids)],
        }
    
    @api.constrains('name')
    def check_name(self):
        for record in self:
            if record.name:
                if len(record.name) < 3:
                    raise ValidationError('El nombre de la plaga debe tener al menos 3 caracteres')
                if not record.name.isalpha():
                    raise ValidationError('El nombre de la plaga solo puede contener letras')