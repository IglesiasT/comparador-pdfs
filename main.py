from comparador_pdf import ComparadorPDF


def main():
    # ruta proceso que genera los pdf: m2.backend apps pdfengine2 infrep
    directorio_inputs = 'input1'
    directorio_inputs_ok = 'input2'

    comparador = ComparadorPDF(directorio_inputs, directorio_inputs_ok)
    archivos_con_diferencias = comparador.obtener_archivos_con_diferencias()

    for archivo, diferencias in archivos_con_diferencias.items():
        print(f'Se encontraron las siguientes diferencias en {archivo}:')
        for diferencia in diferencias:
            diferencia.mostrar_diferencia()


if __name__ == '__main__':
    main()
