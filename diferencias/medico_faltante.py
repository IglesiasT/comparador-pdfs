from diferencias.diferencia import Diferencia


class MedicoFaltante(Diferencia):
    def __init__(self, nombre_medico):
        self._nombre_medico = nombre_medico

    def mostrar(self):
        print(f'Medico faltante: {self._nombre_medico}')
