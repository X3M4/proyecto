from odoo import models, fields, api

class variedades(models.Model):
    _name='cc.variedades'
    
    especie = fields.Char(
        string='Especie',
        required=True,
        help='Escriba la especie a sembrar. Ej. Cebolla'
    )
    
    name = fields.Char(
        string='Variedad',
        required=True,
        help='Escribe la variedad a sembrar'
    )
    
    propiedad = fields.Char(
        string='Propiedad',
        required=False,
        help='Empresa que tiene la propiedad de la patente de semilla'
    )
    
    proveedor=fields.Char(
        string='Proveedor',
        required=True,
        help='Empresa proveedora de las semillas. Puede ser la misma empresa propietaria'
    )
    
    cultivo = fields.One2many(
        string='cultivo',
        comodel_name='cc.cultivos',
        inverse_name='variedad'
    )
    
    
