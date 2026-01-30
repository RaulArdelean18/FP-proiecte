class Muzica:
    def __init__(self,titlu,artist,gen,durata):
        self.__titlu=titlu
        self.__artist=artist
        self.__gen=gen
        self.__durata=durata

    # gettere

    @property
    def titlu(self):
        return self.__titlu
    @property
    def artist(self):
        return self.__artist
    @property
    def gen(self):
        return self.__gen
    @property
    def durata(self):
        return self.__durata

    #settere

    @titlu.setter
    def titlu(self,titlu):
        self.__titlu=titlu
    @artist.setter
    def artist(self,artist):
        self.__artist=artist
    @gen.setter
    def gen(self,gen):
        self.__gen=gen
    @durata.setter
    def durata(self,durata):
        self.__durata=durata

    def __str__(self):
        return f"{self.titlu},{self.artist},{self.gen},{self.durata}"