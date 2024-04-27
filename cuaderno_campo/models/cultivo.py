from odoo import fields, models, api


class cultivo(models.Model):
    _name = 'cc.cultivos'

    name = fields.Char(
        string='Código',
        required=True,
        help = 'Escribe el código para parcela. Este código podría ser usado como identificador de origen en la trazabilidad'
    )

    parcela = fields.Many2one(
        comodel_name='cc.parcelas',
        string='Parcela',
        required=False
    )

    variedad = fields.Many2one(
        comodel_name='cc.variedades',
        string='Especie/Variedad',
        required=False)

    superficie_cultivada = fields.Float(
        string='Superficie',
        required=True,
        help = 'Superficie que ocupa la variedad sembrada'
    )

    maquinaria = fields.Many2one(
        'cc.maquinaria',
        string='Maquinaria de tiro',
        required=False
    )

    fecha_siembra = fields.Date(
        string='Fecha de siembra',
        required=True,
        help='Fecha estimada de siembra'
    )

    fecha_cosecha = fields.Date(
        string='Fecha de cosecha',
        required=False,
        help = 'Fecha estimada de cosecha'
    )

    cosecha_estimada= fields.Integer(
        string='Cosecha prevista',
        required = False,
        help='Peso de la cosecha estimada en Kg'
    )



