import os
import fitz  # PyMuPDF


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

    @staticmethod
    def obtener_contenido(pdf: fitz.Document) -> str:
        texto = ''

        for numero_pagina in range(pdf.page_count):
            pagina = pdf.load_page(numero_pagina)
            texto += pagina.get_text()

        return texto

    def _son_iguales(self, pdf1: fitz.Document, pdf2: fitz.Document) -> bool:
        return self.obtener_contenido(pdf1) == self.obtener_contenido(pdf2)

    @staticmethod
    def obtener_paginas_donde_hay_diferencias(pdf1: fitz.Document, pdf2: fitz.Document) -> list:
        # TODO devolver objeto no lista
        paginas_diferentes = []

        if pdf1.page_count != pdf2.page_count:
            print(f'\nLos PDF de {pdf1.name} tienen distinta cantidad de paginas')
            print('Paginas pdf1: ' + str(pdf1.page_count))
            print('Paginas pdf2: ' + str(pdf2.page_count))
            return paginas_diferentes  # TODO refactor

        for numero_pagina in range(pdf1.page_count):
            pagina_pdf1 = pdf1.load_page(numero_pagina)
            pagina_pdf2 = pdf2.load_page(numero_pagina)

            if pagina_pdf1.get_text() != pagina_pdf2.get_text():
                paginas_diferentes.append(numero_pagina)

        return paginas_diferentes

    def obtener_diferencias(self) -> dict:
        """
        Obtiene las diferencias de forma precisa de una lista de archivos pdf
        (ahora mismo solo retorna un diccionario donde las keys son archivos
        que tienen pares y los valores una lista de las páginas donde hay diferencias)
        """
        archivos_a_comparar = self._matchear_pdfs()
        paginas_con_diferencias = {}

        for archivo in archivos_a_comparar:
            pdf1 = fitz.open(os.path.join(self._input1, archivo))
            pdf2 = fitz.open(os.path.join(self._input2, archivo))

            if not self._son_iguales(pdf1, pdf2):
                paginas_con_diferencias[archivo] = self.obtener_paginas_donde_hay_diferencias(pdf1, pdf2)

            # Una vez hechos los checkeos se cierran los archivos en la misma iteracion
            pdf1.close()
            pdf2.close()

        return paginas_con_diferencias
