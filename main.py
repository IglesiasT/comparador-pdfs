import fitz # PyMuPDF

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

def obtener_pagina_donde_hay_diferencia(file1, file2):
    # Retornar una sola y que la iteracion se haga afuera o que retorne una lista?
    pass

def obtener_diferencias(file1, file2):
    # TODO: refactorizar para que reciba una lista de paths
    
    if not son_iguales(file1, file2):
        print(obtener_pagina_donde_hay_diferencia(file1, file2))
    else:
        print('No hay diferencias')

def main():
    file1 = 'liviano.PDF'
    file2 = 'pesado.PDF'

    print(obtener_diferencias(file1, file2))

if __name__ == '__main__':
    main()
