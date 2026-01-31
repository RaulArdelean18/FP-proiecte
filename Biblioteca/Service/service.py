from Repository.Repo import *

class CartiError(Exception):
    pass


class CartiService:
    def __init__(self, repo):
        self.__repo = repo
        self.__filtru_text=""
        self.__filtru_an=-1

    def adaugare(self,id_key:str,titlu:str,autor:str,an_aparitie:str):
        toate = self.__repo.get_all()
        for c in toate:
            if c.id == id_key:
                raise CartiError(f"ID-ul {id_key} există deja în bibliotecă!")
        carte = Carte(id_key,titlu,autor,an_aparitie)
        self.__repo.adaugare(carte)
        self.__repo.save_to_file()

    def stergere(self,number:str):
        self.__repo.sterge(number)
        self.__repo.save_to_file()

    def undo(self):
        self.__repo.undo_op()
        self.__repo.save_to_file()

    def set_filter(self,text,an):
        self.__filtru_text = text
        self.__filtru_an = an

    def get_filtru_current(self):
        return self.__filtru_text,self.__filtru_an

    def get_filtru(self):
        lista = self.__repo.get_all()

        if self.__filtru_text == "" and self.__filtru_an == -1:
            return lista

        ans = []

        for item in lista:
            if self.__filtru_text.lower() in item.titlu.lower() and int(item.anAparitie)<int(self.__filtru_an):
                ans.append(item)

        return ans



