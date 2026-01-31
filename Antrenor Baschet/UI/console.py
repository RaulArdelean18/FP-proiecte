class Console:
    def __init__(self,service):
        self.__service = service

    def __add_player(self):
        nume = input("Introduceti numele jucatorului: ")
        prenume = input("Introduceti prenumele jucatorului: ")
        inaltime = int(input("Introduceti inaltime jucatorului: "))
        post = input("Introduceti postul jucatorului: ")

        self.__service.add_player(nume,prenume,inaltime,post)
        print("S-a adaugat cu succes jucatorul in echipa")

    def __modify_inaltime(self):
        nume = input("Introduceti numele jucatorului: ")
        prenume = input("Introduceti prenumele jucatorului: ")
        inaltime = int(input("Introduceti noua inaltime a jucatorului: "))
        self.__service.modify_inaltime(nume,prenume,inaltime,"Fundas")
        print("S-a modificat playerul cu succes")

    def __best_team(self):
        fundas1,fundas2,extrema1,extrema2,pivot=self.__service.best_team()
        print("Prenume | Nume | Post | Inaltime")
        print(f"{fundas1.nume} | {fundas1.prenume} | {fundas1.inaltime} | {fundas1.post}")
        print(f"{fundas2.nume} | {fundas2.prenume} | {fundas2.inaltime} | {fundas2.post}")
        print(f"{extrema1.nume} | {extrema1.prenume} | {extrema1.inaltime} | {extrema1.post}")
        print(f"{extrema2.nume} | {extrema2.prenume} | {extrema2.inaltime} | {extrema2.post}")
        print(f"{pivot.nume} | {pivot.prenume} | {pivot.inaltime} | {pivot.post}")

    def __import(self):
        filename = input("Introduceti filename: ")
        new_players = self.__service.import_players(filename)
        print(f"S-a adaugat cu succes {new_players} jucatori din {filename}")


    def run(self):
        while True:
            try:
                print("\n 1. Add player | 2. Modify inaltime | 3. Print by an constraint | 4. Import from an specific file | 5. Exit")

                choice = input("\n Enter your choice: ")
                if choice == "1":
                    self.__add_player()
                elif choice == "2":
                    self.__modify_inaltime()
                elif choice == "3":
                    self.__best_team()
                elif choice == "4":
                    self.__import()
                elif choice == "5":
                    break
                else:
                    print("\n Invalid choice")

            except Exception as e:
                print(f"\n [ERROR] {e}")
            except ValueError:
                print("\n Ai introdus un numar care nu este un nr intreg")
