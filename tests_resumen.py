import os
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

    def test_extraer_indice_devuelve_indices_de_la_primer_pagina(self):
        indices_esperados = [
            "PRODUCTOS DE LANZAMIENTO",
            "PRIMERA LINEA DE PROMOCION",
            "SEGUNDA LINEA DE PROMOCION",
            "RECORDATORIOS",
            "ENTRY MARKET"
            ]

        self.assertEqual(self.resumen._extraer_indices(), indices_esperados)
        self.pdf_prueba.close()


if __name__ == '__main__':
    unittest.main()
