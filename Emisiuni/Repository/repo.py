from Domain.domain import Emisiune

class EmisiuneRepo:
    def __init__(self, filename):
        self.__filename = filename
        self.__emisiuni = []
        self.__load_from_file()

    def __load_from_file(self):
        """ Citește emisiunile din fișier  """
        try:
            with open(self.__filename, "r") as f:
                for line in f:
                    if line.strip():
                        parts = line.strip().split(",")
                        self.__emisiuni.append(Emisiune(*parts))
        except FileNotFoundError:
            pass

    def save_to_file(self):
        """ Salvează modificările în fișier """
        with open(self.__filename, "w") as f:
            for e in self.__emisiuni:
                f.write(str(e) + "\n")

    def get_all(self):
        return self.__emisiuni

    def sterge(self, nume, tip):
        """ Șterge emisiunea din listă """
        for i, e in enumerate(self.__emisiuni):
            if e.nume == nume and e.tip == tip:
                del self.__emisiuni[i]
                return True
        return False