from comparador_pdf import ComparadorPDF
from salida import Salida


def main():
    directorio_inputs_anteriores = 'static/anteriores'
    directorio_inputs_nuevos = 'static/nuevos'
    directorio_salida = 'static/salida.xlsx'

    comparador = ComparadorPDF(directorio_inputs_anteriores, directorio_inputs_nuevos)
    archivos_con_diferencias = comparador.obtener_archivos_con_diferencias()
    salida = Salida(archivos_con_diferencias, directorio_salida)

    salida.generar_salida()


if __name__ == '__main__':
    main()
