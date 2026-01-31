class Contact:
    def __init__(self, id_val:int,name:str, nr_telefon:str, grup:str):
        self.__id = id_val
        self.__name = name
        self.__nr_telefon = nr_telefon
        self.__grup = grup

    # gettere

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def nr_telefon(self):
        return self.__nr_telefon

    @property
    def grup(self):
        return self.__grup

    def __str__(self):
        return f"{self.__id},{self.__name},{self.__nr_telefon},{self.__grup}"