from odoo import models, api, fields


class municipios(models.Model):
    _name = 'cc.municipios'

    provincia = fields.Integer(
        string='Provincia',
    )

    municipios = fields.Integer(
        string='Municipio'
    )

    name = fields.Char(
        string='Nombre'
    )

    '''@staticmethod
    def get_provincias(env):
        municipios = env['cc.municipios'].search([])
        provincias_set = set()
        for municipio in municipios:
            provincias_set.add(municipio.provincia)
        provincias_list = list(provincias_set)
        return provincias_list'''
