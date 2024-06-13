from diferencias.sin_diferencias import SinDiferencias
from .tipo_de_pagina import TipoDePagina


class HojaEntidadesCompetencia(TipoDePagina):
    def __init__(self, pagina):
        super().__init__(pagina)
        self._nombre = 'Hoja entidades competencia'

    def obtener_diferencias(self, otra_hoja) -> list:
        diferencias = [SinDiferencias()]

        return diferencias
