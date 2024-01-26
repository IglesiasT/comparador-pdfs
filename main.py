import os

import fitz  # PyMuPDF


def obtener_contenido(pdf: fitz.Document) -> str:
    texto = ''

    for numero_pagina in range(pdf.page_count):
        pagina = pdf.load_page(numero_pagina)
        texto += pagina.get_text()

    return texto


def son_iguales(pdf1: fitz.Document, pdf2: fitz.Document) -> bool:
    return obtener_contenido(pdf1) == obtener_contenido(pdf2)


def obtener_paginas_donde_hay_diferencias(pdf1: fitz.Document, pdf2: fitz.Document) -> list:
    paginas_diferentes = []

    if pdf1.page_count != pdf2.page_count:
        print(f'Los PDF de {pdf1.name} tienen distinta cantidad de paginas')
        print('Paginas pdf1: ' + str(pdf1.page_count))
        print('Paginas pdf2: ' + str(pdf2.page_count))
        return paginas_diferentes  # TODO refactor

    for numero_pagina in range(pdf1.page_count):
        pagina_pdf1 = pdf1.load_page(numero_pagina)
        pagina_pdf2 = pdf2.load_page(numero_pagina)

        if pagina_pdf1.get_text() != pagina_pdf2.get_text():
            paginas_diferentes.append(numero_pagina)

    return paginas_diferentes


def obtener_diferencias(archivos_a_comparar: list, input1, input2) -> dict:
    """
    Obtiene los diferencias de forma precisa de una lista de archivos pdf
    (ahora mismo solo retorna un diccionario donde las keys son archivos
    que tienen pares y los valores una lista de las páginas donde hay diferencias)
    """
    paginas_con_diferencias = {}

    for archivo in archivos_a_comparar:
        pdf1 = fitz.open(os.path.join(input1, archivo))
        pdf2 = fitz.open(os.path.join(input2, archivo))

        if not son_iguales(pdf1, pdf2):
            paginas_con_diferencias[archivo] = obtener_paginas_donde_hay_diferencias(pdf1, pdf2)

        # Una vez hechos los checkeos se cierran los archivos en la misma iteracion
        pdf1.close()
        pdf2.close()

    # Teniendo los archivos y las páginas donde hay diferencias
    # buscar_diferencias_por_pagina(paginas_con_diferencias)

    return paginas_con_diferencias


def matchear_pdfs(input1, input2) -> list:
    """
    Retorna una lista con los nombres de los archivos que si tienen par
    Es recíproco que un archivo tenga par y sea analizable
    """

    archivos_con_pares = []

    for archivo in os.listdir(input1):
        if archivo not in os.listdir(input2):
            print('No se encontró el par del archivo ' + archivo)
        else:
            archivos_con_pares.append(archivo)

    return archivos_con_pares


def main():
    directorio_inputs = 'input1'
    directorio_inputs_ok = 'input2'

    pares_a_comparar = matchear_pdfs(directorio_inputs, directorio_inputs_ok)

    # Actualmente muestra un diccionario con todos los pdf, pensar como mejorar eso
    print(obtener_diferencias(pares_a_comparar, directorio_inputs, directorio_inputs_ok))


if __name__ == '__main__':
    main()
