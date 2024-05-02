import unittest
import fitz

from tipos_paginas.resumen import Resumen


class TestResumen(unittest.TestCase):
    """
    Siguiente refactor: mockear la dependencia de los PDF
    """
    def setUp(self):
        pdf_prueba = fitz.open('anteriores/DISTRITO-MARCELO_SERGIO_SALLUCCI.PDF')
        paginas_resumen = [pag for pag in pdf_prueba.pages(stop=5)]
        self.resumen = Resumen(paginas_resumen)

    def tearDown(self):
        # Cerramos el archivo luego de cada test independientemente de si falla o no
        if hasattr(self, 'pdf_prueba') and hasattr(self.pdf_prueba, 'close'):
            self.pdf_prueba.close()

    def test_extraer_informacion_devuelve_indices_de_la_primer_pagina(self):
        indices_esperados = [
            "PRODUCTOS DE LANZAMIENTO",
            "PRIMERA LINEA DE PROMOCION",
            "SEGUNDA LINEA DE PROMOCION",
            "RECORDATORIOS",
            "ENTRY MARKET"
            ]

        info_extraida = self.resumen.extraer_informacion()

        self.assertEqual(info_extraida["indices"], indices_esperados)

    def test_extraer_informacion_devuelve_columnas_productos(self):
        columnas_esperadas = ["Linea", "Marca", "Mercado", "MAT", "TRIM"]

        info_extraida = self.resumen.extraer_informacion()

        self.assertEqual(info_extraida["columnas_productos"][1], columnas_esperadas)


if __name__ == '__main__':
    unittest.main()
