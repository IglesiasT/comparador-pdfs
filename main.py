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
    return obtener_contenido_pdf(file1) == obtener_contenido_pdf(file2)


def obtener_paginas_donde_hay_diferencias(file1, file2) -> list:

    pdf1 = fitz.open(file1)
    pdf2 = fitz.open(file2)
    paginas_diferentes = []

    if pdf1.page_count != pdf2.page_count:
        print('no tienen la misma cantidad de paginas')  # Manejar esto, no deberia romperse

    for numero_pagina in range(pdf1.page_count):  # Pensar como evitar esta nueva iteracion
        pagina_pdf1 = pdf1.load_page(numero_pagina)
        pagina_pdf2 = pdf2.load_page(numero_pagina)

        if pagina_pdf1.get_text() != pagina_pdf2.get_text():
            paginas_diferentes.append(numero_pagina)

    pdf1.close()
    pdf2.close()

    return paginas_diferentes


def obtener_diferencias(file1, file2):
    # TODO: refactorizar para que reciba una lista de paths

    if son_iguales(file1, file2):
        return 'No hay diferencias'

    return obtener_paginas_donde_hay_diferencias(file1, file2)


def main():
    file1 = 'liviano.PDF'
    file2 = 'pesado.PDF'

    print(obtener_diferencias(file1, file2))


if __name__ == '__main__':
    main()
