from Domain.domain import Jucator
from Validator.validator import ValidatorError
import random

class ServiceJucator:
    def __init__(self,repo,validator):
        self.__repo = repo
        self.__validator = validator
        self.__good_post = ["Fundas", "Pivot", "Extrema"]

    def add_player(self,nume:str,prenume:str,inaltime:int,post:str):
        """
        Functia verifica si adauga player ul
        :param nume: numele jucatorului, string
        :param prenume: prenume jucatorului, string
        :param inaltime: inaltimea jucatorului, int
        :param post: postul jucatorului, string
        :return:
        """
        player = Jucator(nume,prenume,inaltime,post)
        self.__validator.valideaza_jucator(player)
        self.__validator.exista_player(player)
        self.__repo.add_jucator(player)
        self.__repo.save_to_file()

    def modify_inaltime(self,nume:str,prenume:str,inaltime:int,post:str):
        """
        Modific inaltimea jucatorului
        :param nume: numele jucatorului, string
        :param prenume: prenumele jucatorului, string
        :param inaltime: inaltimea jucatorului, int
        :param post: postul jucatorului, string
        :return:
        """
        player = Jucator(nume,prenume,inaltime,post)
        self.__validator.valideaza_jucator(player)
        self.__validator.nu_exista_player(player)
        self.__repo.modify_jucator(player)
        self.__repo.save_to_file()

    def best_team(self):
        """
        Afla cea mai buna echipa cu cei mai mari fundasi, extreme si pivot
        :return: dau return la un tuple de Jucatori cu 2 fundasi, 2 extreme si un pivot
        """
        echipa = self.__repo.get_all()
        self.__validator.valid_team(echipa)

        fundas = []

        for player in echipa:
            if player.post == "Fundas":
                fundas.append(player)

        sorted_fundas = sorted(fundas, key=lambda player: int(player.inaltime), reverse=True)

        extreme = []

        for player in echipa:
            if player.post == "Extrema":
                extreme.append(player)

        sorted_extreme = sorted(extreme, key=lambda player: int(player.inaltime), reverse=True)

        pivot = []

        for player in echipa:
            if player.post == "Pivot":
                pivot.append(player)

        sorted_pivot = sorted(pivot, key=lambda player: int(player.inaltime), reverse=True)

        return sorted_fundas[0],sorted_fundas[1], sorted_extreme[0],sorted_extreme[1], sorted_pivot[0]

    def import_players(self, filename:str):
        """
        Functia da import la player care nu se afla in echipa si da return la cati jucatori au intrat in echipa
        :param filename: filenamul de unda luma numele jucatorilor (str)
        :return: cati jucatori s-au adaugat in echipa (int)
        """
        cnt = 0
        try:
            with open(filename) as file:
                for line in file:
                    if line.strip():
                        parts = line.strip().split(" ")
                        inaltime = random.randint(150, 270)
                        post = random.choice(self.__good_post)
                        #print(f"Jucatori in repo: {[str(j) for j in self.__repo.get_all()]}")
                        #print(f"Nume {parts[0]} | Prenume {parts[1]} | Inaltime {inaltime} | Post {post}")
                        try:
                            self.__validator.valideaza_jucator(Jucator(parts[0],parts[1],inaltime,post))
                            self.__validator.exista_player(Jucator(parts[0],parts[1],inaltime,post))
                        except ValidatorError:
                            continue
                        cnt += 1
                        self.__repo.add_jucator(Jucator(parts[0],parts[1],inaltime,post))
                        self.__repo.save_to_file()

        except FileNotFoundError:
            pass

        return cnt