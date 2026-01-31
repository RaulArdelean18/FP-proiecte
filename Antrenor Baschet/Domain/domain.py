class Jucator:
    def __init__(self, nume:str,prenume:str,inaltime:int,post:str):
        self.__nume = nume
        self.__prenume = prenume
        self.__inaltime = inaltime
        self.__post = post

    # gettere

    @property
    def nume(self):
        return self.__nume
    @property
    def prenume(self):
        return self.__prenume
    @property
    def inaltime(self):
        return self.__inaltime
    @property
    def post(self):
        return self.__post

    # settere

    @nume.setter
    def nume(self,nume:str):
        self.__nume = nume
    @prenume.setter
    def prenume(self,prenume:str):
        self.__prenume = prenume
    @inaltime.setter
    def inaltime(self,inaltime:int):
        self.__inaltime = inaltime
    @post.setter
    def post(self,post:str):
        self.__post = post

    def __str__(self):
        return f"{self.__nume},{self.prenume},{self.inaltime},{self.post}"

