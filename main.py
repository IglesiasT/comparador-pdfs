from comparador_pdf import ComparadorPDF


def main():
    directorio_inputs_anteriores = 'static/anteriores'
    directorio_inputs_nuevos = 'static/nuevos'

    comparador = ComparadorPDF(directorio_inputs_anteriores, directorio_inputs_nuevos)
    archivos_con_diferencias = comparador.obtener_archivos_con_diferencias()

    for archivo, diferencias in archivos_con_diferencias.items():
        print(f'Se encontraron las siguientes diferencias en {archivo}:')
        for diferencia in diferencias:
            diferencia.mostrar()


if __name__ == '__main__':
    main()
