import unittest

from main import son_iguales

class TestComparadorPDFs(unittest.TestCase):
    """
    Proximo refactor: mockear la dependencia de los PDFs
    """
    
    def test_detecta_dos_pdf_iguales(self):
        file1 = 'liviano.PDF'
        file2 = 'liviano (copy).PDF'
        self.assertTrue(son_iguales(file1, file2))

    def test_detecta_dos_pdf_distintos(self):
        file1 = 'liviano.PDF'
        file2 = 'pesado.PDF'
        self.assertFalse(son_iguales(file1, file2))

    def test_detecta_pagina_donde_hay_diferencia(self):
        file1 = 'liviano.PDF'
        file2 = 'pesado.PDF'
        self.assertEqual(son_iguales(file1, file2), 3)

if __name__ == '__main__':
    unittest.main()
