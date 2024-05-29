from comparador_pdf import ComparadorPDF


def main():
    directorio_inputs = 'nuevos'
    directorio_inputs_ok = 'anteriores'

    comparador = ComparadorPDF(directorio_inputs_ok, directorio_inputs)
    archivos_con_diferencias = comparador.obtener_archivos_con_diferencias()

    for archivo, diferencias in archivos_con_diferencias.items():
        print(f'Se encontraron las siguientes diferencias en {archivo}:')
        for diferencia in diferencias:
            diferencia.mostrar()


if __name__ == '__main__':
    main()
