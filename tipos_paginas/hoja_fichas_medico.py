from tipos_paginas.tipo_de_pagina import TipoDePagina
from diferencias.sin_diferencias import SinDiferencias


class HojaFichasMedico(TipoDePagina):
    def __init__(self, pagina):
        super().__init__(pagina)
        self._nombre = 'Hoja Fichas Medico'

    def obtener_diferencias(self, otra_hoja) -> list:
        return [SinDiferencias()]
