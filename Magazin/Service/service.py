class ProduseError(Exception):
    pass

class Service:
    def __init__(self,repo):
        self.__repo = repo
        self.__filtru_text = ""
        self.__filtru_pret = -1

    def adaugare(self, id_key:str, denumire:str, pret:float):
        """
        Verific daca produsul nu se afla pana acum in data base
        daca nu exista, il adaug
        """
        toate = self.__repo.get_all()

        for item in toate:
            if item.id == id_key:
                raise ProduseError(f"Id ul {id_key} is already in database")

        self.__repo.add_produs(id_key, denumire, pret)
        self.__repo.save_to_file()

    def stergere(self, id_key:str):
        """
        Verific daca exista id uri cu valoarea id_key
        :param id_key:
        :return: noothing
        """
        toate = self.__repo.get_all()
        new_list =[]
        for item in toate:
            #print(f"{item.id} -> {id_key}")
            if id_key not in str(item.id):
                new_list.append(item)

        self.__repo.replace(new_list)
        self.__repo.save_to_file()

    def undoo(self):
        """
        Apelez functia de undoo din repo
        :return:
        """
        self.__repo.undo_operation()
        self.__repo.save_to_file()

    def set_filter(self,text:str, pret:float):
        """
        imi setez filtrul cu text si pret
        :param text:
        :param pret:
        :return: nothing
        """
        self.__filtru_text = text
        self.__filtru_pret = pret

    def get_filtru(self):
        """
        aflu ce filtru am stocat
        :return: filtru
        """
        return self.__filtru_text, self.__filtru_pret


    def filter_operation(self):
        """
        imi filtrez lista dupa text si pret
        :return: lista cu produsele valide
        """
        lista = self.__repo.get_all()

        if self.__filtru_text == "" and self.__filtru_pret == -1:
            return lista

        ans = []

        for item in lista:
            if self.__filtru_text.lower() in item.denumire.lower() and float(item.pret) < float(self.__filtru_pret):
                ans.append(item)

        return ans



