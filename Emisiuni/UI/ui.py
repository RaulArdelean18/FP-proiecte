from Services.service import EmisiuneError


class Console:
    def __init__(self, srv):
        self.__srv = srv

    def __afiseaza_tabel(self, program):
        """Afișează programul în format tabelar"""
        print(f"\n{'Ora':<5} | {'Nume':<15} | {'Tip':<12} | {'Descriere'}")
        print("-" * 60)
        for p in program:
            print(f"{p['ora']:<5} | {p['nume']:<15} | {p['tip']:<12} | {p['desc']}")

    def run(self):
        while True:
            print("\n1. Sterge | 2. Actualizeaza | 3. Program | 4. Blocheaza | 0. Exit")
            opt = input("Alege opțiunea: ")

            try:
                if opt == "0":
                    break
                elif opt == "1":
                    n = input("Nume emisiune: ")
                    t = input("Tip emisiune: ")
                    self.__srv.sterge_emisiune(n, t)
                    print("Operațiune reușită!")
                elif opt == "2":
                    n = input("Nume: ")
                    t = input("Tip: ")
                    d = int(input("Durata nouă (ore): "))
                    desc = input("Descriere nouă: ")
                    self.__srv.actualizeaza_emisiune(n, t, d, desc)
                    print("Operațiune reușită!")
                elif opt == "3":
                    s = int(input("Ora început: "))
                    f = int(input("Ora sfârșit: "))
                    prog = self.__srv.genereaza_program(s, f)
                    self.__afiseaza_tabel(prog)
                elif opt == "4":
                    tipuri = input("Introduceți tipurile de blocat (ex: Stiri, Film) sau vid: ")
                    self.__srv.blocheaza_tipuri(tipuri)
                    print("Lista de blocare actualizată.")
                else:
                    print("Opțiune invalidă!")

            except EmisiuneError as ee:
                print(f"\n[EROARE] {ee}")
            except ValueError:
                print("\n[EROARE] Te rog introdu date numerice valide pentru oră/durată!")