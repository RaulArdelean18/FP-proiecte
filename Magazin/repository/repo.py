from Domain.domain import Produs

class RepoMagazin:
    def __init__(self, filename:str):
        self.__filename = filename
        self.__lista = []
        self.__undo_list = []
        self.__load_from_file()

    def __load_from_file(self):
        """
        Preiau datele care le-am avut anterior
        :return: nothing
        """
        try:
            with open(self.__filename,'r') as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(',')
                        self.__lista.append(Produs(parts[0],parts[1],float(parts[2])))
        except FileNotFoundError:
            pass

    def save_to_file(self):
        """
        Salvez lista in filename
        :return: o lista cu datele actuale
        """
        with open(self.__filename,'w') as file:
            for item in self.__lista:
                file.write(str(item)+"\n")

    def get_all(self):
        """
        Preia toate datele din momentul de fata
        :return: o lista cu datele
        """
        return self.__lista

    def add_produs(self, id_key:str, denumire:str, pret:float):
        """
        Adaug item ul in lista
        :return: nothing
        """
        #print(f"repo {id_key}")
        self.__lista.append(Produs(id_key,denumire,pret))
        self.save_to_file()

    def replace(self, ans:list):
        """
        dau replace la __lista cu ans
        :param ans:
        :return:
        """
        self.__undo_list.append(list(self.__lista))
        self.__lista = ans
        self.save_to_file()

    def undo_operation(self):
        """
        Verific daca pot face op de undo. Daca o pot face, o fac
        :return:
        """
        if not self.__undo_list:
            raise Exception("Nu se mai poate face undo!")
        self.__lista = self.__undo_list.pop()
        self.save_to_file()




