from Services.service import PiesaError


class Console:
    def __init__(self,srv):
        self.__srv=srv

    def run(self):
        while True:
            print("\n 1. Add peisa | 2. Modify piesa | 3. Random generator | 4. Export file | 0. Exit")

            opt = input("Alege optiunea: ")

            try:
                if opt == "0":
                    break
                elif opt == "1":
                    titlu = input("Titlu: ")
                    regizor = input("Regizor: ")
                    gen = input("Gen: ")
                    durata = int(input("Durata: "))
                    self.__srv.add_piesa(titlu, regizor, gen, durata)
                    print("S-a adaugat piesa")
                elif opt=="2":
                    titlu = input("Titlu: ")
                    regizor = input("Regizor: ")
                    gen = input("Gen: ")
                    durata = int(input("Durata: "))
                    self.__srv.modify_piesa(titlu, regizor, gen, durata)
                    print("S-a modificat piesa")
                elif opt=="3":
                    n = int(input("Numarul de piese generate random: "))
                    self.__srv.add_random(n)
                    print("S-a randomizat n piese")
                elif opt=="4":
                    filename = input("Filename unde vrem sa exportam: ")
                    self.__srv.export_file(filename)
                else:
                    print("Optiune invalida")

            except PiesaError as e:
                print(f"\n[ERROR] {e}")
            except ValueError:
                print("\n[ERROR] Data introdusa nu este un numar")
