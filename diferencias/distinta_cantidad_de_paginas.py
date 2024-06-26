from diferencias.diferencia import Diferencia


class DistintaCantidadDePaginas(Diferencia):
    def __init__(self, cantidad_paginas_1, cantidad_paginas_2):
        assert cantidad_paginas_1 != cantidad_paginas_2

        self._cantidad_paginas_1 = cantidad_paginas_1
        self._cantidad_paginas_2 = cantidad_paginas_2

    def mostrar(self):
        print(f'Cantidad de paginas en input 1: {self._cantidad_paginas_1}\n'
              f'Cantidad de paginas en input 2: {self._cantidad_paginas_2}')
