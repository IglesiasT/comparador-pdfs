from .diferencia import Diferencia

class VariacionMAT(Diferencia):
    def __init__(self, mat_anterior, mat_nuevo):
        self.mat_anterior = mat_anterior
        self.mat_nuevo = mat_nuevo

    def mostrar(self):
        porcentaje_variacion = (self.mat_nuevo - self.mat_anterior) / self.mat_anterior * 100
        print(f'Variacion de MAT: {porcentaje_variacion:.2f}%')
