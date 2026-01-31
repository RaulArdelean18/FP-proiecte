from Service.service import CartiService, CartiError


class Console:
    def __init__(self,srv):
        self.__srv=srv


    def __print_lista(self):
        f_text, f_an = self.__srv.get_filtru_current()
        print(f"\n--- Filtru curent: Text='{f_text}', An < {f_an} ---")
        carti = self.__srv.get_filtru()
        if not carti:
            print("Nicio carte de afișat.")
        for c in carti:
            print(f"ID: {c.id} | Titlu: {c.titlu} | Autor: {c.autor} | An: {c.anAparitie}")

    def run(self):
        while True:
            print("\n 1. Add carte | 2. Delete carte | 3. Filtrare | 4. Undo | 5. Exit")
            op = input("\n Enter your choice: ")
            try:
                if op == "1":
                    id_key = input("Enter carte ID: ")
                    titlu = input("Enter carte Titlu: ")
                    autor = input("Enter carte Author: ")
                    an_aparitie = input("Enter carte An Aparitie: ")
                    self.__srv.adaugare(id_key,titlu,autor,an_aparitie)
                    print("\n S-a adaugat cartea in baza de date")
                elif op=="2":
                    number = input("Enter an pe care vrei sa il elimini din baza de date: ")
                    self.__srv.stergere(number)
                    print(f"\n S-a sters cartile din anul {number}")
                elif op=="3":
                    text = input("Introdu text pentru filtrare titlu: ")
                    an = int(input("Introdu anul maxim (va afișa cărțile cu an < acesta): "))
                    self.__srv.set_filter(text, an)
                    self.__print_lista()
                elif op=="4":
                    self.__srv.undo()
                elif op=="5":
                    break
                else:
                    print("\n Operatiune invalida")

            except CartiError as e:
                print(f"[ERROR] {e}]")
            except ValueError:
                print("[ERROR] Invalid number input")



