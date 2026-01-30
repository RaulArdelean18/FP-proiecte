class Console:
    def __init__(self,srv):
        self.__srv = srv

    def __print_list(self):
        """
        afisez dupa filtru
        :return:
        """
        ans = self.__srv.filter_operation()
        if not ans:
            print("Nu exista un produs valid")
        else:
            for item in ans:
                print(f"ID: {item.id} | Denumire: {item.denumire} | Pret: {item.pret}")

    def run(self):
        while True:
            print("\n 1. Add | 2. Delete id's by an digit | 3. Filter | 4. Undo | 5. Exit")

            opt = input("Introduceti optiunea: ")

            try:
                if opt == "1":
                    key = input("Introduceti id: ")
                    denumire = input("Introduceti denumirea produsului: ")
                    pret = float(input("Introduceti pret produsului: "))
                    self.__srv.adaugare(key,denumire,pret)
                    print("Produsul a fost adaugat")
                elif opt=="2":
                    key = input("Introduceti cifra: ")
                    self.__srv.stergere(key)
                    print("Produsul a fost sters")
                elif opt=="3":
                    text = input("Introduceti textul pentru filtrare: ")
                    pret = float(input("Introduceti pretul pentru filtru: "))
                    self.__srv.set_filter(text,pret)
                    self.__print_list()
                elif opt=="4":
                    self.__srv.undoo()
                    print("S-a facut undo")
                elif opt=="5":
                    break
                else:
                    print("Optiune invalida")

            except Exception as e:
                print(f"[ERROR] {e}")
            except ValueError:
                print("Nu ai introdus o valoare de tip float la pret")

