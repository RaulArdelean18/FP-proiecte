from Repository.Repo import CartiRepo
from Service.service import CartiService, CartiError


class Teste:
    def __init__(self):
        self.__test_file=("test_data.txt")
        self.__reset_file()
        self.__repo=CartiRepo(self.__test_file)
        self.__service = CartiService(self.__repo)

    def __reset_file(self):
        with open(self.__test_file, "w") as f:
            f.write("")

    def teste_all(self):
        print("\n Run tests")
        self.__teste_adaugare()
        self.__test_stergere()
        self.__test_filtrare()
        self.__test_undo()
        self.__test_validare_id()

    def __test_validare_id(self):
        self.__reset_file()
        self.__service.adaugare("unique_1", "Titlu", "Autor", "2000")

        try:
            self.__service.adaugare("unique_1", "Alt Titlu", "Alt Autor", "2022")
            assert False, "Ar fi trebuit să arunce CartiError pentru ID duplicat"
        except CartiError:
            assert True

    def __teste_adaugare(self):
        initial_count = len(self.__service.get_filtru())
        self.__service.adaugare("5","Ana","Paul","2022")
        assert initial_count+1 == len(self.__service.get_filtru())

        repo_nou = CartiRepo(self.__test_file)
        assert len(repo_nou.get_all())==1

    def __test_stergere(self):
        self.__service.adaugare("6","Anaare","Paul","2022")
        self.__service.stergere("5")

        lista = self.__service.get_filtru()

        for filtru in lista:
            assert '5' not in str(filtru.anAparitie)

    def __test_filtrare(self):
        self.__service.adaugare("3", "Python Programming", "Autor", "2010")
        self.__service.set_filter("Python", 2015)
        rezultat = self.__service.get_filtru()
        assert len(rezultat) == 1
        assert rezultat[0].titlu == "Python Programming"

        self.__service.set_filter("Python", 2000)
        assert len(self.__service.get_filtru()) == 0

    def __test_undo(self):
        self.__reset_file()
        repo = CartiRepo(self.__test_file)
        srv = CartiService(repo)
        srv.adaugare("1", "Carte1", "A", "2000")
        srv.adaugare("2", "Carte2", "B", "2005")

        srv.stergere("5")
        assert len(srv.get_filtru()) == 1

        srv.undo()
        assert len(srv.get_filtru()) == 2