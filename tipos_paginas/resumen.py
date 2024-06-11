from diferencias.sin_diferencias import SinDiferencias
from diferencias.variacion_mat import VariacionMAT
from diferencias.variacion_trim import VariacionTRIM
from tipos_paginas.tipo_de_pagina import TipoDePagina


class Resumen(TipoDePagina):
    def __init__(self, pagina):
        super().__init__(pagina)
        self._nombre = 'Resumen'


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

            tabla_formateada.append(["Linea", "Marca", "Mercado", mat, trim])   # Harcodeado, reemplazar por linea, marca y mercado reales de cada fila

        return tabla_formateada
    

    def _comparar_columnas_productos(self, otro_resumen) -> list:
        """
        """

        diferencias = []
        header, tabla = self.pagina.find_tables(strategy="lines_strict")[1].extract()
        otro_header, otra_tabla = otro_resumen.pagina.find_tables(strategy="lines_strict")[1].extract()
        tabla = self._formatear_tabla(tabla[0])
        otra_tabla = self._formatear_tabla(otra_tabla[0])

        # Comparamos los headers de las tablas TODO refactor agregar diferencia si no coinciden
        assert header[0].split() == otro_header[0].split() == ['Linea', 'Marca', 'Mercado', 'MAT', 'TRIM']

        # Comparamos variacion de MAT y TRIM
        limite_variacion = 0.05
        for i in range(len(tabla)):
            mat = tabla[i][3]
            otro_mat = otra_tabla[i][3]
            trim = tabla[i][4]
            otro_trim = otra_tabla[i][4]

            if abs(mat - otro_mat) > limite_variacion:
                print(f"Variacion de MAT en fila {i} es mayor a {limite_variacion}")
                diferencias.append(VariacionMAT(mat, otro_mat))
            if abs(trim - otro_trim) > limite_variacion:
                print(f"Variacion de TRIM en fila {i} es mayor a {limite_variacion}")
                diferencias.append(VariacionTRIM(trim, otro_trim))
        
        return diferencias
    

    def obtener_diferencias(self, otro_resumen) -> list:
        """
        """

        if not isinstance(otro_resumen, type(self)):    # TODO mover a la clase madre
            raise TypeError("Los tipos de página no coinciden")

        diferencias = []
        diferencias.extend(self._comparar_columnas_productos(otro_resumen))

        # Si luego de todas las comparaciones no hay diferencias, decimos que no tienen diferencias
        if not diferencias:
            diferencias.append(SinDiferencias())

        return diferencias
