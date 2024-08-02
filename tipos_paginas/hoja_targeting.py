from tipos_paginas.tipo_de_pagina import TipoDePagina
from diferencias.diferencia import Diferencia
from diferencias.medico_faltante import MedicoFaltante
from diferencias.sin_diferencias import SinDiferencias


class HojaTargeting(TipoDePagina):
    def __init__(self, pagina):
        super().__init__(pagina)
        self._nombre = 'Hoja Targeting'
        self.medicos = self._obtener_medicos()

    def _obtener_medicos(self) -> list[dict]:
        medicos = []
        texto = self.pagina.get_text()
        tablas_hoja: list[list[str]] = self.pagina.find_tables(strategy="lines_strict")[0].extract()
        start = 7 if 'Total' in texto else 5    # Vemos si tiene la tabla de letras totales o no

        for tabla in tablas_hoja[start:]:   # Cada string es una tabla del pdf
            if not tabla[0]:
                continue    # Salteamos las tablas vacías leídas por PyMuPDF

            filas = tabla[0].split('\n')
            for fila in filas:
                if fila.strip():    # Si la línea no está vacía
                    medico = {
                        'nombre': fila[:-3].strip(),
                        'especialidad': fila[-3:],
                        'fue_visitado': False,  # 'x14' en get_text es la tilde de que ya fue visitado
                        'fue_visitado_por_otro': True  # Si tiene R
                    }
                    medicos.append(medico)

        return medicos

    def obtener_diferencias(self, otra_hoja_targeting) -> list:
        if not isinstance(otra_hoja_targeting, type(self)):
            raise TypeError("Los tipos de página no coinciden")

        diferencias = []    # Comprar medicos, mercados, tildes y letras asignadas
        diferencias.extend(self._comparar_medicos(otra_hoja_targeting.medicos))
        if not diferencias:
            diferencias.append(SinDiferencias())

        return diferencias

    def _comparar_medicos(self, otros_medicos: list[dict]) -> list[Diferencia]:
        # TODO checkear que los medicos sean los mismos que los de hoja resumen
        diferencias = []

        nombres = [medico['nombre'] for medico in self.medicos]
        for medico in otros_medicos:
            if medico['nombre'] not in nombres:
                diferencias.append(MedicoFaltante(medico['nombre']))

        return diferencias
