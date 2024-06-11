from tipos_paginas.tipo_de_pagina import TipoDePagina

class HojaLineaMercadoSuperior(TipoDePagina):
    def __init__(self, pagina):
        super().__init__(pagina)
        self._nombre = 'Hoja de Linea de Mercado Superior'


    def _extraer_indices(self) -> list:
        indices = [
            "PRODUCTOS DE LANZAMIENTO",
            "PRIMERA LINEA DE PROMOCION",
            "SEGUNDA LINEA DE PROMOCION",
            "RECORDATORIOS",
            "ENTRY MARKET"
        ]

        lineas = [linea.strip() for linea in self._pagina.get_text().split('\n') if linea.strip()]

        return [texto for texto in lineas if texto in indices]
    

    def obtener_diferencias(self, otra_hoja) -> list:
        pass
    