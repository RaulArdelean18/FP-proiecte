from Domain.domain import Muzica


class MusicRepo:
    def __init__(self,filename):
        self.__filename=filename
        self.__piese = []
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename,'r') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(',')
                        self.__piese.append(Muzica(*parts))
        except FileNotFoundError:
            print("File not found")

    def save_to_file(self):
        with open(self.__filename,'w') as file:
            for piece in self.__piese:
                file.write(str(piece)+'\n')

    def get_all(self):
        return self.__piese

    def load_piesa(self,titlu, artist,gen,durata):
        self.__piese.append(Muzica(titlu,artist,gen,durata))

