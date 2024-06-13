from diferencias.sin_diferencias import SinDiferencias
from tipos_paginas.tipo_de_pagina import TipoDePagina


class HojaD(TipoDePagina):
    def __init__(self, pagina):
        super().__init__(pagina)
        self._nombre = 'Hoja D'

    def obtener_diferencias(self, otra_hoja) -> list:
        diferencias = [SinDiferencias()]

        return diferencias
