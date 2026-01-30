class Emisiune:
    def __init__(self, nume, tip, durata, descriere):
        """ Inițializează o emisiune  """
        self.__nume = nume
        self.__tip = tip
        self.__durata = int(durata)
        self.__descriere = descriere

    # Gettere
    @property
    def nume(self):
        return self.__nume

    @property
    def tip(self):
        return self.__tip

    @property
    def durata(self):
        return self.__durata

    @property
    def descriere(self):
        return self.__descriere

    @durata.setter
    def durata(self, value):
        self.__durata = int(value)

    @descriere.setter
    def descriere(self, value):
        self.__descriere = value

    def __str__(self):
        return f"{self.__nume},{self.__tip},{self.__durata},{self.__descriere}"
