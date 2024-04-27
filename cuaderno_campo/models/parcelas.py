from odoo import models, api, fields


class parcelas(models.Model):
    _name = 'cc.parcelas'
    
    codigo_provincia = fields.Char(
        string='Código Provincia',
        required=True,
        help='Escriba el código de pronvincia. Ej: 02 para Albacete',
        size=2
    )

    codigo_municipio = fields.Char(
        string='Código Municipio',
        help='Escriba el código del municipio. Ej: 069 para La Roda',
        required=True,
        size=3
    )

    name = fields.Char(
        string='Municipio',
        required=True,
        help='Escriba el nombre del municipio'
    )
    
    finca = fields.Char(
        string='Finca',
        required=False,
        help='Nombre de la finca (no obligatorio)'
    )

    agregado = fields.Integer(
        string='Agregado',
        help='Agregado (no obligatorio)'
    )

    zona = fields.Integer(
        string='Zona',
        help='Zona (no obligatorio)'
    )

    poligono = fields.Integer(
        string='Polígono',
        required=True,
        help='Nº polígono'
    )

    parcela = fields.Integer(
        string='Parcela',
        required=True,
        help='Nº de parcela'
    )

    recinto = fields.Integer(
        string='Recinto',
        required=True,
        help='Nº de recinto'
    )

    uso = fields.Char(
        string='Uso SIGPAC',
        required=True,
        help='Familia de cultivos indicada en el SIGPAC para la parcela indicada'
    )

    superficie = fields.Float(
        string='Superficie SIGPAC (ha)',
        required=True,
        help='Superficie en hectáreas indicada en el SIGPAC para la parcela'
    )

    coordenadas = fields.Char(
        String = 'Coordenadas',
        required=False,
        help='Coordenadas de la parcela según datos del SIGPAC')

    ocupacion = fields.Selection(
        string='Ocupación',
        selection=[
            ('1', 'Propio'),
            ('2', 'Arrendado'),
            ('3', 'Otro')
        ],
        required=True,
        help='Tipo de ocupación de la parcela según titularidad'
    )

    titular = fields.Char(
        string='Titular',
        required=True,
        help='Nombre del titular de la parcela',
        size=100,
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
        help='Sistema de cultivo respecto al sistema de regadío'
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
        help='Estructura respecto al sistema de cultivo'
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
        help='Sistema de asesoramiento en gestión integrada de plagas'
    )
    
    cultivo = fields.One2many(
        'cc.cultivos',
        'parcela',
        string='Cultivos',
        required=False
    )
