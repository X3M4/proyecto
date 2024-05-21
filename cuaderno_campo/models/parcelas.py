from odoo import models, api, fields
from odoo.exceptions import ValidationError


class Parcelas(models.Model):
    _name = 'cc.parcelas'
    _description = 'Parcelas'
    _inherit = ['mail.thread', 'mail.activity.mixin',]
    
    codigo_provincia = fields.Char(
        string='Código Provincia',
        required=True,
        help='Escriba el código de pronvincia. Ej: 02 para Albacete',
        size=2,
        tracking=True,
    )

    codigo_municipio = fields.Char(
        string='Código Municipio',
        help='Escriba el código del municipio. Ej: 069 para La Roda',
        required=True,
        size=3,
        tracking=True,
    )

    name = fields.Char(
        string='Municipio',
        required=True,
        help='Escriba el nombre del municipio',
        tracking=True,
    )
    
    finca = fields.Char(
        string='Finca',
        required=False,
        help='Nombre de la finca (no obligatorio)',
        tracking=True,
    )

    agregado = fields.Integer(
        string='Agregado',
        help='Agregado (no obligatorio)',
        tracking=True,
    )

    zona = fields.Integer(
        string='Zona',
        help='Zona (no obligatorio)',
        tracking=True,
    )

    poligono = fields.Integer(
        string='Polígono',
        required=True,
        help='Nº polígono',
        tracking=True,
    )

    parcela = fields.Integer(
        string='Parcela',
        required=True,
        help='Nº de parcela',
        tracking=True,
    )

    recinto = fields.Integer(
        string='Recinto',
        required=True,
        help='Nº de recinto',
        tracking=True,
    )

    uso = fields.Char(
        string='Uso SIGPAC',
        required=True,
        help='Familia de cultivos indicada en el SIGPAC para la parcela indicada',
        tracking=True,
    )

    superficie = fields.Float(
        string='Superficie SIGPAC (ha)',
        required=True,
        help='Superficie en hectáreas indicada en el SIGPAC para la parcela',
        tracking=True,
    )
    
    superficie_libre = fields.Float(
        string='Superficie libre (ha)',
        compute='_compute_superficie_libre',
        tracking=True,
    )

    coordenadas = fields.Char(
        String = 'Coordenadas',
        required=False,
        help='Coordenadas de la parcela según datos del SIGPAC',
        tracking=True,)

    ocupacion = fields.Selection(
        string='Ocupación',
        selection=[
            ('1', 'Propio'),
            ('2', 'Arrendado'),
            ('3', 'Otro')
        ],
        required=True,
        help='Tipo de ocupación de la parcela según titularidad',
        tracking=True,
    )

    titular_ids = fields.Many2one(
        string='Titulares',
        comodel_name='res.partner',
        tracking=True,
    )
    

    riego = fields.Selection(
        string='Sistema de cultivo (Secano/Regadío)',
        selection=[
            ('1', 'Secano'),
            ('2', 'Aspersión'),
            ('3', 'Goteo o localizado'),
            ('4', 'Gravedad'),
        ],
        required=True,
        help='Sistema de cultivo respecto al sistema de regadío',
        tracking=True,
    )

    estructura = fields.Selection(
        string='Aire libre/Protegido',
        selection=[
            ('1', 'Aire libre'),
            ('2', 'Malla'),
            ('3', 'Cubierta bajo plástico'),
            ('4', 'Invernadero'),
        ],
        required=True,
        help='Estructura respecto al sistema de cultivo',
        tracking=True,
    )

    asesoramiento = fields.Selection(
        string='Sistema de asesoramiento',
        selection=[
            ('1', 'Agricultura ecológica'),
            ('2', 'Producción Integrada'),
            ('3', 'Certificación Privada'),
            ('4', 'Agrupación de Tratamiento Integrado en Agricultura'),
            ('5', 'Asistida de un asesor'),
            ('6', 'Sin obligación de aplicar GIP')
        ],
        required=True,
        help='Sistema de asesoramiento en gestión integrada de plagas',
        tracking=True,
    )
    
    cultivo = fields.One2many(
        'cc.cultivos',
        'parcela',
        string='Cultivos',
        required=False,
        tracking=True,
    )
    
    num_cultivos = fields.Integer(
        string='Número de cultivos',
        compute='_compute_num_cultivos',
        tracking=True,
    )
    
    #Campos calculados
    def _compute_superficie_libre(self):
        superficie = 0
        for record in self:
            for cultivo in record.cultivo:
                superficie += cultivo.superficie_cultivada
            record.superficie_libre = record.superficie - superficie
            
    def _compute_num_cultivos(self):
        for record in self:
            record.num_cultivos = len(record.cultivo)
    #Restricciones
    
    @api.constrains('superficie')
    def _check_superficie(self):
        for record in self:
            if record.superficie < 0:
                raise ValueError('La superficie no puede ser negativa')
    
    @api.constrains('superficie_libre')
    def _check_superficie_libre(self):
        for record in self:
            if record.superficie_libre < 0:
                raise ValueError('La superficie libre no puede ser negativa')
            
    
    #Métodos smartbutton
    def action_view_cultivos(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Cultivos',
            'res_model': 'cc.cultivos',
            'view_mode': 'tree,form',
            'domain': [('parcela', '=', self.id)],
        }