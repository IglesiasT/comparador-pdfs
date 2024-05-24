from tipos_paginas.tipo_de_pagina import TipoDePagina

class HojaLineaMercadoSuperior(TipoDePagina):
    def __init__(self):
        super().__init__()
        self._nombre = 'Hoja de Linea de Mercado Superior'


    def obtener_diferencias(self, otra_pagina: 'HojaLineaMercadoSuperior') -> list:
        pass
    