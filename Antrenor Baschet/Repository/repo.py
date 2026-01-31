from Domain.domain import Jucator

class JucatorRepo:
    def __init__(self,filename:str):
        self.__filename = filename
        self.__echipa = []
        self.__load_from_file()

    def __load_from_file(self):
        try:
            with open(self.__filename,"r") as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(",")
                        self.__echipa.append(Jucator(parts[0],parts[1],int(parts[2]),parts[3]))

        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open(self.__filename,"w") as file:
            for echipa in self.__echipa:
                file.write(str(echipa)+"\n")

    def get_all(self):
        return self.__echipa

    def add_jucator(self,jucator:Jucator):
        """
        Adaug jucatorul in echipa
        :param jucator:
        :return:
        """
        self.__echipa.append(jucator)
        self.save_to_file()

    def modify_jucator(self,jucator:Jucator):
        """
        Modific jucatorul cu numele si prenumele cunoscut, ii modificam doar inaltimea
        :param jucator:
        :return:
        """
        for item in self.__echipa:
            if item.nume == jucator.nume and item.prenume==jucator.prenume:
                item.inaltime = jucator.inaltime
                break
        self.save_to_file()