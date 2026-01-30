import random

class PiesaError(Exception):
    pass

class PiesaService:
    def __init__(self,repo):
        self.__repo = repo
        self.__good = ["Comedie","Drama","Satira","Altele"]
        self.__title_names = ["aaaa","bbbb","cccc","dddd","eeee","ffff"]
        self.__regizor_names = ["Ana","Paul","Marcel","Costel","Suzi"]

    def add_piesa(self,titlu, regizor, gen, durata):
        if not gen in self.__good:
            raise PiesaError("Nu este un gen valid")
        self.__repo.load_piese(titlu, regizor, gen, durata)
        self.__repo.save_to_file()

    def modify_piesa(self,titlu, regizor, gen, durata):
        if not gen in self.__good:
            raise PiesaError("Nu este un gen valid")
        gasit = False
        for e in self.__repo.get_all():
            #print(dir(e))
            if e.titlu == titlu and e.regizor == regizor:
                gasit = True
                e.gen=gen
                e.durata=durata
                break

        if not gasit:
            raise PiesaError("Nu s-a gasit piesa in lista")
        self.__repo.save_to_file()

    def add_random(self,n:int):
        while n>0:
            titlu = random.choice(self.__title_names)
            regizor = random.choice(self.__regizor_names)
            gen = random.choice(self.__good)
            durata = random.randint(1,120)
            self.add_piesa(titlu, regizor, gen, durata)
            n -= 1
        self.__repo.save_to_file()

    def export_file(self,filename:str):
        lista = self.__repo.get_all()
        list_sorted = sorted(lista,key=lambda e: (e.regizor, e.gen))

        try:
            with open(filename,"w") as f:
                for piesa in list_sorted:
                    f.write(str(piesa)+"\n")
        except IOError:
            print(f"Nu s-a putut scrie in {filename}")

