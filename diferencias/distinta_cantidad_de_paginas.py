class DistintaCantidadDePaginas:
    def __init__(self, cantidad_paginas_1, cantidad_paginas_2):
        assert cantidad_paginas_1 != cantidad_paginas_2

        self._cantidad_paginas_1 = cantidad_paginas_1
        self._cantidad_paginas_2 = cantidad_paginas_2

    def mostrar_diferencia(self):
        return f'Cantidad de paginas en input 1: {self._cantidad_paginas_1}\nCantidad de paginas en input 2: {self._cantidad_paginas_2}'
