import random

class EmisiuneError(Exception):
    """Clasă personalizată pentru erorile aplicației"""
    pass


class EmisiuneService:
    def __init__(self, repo):
        self.__repo = repo
        self.__tipuri_blocate = []

    def blocheaza_tipuri(self, lista_tipuri):
        self.__tipuri_blocate = [t.strip() for t in lista_tipuri.split(",") if t.strip()]

    def sterge_emisiune(self, nume, tip):
        if tip in self.__tipuri_blocate:
            raise EmisiuneError("emisiune blocată")

        if not self.__repo.sterge(nume, tip):
            raise EmisiuneError("Avertisment: Emisiunea nu există!")

        self.__repo.save_to_file()

    def actualizeaza_emisiune(self, nume, tip, durata, descriere):
        if tip in self.__tipuri_blocate:
            raise EmisiuneError("Emisiune blocată")

        gasit = False
        for e in self.__repo.get_all():
            if e.nume == nume and e.tip == tip:
                e.durata = durata
                e.descriere = descriere
                gasit = True
                break

        if not gasit:
            raise EmisiuneError("Emisiunea nu există!")

        self.__repo.save_to_file()

    def genereaza_program(self, ora_s, ora_f):
        # Filtrăm emisiunile care au tipul în lista blocată
        disponibile = [e for e in self.__repo.get_all() if e.tip not in self.__tipuri_blocate]
        if not disponibile:
            return []

        program = []
        ora_c = ora_s
        folosite = set()

        while ora_c < ora_f:
            e = random.choice(disponibile)
            desc = e.descriere

            if e.nume in folosite:
                desc += " ****"

            # Calculăm durata astfel încât să nu depășim ora de sfârșit
            durata_emisiune = e.durata
            if ora_c + durata_emisiune > ora_f:
                durata_emisiune = ora_f - ora_c

            program.append({
                "ora": ora_c,
                "nume": e.nume,
                "tip": e.tip,
                "desc": desc
            })

            folosite.add(e.nume)
            ora_c += durata_emisiune

        return program