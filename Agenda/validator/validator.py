class ValidatorError(Exception):
    pass

class Validator:
    def __init__(self):
        self.__good_grup = ["Prieteni","Familie","Job"]

    def validateContact(self,contact):
        erori = []

        if contact.name=="":
            erori.append("Numele este vid")
        elif not contact.name.isalpha():
            erori.append("Numele nu este format numai din litere")

        if contact.nr_telefon=="":
            erori.append("Nr de telefon este vid")
        else:
            if not contact.nr_telefon.isdigit():
                erori.append("Nr de telefon nu este format numai din cifre")


        if contact.grup not in self.__good_grup:
            erori.append("Grupul este invalid")

        if erori:
            raise ValidatorError("; ".join(erori))

    def validate_name(self,name:str):
        erori = []
        if name=="":
            erori.append("Numele este vid")
        elif not name.isalpha():
            erori.append("Numele nu este format numai din litere")

        if erori:
            raise ValidatorError("; ".join(erori))

    def validate_group(self,group:str):
        erori = []
        if group=="":
            erori.append("Grupul este vid")
        if group not in self.__good_grup:
            erori.append("Grupul nu este valid")
        if erori:
            raise ValidatorError("; ".join(erori))
