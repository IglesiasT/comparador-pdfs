import os
import fitz  # PyMuPDF

from diferencias.distinta_cantidad_de_paginas import DistintaCantidadDePaginas
from diferencias.distinto_texto import DistintoTexto
from tipos_paginas.hoja_d import HojaD
from tipos_paginas.hoja_entidades_competencia import HojaEntidadesCompetencia
from tipos_paginas.hoja_heart import HojaHeart
from tipos_paginas.hoja_linea_mercado_superior import HojaLineaMercadoSuperior
from tipos_paginas.resumen import Resumen
from tipos_paginas.tipo_de_pagina import TipoDePagina


class ComparadorPDF:
    def __init__(self, input1, input2):
        self._input1 = str(input1)
        self._input2 = str(input2)
        self._mapeo_ids_paginas = {
            "hoja_linea_mercado_superior": HojaLineaMercadoSuperior,
            "hoja_resumen": Resumen,
            "hoja_heart": HojaHeart,
            "hoja_d": HojaD,
            "hoja_entidades_competencia": HojaEntidadesCompetencia,
        }

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

    def _obtener_tipo_de_pagina(self, pagina_pdf) -> TipoDePagina:
        """
        Recibe una pagina y devuelve su tipo para que pueda ser comparada
        """

        id_pagina = pagina_pdf.get_text().split('id:')[1].strip()
        id_pagina = id_pagina.replace(' ', '_')  # Para que sea compatible con las keys de las clases
        tipo_pagina = self._mapeo_ids_paginas[id_pagina]

        return tipo_pagina(pagina_pdf)

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
            archivos_con_diferencias[archivo] = []

            # Diferencias generales de los pdfs
            if pdf1.page_count != pdf2.page_count:
                archivos_con_diferencias[archivo].append(DistintaCantidadDePaginas(pdf1.page_count, pdf2.page_count))
                continue

            for i in range(10):  # Sabiendo que ambos tienen misma cantidad de páginas TODO cambiar range a pdf1.page_count
                pagina_pdf1 = pdf1.load_page(i)
                pagina_pdf2 = pdf2.load_page(i)

                # Identificamos cada tipo de página y obtenemos sus diferencias particulares
                tipo_de_pagina_pdf1 = self._obtener_tipo_de_pagina(pagina_pdf1)
                tipo_de_pagina_pdf2 = self._obtener_tipo_de_pagina(pagina_pdf2)

                # Delegamos la comparación en el tipo de pagina
                archivos_con_diferencias[archivo] += tipo_de_pagina_pdf1.obtener_diferencias(tipo_de_pagina_pdf2)

            pdf1.close()
            pdf2.close()

        return archivos_con_diferencias
