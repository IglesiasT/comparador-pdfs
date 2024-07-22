from tipos_paginas.tipo_de_pagina import TipoDePagina


class HojaTargeting(TipoDePagina):
    def __init__(self, pagina):
        super().__init__(pagina)
        self._nombre = 'Hoja Targeting'

    def obtener_diferencias(self, otra_hoja_targeting) -> list:
        pass
