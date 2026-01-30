class Piesa:
    def __init__(self, titlu, regizor, gen, durata:int):
        self.__titlu = titlu
        self.__regizor = regizor
        self.__gen = gen
        self.__durata = durata

    # Gettere
    @property
    def titlu(self):
        return self.__titlu

    @property
    def regizor(self):
        return self.__regizor

    @property
    def gen(self):
        return self.__gen

    @property
    def durata(self):
        return self.__durata

    # Setter
    @titlu.setter
    def titlu(self, titlu):
        self.__titlu = titlu

    @regizor.setter
    def regizor(self, regizor):
        self.__regizor = regizor

    @gen.setter
    def gen(self, gen):
        self.__gen = gen

    @durata.setter
    def durata(self, durata):
        self.__durata = durata

    def __str__(self):
        return f"{self.__titlu},{self.__regizor},{self.__gen},{self.__durata}"