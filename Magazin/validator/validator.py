class ValidatorError(Exception):
    pass


class ValidatorMagazin:
    def valideaza_produs(self, produs):
        """
        Valideaza un produs la adaugare
        :param produs: structura de date unde avem id, denumire si pret
        :return: nothing
        """
        erori = []
        if not produs.id:
            erori.append("ID-ul nu poate fi vid")

        if not produs.denumire:
            erori.append("Denumirea nu poate fi vidă")
        elif not produs.denumire.isalpha():
            erori.append("Denumirea trebuie sa fie formata doar din litere")
        if produs.pret <= 0:
            erori.append("Prețul trebuie să fie un număr pozitiv")

        if erori:
            raise ValidatorError("; ".join(erori))

    def valideaza_cifra_stergere(self, cifra_str:str):
        """
        Valideaza task ul 2, verifica sa vada daca exista cifra_str in id uri
        :param cifra_str: o cifra
        :return: nothing
        """
        if len(cifra_str) != 1 or not cifra_str.isdigit():
            raise ValidatorError("Trebuie să introduceți exact O CIFRĂ (0-9) pentru ștergere!")

    def valideaza_parametri_filtru(self, text:str, pret:float):
        """
        Valideaza daca parametri filtrului sunt corecti
        :param text: un string cu un text
        :param pret: o variabila de tip float
        :return: nothung
        """

        if pret < 0 and pret != -1:
            raise ValidatorError("Prețul de filtrare trebuie să fie pozitiv sau -1 pentru dezactivare!")
        if text!="" and not text.isalpha():
            raise ValidatorError("Textul de filtrare trebuie sa fie compus doar din litere")