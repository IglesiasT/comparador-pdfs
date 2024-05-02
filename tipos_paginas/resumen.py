from diferencias.sin_diferencias import SinDiferencias
from tipos_paginas.tipo_de_pagina import TipoDePagina


class Resumen(TipoDePagina):
    def __init__(self, paginas: list):
        super().__init__()
        self._nombre = 'Resumen'
        self._paginas = paginas   # Se espera que sean una lista de objetos de tipo Page
        self._diferencias = []

    def _extraer_indices(self) -> list:
        indices = [
            "PRODUCTOS DE LANZAMIENTO",
            "PRIMERA LINEA DE PROMOCION",
            "SEGUNDA LINEA DE PROMOCION",
            "RECORDATORIOS",
            "ENTRY MARKET"
        ]

        pagina_indice = self._paginas[0]
        lineas = [linea.strip() for linea in pagina_indice.get_text().split('\n') if linea.strip()]

        return [texto for texto in lineas if texto in indices]

    @staticmethod
    def _formatear_tabla(texto_tabla: str) -> list:
        """
        TODO refactor para retornar lineas directamente y mat y trim para luego ser comparados en otro lado
        """

        tabla_formateada = []
        lineas = texto_tabla.split('\n')

        for linea in lineas:
            linea_formateada = linea.replace(' ≈', '')    # Limpiar caracteres raros
            linea_formateada = linea_formateada.replace(',', '.')  # Para parseo a float
            # Linea (investigar obtencion con regex)
            # Marca (pensar si se puede obtener por ser unica columna en bold)
            # Mercado
            mat = float(linea_formateada.split(' ')[-2])
            trim = float(linea_formateada.split(' ')[-1])

            tabla_formateada.append(["Linea", "Marca", "Mercado", mat, trim])

        return tabla_formateada

    def _extraer_columnas_productos(self) -> dict:
        columnas_productos = ["Linea", "Marca", "Mercado", "MAT", "TRIM"]
        columnas_productos_extraidas = {}
        paginas_mercados = self._paginas[1:]

        for pagina in paginas_mercados:
            header, tabla = pagina.find_tables(strategy="lines_strict")[1].extract()
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

    def obtener_diferencias(self, otro_resumen) -> list:
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

        diferencias = []

        # TODO refactor
        info_resumen = self.extraer_informacion()

        # self._comparar_cantidad_paginas(len(otro_resumen.paginas))
        # self._comparar_pagina_indices(otro_resumen.paginas[0])
        # Notar que la ejecucion sigue aunque haya distinta cantidad de paginas
        # for pagina1, pagina2 in zip(self.paginas, otro_resumen.paginas):pass
        # self._comparar_paginas(pagina1, pagina2)
        # self._comparar_contenido_texto(pagina1, pagina2)

        # Si luego de todas las comparaciones no hay diferencias, decimos que no tienen diferencias
        if not diferencias:
            diferencias.append(SinDiferencias())

        return diferencias
