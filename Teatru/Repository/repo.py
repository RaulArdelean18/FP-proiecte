from Domain.domain import Piesa

class PiesaRepo:
    def __init__(self,filename):
        self.__filename = filename
        self.__piese = []
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename,'r') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(',')
                        self.__piese.append(Piesa(*parts))
        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open(self.__filename,'w') as f:
            for e in self.__piese:
                f.write(str(e)+'\n')

    def get_all(self):
        return self.__piese

    def load_piese(self,titlu, regizor, gen, durata):
        self.__piese.append(Piesa(titlu, regizor, gen, durata))
