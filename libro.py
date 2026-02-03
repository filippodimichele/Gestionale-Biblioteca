class Libro:

    def __init__(self, titolo, isbn, autore):
        self.titolo = titolo
        self.isbn = isbn
        self.autore = autore
        self.disponibile = True

    def __repr__(self):
        stato = "Disponibile" if self.disponibile else "In prestito"
        return f"Libro(titolo='{self.titolo}', isbn='{self.isbn}', stato='{stato}')"

    def __eq__(self, other):
        if not isinstance(other, Libro):
            return False
        return self.isbn == other.isbn

    def presta(self):
        if self.disponibile:
            self.disponibile = False
            return True
        return False

    def restituisci(self):
        self.disponibile = True