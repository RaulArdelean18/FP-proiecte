import random

class MuzicaError(Exception):
    pass

class MuzicaService:
    def __init__(self,repo):
        self.__repo=repo
        self.__good = ["Rock", "Pop", "Jazz", "Altele"]
        self.__titlu = ["aaaa","bbbb","cccc","dddd","eeee","ffff"]
        self.__artist = ["Paul","Raul","Costel","Marcel","Suzi"]

    def add_random(self,n:int):
        while n>0:
            titlu = random.choice(self.__titlu)
            artist = random.choice(self.__artist)
            gen = random.choice(self.__good)
            durata = random.randint(1,300)
            self.__repo.load_piesa(titlu,artist,gen,durata)
            n-=1
        self.__repo.save_to_file()


    def modify(self,titlu,artist,gen,durata:int):
        if not gen in self.__good:
            raise MuzicaError("Genul piesei nu este bun")
        if durata < 0:
            raise MuzicaError("Durata este negativa")
        gasit = False

        for e in self.__repo.get_all():
            if e.titlu == titlu and e.artist==artist:
                e.gen=gen
                e.durata=durata
                gasit = True
                break

        if not gasit:
            raise MuzicaError("Piesa nu exista in lista")

        self.__repo.save_to_file()

    def export_file(self,filename:str):
        lista = self.__repo.get_all()

        try:
            with open(filename,"w") as file:
                for e in lista:
                    file.write(str(e)+"\n")
        except IOError:
            print(f"Nu s-a putut scrie in {filename}")


