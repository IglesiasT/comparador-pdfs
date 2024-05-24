from abc import ABC, abstractmethod


class TipoDePagina(ABC):
    def __init__(self):
        self._nombre = 'Sin nombre'

    @abstractmethod
    def obtener_diferencias(self, otra_pagina : 'TipoDePagina') -> list:
        pass
