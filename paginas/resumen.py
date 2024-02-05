from fitz import Page


class Resumen(Page):
    def __eq__(self, other):
        return self.get_text() == other.get_text()
