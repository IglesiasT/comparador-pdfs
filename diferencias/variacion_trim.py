from .diferencia import Diferencia

class VariacionTRIM(Diferencia):
    def __init__(self, trim_anterior, trim_nuevo):
        self.trim_anterior = trim_anterior
        self.trim_nuevo = trim_nuevo

    def mostrar(self):
        porcentaje_variacion = (self.trim_nuevo - self.trim_anterior) / self.trim_anterior * 100
        print(f'Variacion de TRIM: {porcentaje_variacion:.2f}%')
