import os

import fitz  # PyMuPDF


def obtener_contenido_pdf(path_pdf) -> str:
    archivo_pdf = fitz.open(path_pdf)
    texto = ''

    for numero_pagina in range(archivo_pdf.page_count):
        pagina = archivo_pdf.load_page(numero_pagina)
        texto += pagina.get_text()
    archivo_pdf.close()

    return texto


def son_iguales(file1, file2) -> bool:
    # Usar alguna estructura de datos para compararlos todos juntos?
    # Debe comparar los de informe con los de informe ok
    # Early return si la cantidad de hojas es desigual
    return obtener_contenido_pdf(file1) == obtener_contenido_pdf(file2)


def obtener_paginas_donde_hay_diferencias(file1, file2) -> list:

    pdf1 = fitz.open(file1)
    pdf2 = fitz.open(file2)
    paginas_diferentes = []

    if pdf1.page_count != pdf2.page_count:
        print('Los PDF tienen distinta cantidad de paginas')
        print('Paginas pdf1: ' + str(pdf1.page_count))
        print('Paginas pdf2: ' + str(pdf2.page_count))

    for numero_pagina in range(pdf1.page_count):  # Pensar como evitar esta nueva iteracion
        pagina_pdf1 = pdf1.load_page(numero_pagina)
        pagina_pdf2 = pdf2.load_page(numero_pagina)

        if pagina_pdf1.get_text() != pagina_pdf2.get_text():
            paginas_diferentes.append(numero_pagina)

    pdf1.close()
    pdf2.close()

    return paginas_diferentes


def obtener_diferencias(file1, file2):

    if son_iguales(file1, file2):
        return 'No hay diferencias'

    return obtener_paginas_donde_hay_diferencias(file1, file2)


def matchear_pdfs(input1, input2) -> list:
    """
    Retorna una lista con los nombres de los archivos que si tienen par
    """

    archivos_con_pares = []

    for archivo in os.listdir(input1):
        if archivo not in os.listdir(input2):
            print('No se encontró el par del archivo ' + archivo)
        else:
            archivos_con_pares.append(archivo)

    return archivos_con_pares


def main():
    # TODO: matchear archivos con mismo nombre para compararlos
    directorio_outputs = 'input1'
    directorio_outputs_ok = 'input2'
    pares_a_comparar = matchear_pdfs(directorio_outputs, directorio_outputs_ok)

    print(obtener_diferencias(pares_a_comparar))


if __name__ == '__main__':
    main()
