from Domain.domain import Carte

class CartiRepo:
    def __init__(self,filename:str):
        self.__filename = filename
        self.__lista = []
        self.__stack_undo = []
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename,'r') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(',')
                        self.__lista.append(Carte(*parts))
        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open(self.__filename,'w') as file:
            for item in self.__lista:
                file.write(str(item)+"\n")

    def get_all(self):
        return self.__lista

    def adaugare(self,item:Carte):
        self.__stack_undo.append(list(self.__lista))
        self.__lista.append(item)
        self.save_to_file()

    def sterge(self,number:str):
        self.__stack_undo.append(list(self.__lista))
        new_list = []
        for item in self.__lista:
            if number not in item.anAparitie:
                new_list.append(item)
        self.__lista = new_list
        self.save_to_file()

    def undo_op(self):
        if not self.__stack_undo:
            raise Exception("Nu se mai poate face undo!")
        self.__lista = self.__stack_undo.pop()
        self.save_to_file()


