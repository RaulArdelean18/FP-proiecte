class Console:
    def __init__(self,srv):
        self.__srv = srv

    def __print_list(self):
        """
        afisez dupa filtru
        :return:
        """
        f_text,f_pret = self.__srv.get_filtru()

        text_afisaj = f"'{f_text}'" if f_text != "" else "Vid (fara filtrare denumire)"
        pret_afisaj = f_pret if f_pret != -1 else "Fara limita (pret -1)"

        print(f"\n[FILTRU CURENT] Denumire: {text_afisaj} | Pret max: {pret_afisaj}")
        print("-" * 50)

        ans = self.__srv.filter_operation()
        if not ans:
            print("Nu exista un produs valid")
        else:
            for item in ans:
                print(f"ID: {item.id} | Denumire: {item.denumire} | Pret: {item.pret}")

    def __ui_add(self):
        """
        Functie unde introduce userul datele produsului
        :return:
        """
        key = input("Introduceti id: ")
        denumire = input("Introduceti denumirea produsului: ")
        pret = float(input("Introduceti pret produsului: "))
        self.__srv.adaugare(key, denumire, pret)
        print("Produsul a fost adaugat")

    def __delete(self):
        """
        Functie unde userul sterge toate produsele care au in id o cifra stabilita de el
        :return:
        """
        key = input("Introduceti cifra: ")
        elemente_sterse = self.__srv.stergere(key)
        print(f"S-au sters {elemente_sterse} produse")

    def __filter(self):
        """
        Functie in care userul seteaza dupa ce vrea sa faca un filtru (text si pret)
        :return:
        """
        text = input("Introduceti textul pentru filtrare: ")
        pret = float(input("Introduceti pretul pentru filtru: "))
        self.__srv.set_filter(text, pret)

    def __undo(self):
        """
        Userul face o operatiune de undo la stergere
        :return:
        """
        self.__srv.undoo()
        print("S-a facut undo")

    def run(self):
        while True:
            print("\n 1. Add | 2. Delete id's by an digit | 3. Filter | 4. Undo | 5. Exit")

            opt = input("Introduceti optiunea: ")

            try:
                if opt == "1":
                    self.__ui_add()
                elif opt=="2":
                    self.__delete()
                elif opt=="3":
                    self.__filter()
                elif opt=="4":
                    self.__undo()
                elif opt=="5":
                    break
                else:
                    print("Optiune invalida")

                self.__print_list()

            except Exception as e:
                print(f"[ERROR] {e}")
            except ValueError:
                print("Nu ai introdus o valoare de tip float la pret")

