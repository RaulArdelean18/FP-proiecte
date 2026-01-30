class Produs:
    def __init__(self, id_key:str, denumire:str, pret:float):
        self.__id = id_key
        self.__denumire = denumire
        self.__pret = pret

    # gettere

    @property
    def id(self):
        return self.__id
    @property
    def denumire(self):
        return self.__denumire
    @property
    def pret(self):
        return self.__pret

    # settere

    @pret.setter
    def pret(self, pret:float):
        self.__pret = pret
    @id.setter
    def id(self, val:str):
        self.__id = val
    @denumire.setter
    def denumire(self,denumire:str):
        self.__denumire = denumire

    def __str__(self):
        return f"{self.__id},{self.__denumire},{self.__pret}"

