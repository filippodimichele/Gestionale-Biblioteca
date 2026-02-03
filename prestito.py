from datetime import datetime


class Prestito:

    def __init__(self, libro, utente):
        self.libro = libro
        self.utente = utente
        self.data_prestito = datetime.now()
        self.data_restituzione = None

    def __repr__(self):
        data_p = self.data_prestito.strftime("%d/%m/%Y %H:%M")
        data_r = self.data_restituzione.strftime("%d/%m/%Y %H:%M") if self.data_restituzione else "In corso"
        return f"Prestito(libro='{self.libro.titolo}', utente='{self.utente.nome}', dal={data_p}, al={data_r})"

    def __eq__(self, other):
        if not isinstance(other, Prestito):
            return False
        return (self.libro == other.libro and
                self.utente == other.utente and
                self.data_prestito == other.data_prestito)

    def concludi(self):
        self.data_restituzione = datetime.now()

    def is_attivo(self):
        return self.data_restituzione is None