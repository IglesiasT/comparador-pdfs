from diferencias.distinta_cantidad_de_paginas import DistintaCantidadDePaginas
from diferencias.distinto_texto import DistintoTexto


class Resumen:
    def __init__(self, paginas: list):
        self.paginas = paginas
        self.diferencias = []

    def _extraer_indices(self) -> list:
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

    @staticmethod
    def _formatear_tabla(texto_tabla) -> list:
        tabla_formateada = []
        lineas = texto_tabla.split('\n')

        for linea in lineas:
            tabla_formateada.append(linea)

        return tabla_formateada

    def _extraer_columnas_productos(self) -> dict:
        columnas_productos = ["Linea", "Marca", "Mercado", "MAT", "TRIM"]
        columnas_productos_extraidas = {}
        paginas_mercados = self.paginas[1:]

        for pagina in paginas_mercados:
            header, tabla = pagina.find_tables(strategy="lines_strict").tables[1].extract()
            tabla = self._formatear_tabla(tabla[0])    # Se acomoda a matriz con lista de listas
            print(tabla)

            lineas = [linea.strip() for linea in pagina.get_text().split('\n') if linea.strip()]
            columnas_productos_extraidas[pagina.number] = [texto for texto in lineas if texto in columnas_productos]

        return columnas_productos_extraidas

    def extraer_informacion(self) -> dict:
        """
        Retorna un diccionario con los datos relevantes a extraer de la seccion Resumen
        """

        return {
            "indices": self._extraer_indices(),
            "columnas_productos": self._extraer_columnas_productos()
        }

    def obtener_diferencias(self, otro_resumen):
        """
        ej de output esperado para luego comparar
        la idea es obtener primero el contenido y que luego por fuera se compare (renombrar funcion)
        {"indices": [
            PRODUCTOS DE LANZAMIENTO
            PRIMERA LINEA DE PROMOCION
            SEGUNDA LINEA DE PROMOCION
            RECORDATORIOS
            ENTRY MARKET
            ],
        "columnas_productos": [Linea, Marca, Mercado, MAT, TRIM]
        }
        """
        # TODO refactor
        info_resumen = self.extraer_informacion()

        # self._comparar_cantidad_paginas(len(otro_resumen.paginas))
        # self._comparar_pagina_indices(otro_resumen.paginas[0])
        # Notar que la ejecucion sigue aunque haya distinta cantidad de paginas
        # for pagina1, pagina2 in zip(self.paginas, otro_resumen.paginas):pass
        # self._comparar_paginas(pagina1, pagina2)
        # self._comparar_contenido_texto(pagina1, pagina2)

        for diferencia in self.diferencias:
            diferencia.mostrar()
