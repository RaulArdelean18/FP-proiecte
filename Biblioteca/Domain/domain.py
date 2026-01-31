class Carte:
    def __init__(self, id_key:str, titlu:str, autor:str, an_aparitie:str):
        self.__id = id_key
        self.__titlu = titlu
        self.__autor = autor
        self.__anAparitie = an_aparitie


    #Gettere

    @property
    def id(self):
        return self.__id
    @property
    def titlu(self):
        return self.__titlu
    @property
    def autor(self):
        return self.__autor
    @property
    def anAparitie(self):
        return self.__anAparitie

    #Settere

    @id.setter
    def id(self, value):
        self.__id = value
    @titlu.setter
    def titlu(self, value):
        self.__titlu = value
    @autor.setter
    def autor(self, value):
        self.__autor = value
    @anAparitie.setter
    def anAparitie(self, value):
        self.__anAparitie = value

    def __str__(self):
        return f"{self.__id},{self.__titlu},{self.__autor},{self.__anAparitie}"