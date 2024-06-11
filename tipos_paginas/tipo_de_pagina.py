from abc import ABC, abstractmethod


class TipoDePagina(ABC):
    def __init__(self, pagina):
        self._nombre = 'Sin nombre'
        self.pagina = pagina

    @abstractmethod
    def obtener_diferencias(self, otra_pagina : 'TipoDePagina') -> list:
        pass
