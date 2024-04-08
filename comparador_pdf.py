import os
import fitz  # PyMuPDF

from diferencias.distinta_cantidad_de_paginas import DistintaCantidadDePaginas
from diferencias.distinto_texto import DistintoTexto


class ComparadorPDF:
    def __init__(self, input1, input2):
        self._input1 = str(input1)
        self._input2 = str(input2)

    def _matchear_pdfs(self) -> list:
        """
        Retorna una lista con los nombres de los archivos que si tienen par
        Es recíproco que un archivo tenga par y sea analizable
        """

        archivos_con_pares = []

        for archivo in os.listdir(self._input1):
            if archivo not in os.listdir(self._input2):
                print('No se encontró el par del archivo ' + archivo)
            else:
                archivos_con_pares.append(archivo)

        return archivos_con_pares

    def obtener_diferencias(self, pdf1: fitz.Document, pdf2: fitz.Document) -> list:
        """
        Se toma como supuesto que los archivos ya vienen abiertos
        """
        
        paginas_con_diferencias = []

        if pdf1.page_count != pdf2.page_count:
            return [DistintaCantidadDePaginas(pdf1.page_count, pdf2.page_count)]

        for numero_pagina in range(pdf1.page_count):    # Sabiendo que ambos tienen misma cantidad de páginas
            pagina_pdf1 = pdf1.load_page(numero_pagina)
            pagina_pdf2 = pdf2.load_page(numero_pagina)

            if pagina_pdf1.get_text() != pagina_pdf2.get_text():
                paginas_con_diferencias.append(DistintoTexto(numero_pagina + 1))

        return paginas_con_diferencias

    def obtener_archivos_con_diferencias(self) -> dict:
        """
        Devuelve un diccionario con los nombres de los archivos que tienen diferencias
        y una lista con las diferencias encontradas
        """

        archivos_a_comparar = self._matchear_pdfs()
        archivos_con_diferencias = {}

        for archivo in archivos_a_comparar:
            pdf1 = fitz.open(os.path.join(self._input1, archivo))
            pdf2 = fitz.open(os.path.join(self._input2, archivo))

            archivos_con_diferencias[archivo] = self.obtener_diferencias(pdf1, pdf2)

            pdf1.close()
            pdf2.close()

        return archivos_con_diferencias
