from Domain.domain import Contact

class ContactError(Exception):
    pass

class Service:
    def __init__(self,repo,validator):
        self.__repo = repo
        self.__validator = validator

    def add_contact(self, id_key:int, nume:str, nr_telefon:str, grup:str):
        contact = Contact(id_key, nume, nr_telefon, grup)
        self.__validator.validateContact(contact)
        if not self.__repo.verify_name(contact.name):
            raise ContactError("Numele este deja in contacte")
        if not self.__repo.verify_id(contact.id):
            raise ContactError("Id ul se afla in contacte")

        self.__repo.add(contact)

    def find_number(self,name:str):
        """
        Functia returneaza nr de telefon pentru numele dat, daca exista in lista de contace, daca nu exista, dau return "Nu exista"
        :param name: numele persoanei de la care vrem sa aflam nr de telefon din contact
        :return: un string cu mesajul aferenet
        """
        self.__validator.validate_name(name)
        nr_telefon = self.__repo.find_number(name)
        if nr_telefon is None:
            return "Nu exista in contacte"
        else: return nr_telefon

    def filter_by_group(self,group:str):
        """
        Filtreaza si sorteaza lista de contacte dupa group
        :param group: grupul tinta
        :return: lista cu contactele din grup daca nevida, None daca este vida
        """
        self.__validator.validate_group(group)
        return self.__repo.get_group_sorted(group)

    def export_by_group(self,group:str):
        self.__validator.validate_group(group)
        return self.__repo.get_group(group)

