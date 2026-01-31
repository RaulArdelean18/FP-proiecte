from Domain.domain import Jucator


class ValidatorError(Exception):
    pass

class JucatorValidator:
    def __init__(self,repo):
        self.__good_post = ["Fundas","Pivot","Extrema"]
        self.__repo = repo

    def valideaza_jucator(self,jucator):
        """
        Validez daca inputul din jucator este corect scris
        :param jucator: aici am toate informatiile de la user referitor la jucator
        :return:
        """
        errors=[]
        if jucator.nume=="":
            errors.append("Numele nu poate sa fie vid")
        elif not jucator.nume.isalpha():
            errors.append("Numele poate sa fie compus doar din litere")

        if jucator.prenume=="":
            errors.append("Prenumele nu poate sa fie vid")
        elif not jucator.prenume.isalpha():
            errors.append("Prenumele poate sa fie compus doar din litere")

        if jucator.inaltime<0:
            errors.append("Jucatorul nu poate sa aiba inaltime negativa")

        if jucator.post not in self.__good_post:
            errors.append("Jucatorul nu are o pozitie corecta")

        if errors:
            raise ValidatorError("; ".join(errors))

    def exista_player(self,jucator:Jucator):
        """
        Aceasta functie verifica daca exista jucatorul deja in echipa
        :param jucator: aici am informatiile despre jucator
        """
        echipa = self.__repo.get_all()
        gasit = False
        for items in echipa:
            #print(f"sunt in validator {items.nume} <-> {jucator.nume} | {items.prenume} <-> {jucator.prenume} {gasit}")
            if str(items.nume) == str(jucator.nume) and str(items.prenume)==str(jucator.prenume):
                gasit=True
                break

        if gasit:
            raise ValidatorError(f"Exista jucatorul {jucator.nume} - {jucator.prenume} in echipa")

    def nu_exista_player(self, jucator: Jucator):
        """
        Aceasta functie verifica daca nu exista jucatorul in echipa
        :param jucator: aici am informatiile despre jucator
        """
        echipa = self.__repo.get_all()
        gasit = False
       # print(f"Jucatori in repo din validator: {[str(j) for j in self.__repo.get_all()]}")
        for items in echipa:
            #print(f"{items.nume} <-> {jucator.nume} | {items.prenume} <-> {jucator.prenume}")
            if str(items.nume) == str(jucator.nume) and str(items.prenume) == str(jucator.prenume):
                #print("aici")
                gasit = True
                break

        if not gasit:
            raise ValidatorError(f"Nu exista jucatorul {jucator.nume} - {jucator.prenume} in echipa")

    def valid_team(self,echipa:list):
        """
        Verifica daca am cel putin 2 fundasi, 2 extreme si un pivot
        :param echipa: lista echipei din momentul de fata
        :return:
        """
        cnt_fundas=0
        cnt_extreme=0
        cnt_pivot=0
        for item in echipa:
            if item.post=="Fundas":
                cnt_fundas+=1
            elif item.post=="Extrema":
                cnt_extreme+=1
            elif item.post=="Pivot":
                cnt_pivot+=1

        if not (cnt_fundas>=2 and cnt_extreme>=2 and cnt_pivot>=1):
            raise ValidatorError("Nu avem cel putin 2 fundasi, 2 extreme si un pivot")

