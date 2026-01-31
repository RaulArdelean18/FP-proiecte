from Domain.domain import Contact

class RepositoryException(Exception):
    pass

class RepositoryContact:
    def __init__(self,filename):
        self.__filename = filename
        self.__contacts = []
        self.__load_from_file()

    def __load_from_file(self):
        with open(self.__filename,'r') as file:
            for line in file:
                if line.strip():
                    part = line.strip().split(',')
                    self.__contacts.append(Contact(int(part[0]),part[1],part[2],part[3]))

    def __write_to_file(self):
        with open(self.__filename,'w') as file:
            for contact in self.__contacts:
                file.write(str(contact)+"\n")

    def get_all(self):
        """
        Ne da lista de contacte
        :return: o lista de contacte
        """
        return self.__contacts

    def add(self,contact):
        """
        Adauga contactul din baza de date
        :param contact: contactul persoanei
        :return:
        """
        self.__contacts.append(contact)
        self.__write_to_file()

    def verify_name(self,name:str):
        """
        Functia verifica sa vada daca name se afla in lista
        :param name: numele persoanei cautate
        :return: True / False
        """
        for item in self.__contacts:
            if item.name == name:
                return False
        return True
    def verify_id(self,id:int):
        """
        Functia verifica daca exista un contact deja cu id
        :param id: id ul persoanei pe care vrem sa il adaugam
        :return: True daca nu exista, False daca exista
        """
        for item in self.__contacts:
            if item.id == id:
                return False
        return True

    def find_number(self,name:str):
        """
        Functia da return la numarul de contact al persoanei name
        :param name: persoana la care dorim sa aflam numarul
        :return:
        """

        for item in self.__contacts:
            if item.name == name:
                return item.nr_telefon

        return None

    def get_group_sorted(self,group:str):
        new_list = []
        for contact in self.__contacts:
            if contact.grup == group:
                new_list.append(contact)

        if new_list:
            sorted_list = sorted(new_list, key=lambda x: x.name, reverse=False)
            return sorted_list
        else:
            return None

    def get_group(self,group:str):
        new_list = []
        for contact in self.__contacts:
            if contact.grup == group:
                new_list.append(contact)

        return new_list