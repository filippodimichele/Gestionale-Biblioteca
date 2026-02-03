class Utente:

    MAX_PRESTITI = 3

    def __init__(self, nome, numero_tessera):
        self.nome = nome
        self.numero_tessera = numero_tessera
        self.prestiti = []

    def __repr__(self):
        return f"Utente(nome='{self.nome}', tessera='{self.numero_tessera}', prestiti_attivi={len(self.prestiti)})"

    def __eq__(self, other):
        if not isinstance(other, Utente):
            return False
        return self.numero_tessera == other.numero_tessera

    def puo_prendere_in_prestito(self):
        return len(self.prestiti) < self.MAX_PRESTITI

    def aggiungi_prestito(self, prestito):
        self.prestiti.append(prestito)

    def rimuovi_prestito(self, prestito):
        if prestito in self.prestiti:
            self.prestiti.remove(prestito)