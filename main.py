from comparador_pdf import ComparadorPDF


def main():
    directorio_inputs = 'input1'
    directorio_inputs_ok = 'input2'

    comparador = ComparadorPDF(directorio_inputs, directorio_inputs_ok)
    print(comparador.obtener_diferencias())


if __name__ == '__main__':
    main()
