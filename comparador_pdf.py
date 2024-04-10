import os
import fitz  # PyMuPDF

from diferencias.distinta_cantidad_de_paginas import DistintaCantidadDePaginas
from diferencias.distinto_texto import DistintoTexto
from tipos_hojas.resumen import Resumen


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
            diferencias = []

            if pdf1.page_count != pdf2.page_count:
                archivos_con_diferencias[archivo] = [DistintaCantidadDePaginas(pdf1.page_count, pdf2.page_count)]
                continue

            for numero_pagina in range(pdf1.page_count):    # Sabiendo que ambos tienen misma cantidad de páginas
                pagina_pdf1 = pdf1.load_page(numero_pagina)
                pagina_pdf2 = pdf2.load_page(numero_pagina)

                if pagina_pdf1.get_text() != pagina_pdf2.get_text():
                    diferencias.append(DistintoTexto(numero_pagina + 1))

            if diferencias:
                archivos_con_diferencias[archivo] = diferencias # Si hay diferencias, se agrega al diccionario
            
            # El comparador es quien conoce entre que rangos hay cada tipo de pagina
            resumen1 = Resumen(pdf1.pages(0,6))
            resumen2 = Resumen(pdf2.pages(0,6))

            pdf1.close()
            pdf2.close()

        return archivos_con_diferencias
