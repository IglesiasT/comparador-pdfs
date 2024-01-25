import unittest

from main import son_iguales, obtener_paginas_donde_hay_diferencias


class TestComparadorPDFs(unittest.TestCase):
    """
    Proximo refactor: mockear la dependencia de los PDF
    """

    def test_detecta_dos_pdf_iguales(self):
        file1 = 'liviano.PDF'
        file2 = 'liviano (copy).PDF'
        self.assertTrue(son_iguales(file1, file2))

    def test_detecta_dos_pdf_distintos(self):
        file1 = 'liviano.PDF'
        file2 = 'pesado.PDF'
        self.assertFalse(son_iguales(file1, file2))

    def test_detecta_paginas_donde_hay_diferencias_en_pdf_distintos(self):
        file1 = 'liviano.PDF'
        file2 = 'pesado.PDF'
        esperado = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    11, 12, 13, 14, 15, 16, 17, 18, 19,
                    20, 21, 22, 23, 24, 25, 26, 27, 28,
                    29, 30, 31, 32, 33, 34, 35, 36, 37,
                    38, 39, 40, 41, 42, 43, 44, 45, 46,
                    47, 48, 49, 50]

        diferencia = obtener_paginas_donde_hay_diferencias(file1, file2)

        self.assertEqual(diferencia, esperado)

    def test_no_hay_paginas_distintas_en_pdf_iguales(self):
        file1 = 'liviano.PDF'
        file2 = 'liviano (copy).PDF'
        esperado = []

        diferencia = obtener_paginas_donde_hay_diferencias(file1, file2)

        self.assertEqual(diferencia, esperado)


if __name__ == '__main__':
    unittest.main()
