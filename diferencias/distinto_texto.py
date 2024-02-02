from diferencias.diferencia import Diferencia


class DistintoTexto(Diferencia):
    def __init__(self, numero_pagina_con_diferencia: int):
        self._numero_pagina = numero_pagina_con_diferencia

    def mostrar_diferencia(self):
        print(f'El texto de los archivos difiere en la pagina numero {self._numero_pagina}')
