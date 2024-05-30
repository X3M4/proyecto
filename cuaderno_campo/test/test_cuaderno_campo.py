
from odoo.test import common
from odoo import fields, models

class TestCuadernoCampo(common.TransactionCase):
    def setUpClass(self):
        super().setUpClass()

        
    def test_cuaderno_campo_update(self):
            # Create a new record
            parcela = self.env['cc.parcelas'].create({
                'codigo_provincia': '02',
                'codigo_municipio': '069',
                'name': 'La Roda',
                'finca': 'Finca de Prueba',
                'agregado': 1,
                'zona': 2,
                'poligono': 3,
                'parcela': 4,
            })
            # Update the record
            parcela.write({
                'codigo_provincia': '03',
                'codigo_municipio': '070',
                'name': 'Albacete',
                'finca': 'Finca de Prueba 2',
                'agregado': 2,
                'zona': 3,
                'poligono': 4,
                'parcela': 5,
            })
            # Check that the record was updated with the correct values
            self.assertEqual(parcela.codigo_provincia, '03')
            self.assertEqual(parcela.codigo_municipio, '070')
            self.assertEqual(parcela.name, 'Albacete')
            self.assertEqual(parcela.finca, 'Finca de Prueba 2')
            self.assertEqual(parcela.agregado, 2)
            self.assertEqual(parcela.zona, 3)
            self.assertEqual(parcela.poligono, 4)
            self.assertEqual(parcela.parcela, 5)

        def test_cuaderno_campo_delete(self):
            # Create a new record
            parcela = self.env['cc.parcelas'].create({
                'codigo_provincia': '02',
                'codigo_municipio': '069',
                'name': 'La Roda',
                'finca': 'Finca de Prueba',
                'agregado': 1,
                'zona': 2,
                'poligono': 3,
                'parcela': 4,
            })
            # Delete the record
            parcela.unlink()
            # Check that the record was deleted
            self.assertFalse(parcela.exists())
        
        