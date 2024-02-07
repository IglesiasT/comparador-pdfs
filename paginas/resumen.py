from diferencias.distinta_cantidad_de_paginas import DistintaCantidadDePaginas
from diferencias.distinto_texto import DistintoTexto


class Resumen:
    def __init__(self, paginas: list):
        self.paginas = paginas
        self.diferencias = []

    def _extraer_indices(self) -> list:
        """
        {"indices": [
            PRODUCTOS DE LANZAMIENTO
            PRIMERA LINEA DE PROMOCION
            SEGUNDA LINEA DE PROMOCION
            RECORDATORIOS
            ENTRY MARKET
            ],
        "columnas_mercados": [Linea, Marca, Mercado, MAT, TRIM]
        }
        """
        texto_relevante = [
            "PRODUCTOS DE LANZAMIENTO",
            "PRIMERA LINEA DE PROMOCION",
            "SEGUNDA LINEA DE PROMOCION",
            "RECORDATORIOS",
            "ENTRY MARKET"
            ]

        pagina_indice = self.paginas[0]
        lineas = [linea.strip() for linea in pagina_indice.get_text().split('\n') if linea.strip()]

        return [texto for texto in lineas if texto in texto_relevante]

    def _comparar_cantidad_paginas(self, cantidad_paginas_otro_resumen: int):
        """
        Si esto es un template al cual se compara el output de los resumenes
        generados, tiene sentido que haya una cantidad de paginas establecida?
        """
        pass
        # if len(self.paginas) != cantidad_paginas_otro_resumen:
        #     self.diferencias.append(DistintaCantidadDePaginas(
        #     ))

    def _comparar_contenido_texto(self, pagina1, pagina2):
        """
        En algun lado debe decir Resumen
        Primer pagina resumen:
            PRODUCTOS DE LANZAMIENTO
            PRIMERA LINEA DE PROMOCION
            SEGUNDA LINEA DE PROMOCION
            RECORDATORIOS
            ENTRY MARKET
        """
        assert pagina1.number == pagina2.number

        if pagina1.get_text() != pagina2.get_text():
            self.diferencias.append(DistintoTexto(pagina1.number))

    def obtener_diferencias(self, otro_resumen):
        # TODO refactor

        self._comparar_cantidad_paginas(len(otro_resumen.paginas))
        #self._comparar_pagina_indices(otro_resumen.paginas[0])
        # Notar que la ejecucion sigue aunque haya distinta cantidad de paginas
        for pagina1, pagina2 in zip(self.paginas, otro_resumen.paginas):
            # self._comparar_paginas(pagina1, pagina2)
            self._comparar_contenido_texto(pagina1, pagina2)

        for diferencia in self.diferencias:
            diferencia.mostrar()
