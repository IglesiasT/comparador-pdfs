from diferencias.sin_diferencias import SinDiferencias
from diferencias.variacion_mat import VariacionMAT
from diferencias.variacion_trim import VariacionTRIM
from tipos_paginas.tipo_de_pagina import TipoDePagina


class Resumen(TipoDePagina):
    def __init__(self, pagina):
        super().__init__(pagina)
        self._nombre = 'Resumen'

    @staticmethod
    def _formatear_tabla(tabla) -> list:
        """
        En caso de que queramos comparar linea marca y mercado, probar identificarlos como
        el anterior y el posterior al texto en bold (marca)
        """

        tabla_formateada = []
        lineas_tabla = tabla[0].split('\n')

        for linea_tabla in lineas_tabla:
            linea_formateada = linea_tabla.replace(' ≈', '')  # Limpiar caracteres raros
            linea_formateada = linea_formateada.replace(',', '.')  # Para parseo a float
            linea = ''  # investigar obtencion con regex)
            marca = ''  # pensar si se puede obtener por ser unica columna en bold
            mercado = ''
            mat = float(linea_formateada.split(' ')[-2])
            trim = float(linea_formateada.split(' ')[-1])

            tabla_formateada.append([linea, marca, mercado, mat, trim])

        return tabla_formateada

    def _comparar_columnas_productos(self, otro_resumen) -> list:
        """
        """

        diferencias = []
        header, tabla = self.pagina.find_tables(strategy="lines_strict")[1].extract()
        otro_header, otra_tabla = otro_resumen.pagina.find_tables(strategy="lines_strict")[1].extract()
        tabla = self._formatear_tabla(tabla)
        otra_tabla = self._formatear_tabla(otra_tabla)

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

        if not isinstance(otro_resumen, type(self)):  # TODO mover a la clase madre
            raise TypeError("Los tipos de página no coinciden")

        diferencias = []
        diferencias.extend(self._comparar_columnas_productos(otro_resumen))

        # Si luego de todas las comparaciones no hay diferencias, decimos que no tienen diferencias
        if not diferencias:
            diferencias.append(SinDiferencias())

        return diferencias
