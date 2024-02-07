import unittest
import fitz

from paginas.resumen import Resumen


class TestResumen(unittest.TestCase):
    """
    Siguiente refactor: mockear la dependencia de los PDF
    """
    pdf_prueba = fitz.open('input1/DISTRITO-MARCELO_SERGIO_SALLUCCI.PDF')

    def setUp(self):
        paginas_resumen = [pag for pag in self.pdf_prueba.pages(stop=5)]
        self.resumen = Resumen(paginas_resumen)

    def tearDown(self):
        # Cerramos el archivo luego de cada test independientemente de si falla o no
        if hasattr(self, 'pdf_prueba') and hasattr(self.pdf_prueba, 'close'):
            self.pdf_prueba.close()

    def test_extraer_indice_devuelve_indices_de_la_primer_pagina(self):
        indices_esperados = [
            "PRODUCTOS DE LANZAMIENTO",
            "PRIMERA LINEA DE PROMOCION",
            "SEGUNDA LINEA DE PROMOCION",
            "RECORDATORIOS",
            "ENTRY MARKET"
            ]

        self.assertEqual(self.resumen._extraer_indices(), indices_esperados)

    def test_extraer_columnas_productos_devuelve_headers_tablas(self):
        columnas_esperadas = ["Linea", "Marca", "Mercado", "MAT", "TRIM"]

        self.assertEqual(self.resumen._extraer_columnas_productos()[1], columnas_esperadas)


if __name__ == '__main__':
    unittest.main()
