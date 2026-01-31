import unittest
from Repository.repo import JucatorRepo
from Service.service import ServiceJucator
from Validator.validator import JucatorValidator
from utils.utils import copy_file_content, clear_file_content


class Test(unittest.TestCase):
    def setUp(self):
        """
        Pentru fiecare test deschid si bag Costel,Marcel,200,Fundas in data_default, daca nu il gaseste
        :return:
        """
        try:
            copy_file_content("data_default.txt","test_data.txt")
        except FileNotFoundError:
            with open("data_default.txt", "w") as f:
                f.write("Costel,Marcel,200,Fundas")
            copy_file_content("data_default.txt","test_data.txt")

        self.repo = JucatorRepo("test_data.txt")
        self.validator = JucatorValidator(self.repo)
        self.service = ServiceJucator(self.repo,self.validator)

    def tearDown(self):
        """
        Pt fiecare test sterg datele din fisier
        :return:
        """
        clear_file_content("test_data.txt")

    def test_adaugare(self):
        """
        Verific daca se adauga corect in repo
        :return:
        """
        with self.assertRaises(Exception):
            self.service.add_player("Costel","Marcel",200,"Fundas")
        with self.assertRaises(Exception):
            self.service.add_player("Marcel","Paul","a","Fundas")
        with self.assertRaises(Exception):
            self.service.add_player("Marcel","Paul",200,"Tractor")

        self.service.add_player("Raul","Costel",200,"Fundas")
        self.assertEqual(len(self.repo.get_all()),2)

        with self.assertRaises(Exception):
            self.service.add_player("Horia","Costel",-1,"Fundas")

        with self.assertRaises(Exception):
            self.service.add_player("Horia",3,200,"Fundas")

        with self.assertRaises(Exception):
            self.service.add_player("2314","Mario",200,"Extrema")

    def test_modificare(self):
        """
        Verific sa vad daca codul se comporta corect cand modific inaltimea unui player
        """

        with self.assertRaises(Exception):
            self.service.modify_inaltime("Costel","Marcel",-1,"Fundas")
        #print(f"Jucatori in repo: {[str(j) for j in self.repo.get_all()]}")
        with self.assertRaises(Exception):
            self.service.modify_inaltime("Raul","Marcel",200,"Fundas")

        self.service.modify_inaltime("Costel","Marcel",201,"Fundas")

    def test_team(self):
        """
        Verific daca face cea mai buna echipa
        :return: noothing
        """
        self.service.add_player("Raul","Costel",201,"Fundas")
        self.service.add_player("Horia","Costel",202,"Fundas")
        self.service.add_player("Maria", "Marcel", 201, "Extrema")
        self.service.add_player("Maria", "Marcela", 203, "Extrema")
        self.service.add_player("Marian", "Marcela", 202, "Extrema")
        self.service.add_player("Marian", "Luca", 180, "Pivot")
        self.service.add_player("Marian", "Lucian", 181, "Pivot")

        fundas1,fundas2,extrema1,extrema2,pivot = self.service.best_team()

        self.assertTrue(fundas1.nume == "Horia" and fundas1.prenume=="Costel" and int(fundas1.inaltime)==202)
        self.assertTrue(fundas2.nume == "Raul" and fundas2.prenume=="Costel" and int(fundas2.inaltime)==201)
        self.assertTrue(extrema1.nume == "Maria" and extrema1.prenume=="Marcela" and int(extrema1.inaltime)==203)
        self.assertTrue(extrema2.nume == "Marian" and extrema2.prenume=="Marcela" and int(extrema2.inaltime)==202)
        self.assertTrue(pivot.nume == "Marian" and pivot.prenume=="Lucian" and int(pivot.inaltime)==181)

    def test_import(self):
        """
        Verificam daca importul functioneaza corect
        """
        with open("test_import_file.txt", "w") as f:
            f.write("Ionescu Andrei\n")
            f.write("Costel Marcel\n")

        nr_adaugati = self.service.import_players("test_import_file.txt")

        self.assertEqual(nr_adaugati, 1)
        self.assertEqual(len(self.repo.get_all()), 2)
        nr_inexistent = self.service.import_players("non_existent.txt")
        self.assertEqual(nr_inexistent, 0)

    def test_import_existent(self):
        """
        Verific daca nu se adauga un jucator
        :return:
        """
        with open("test_existent.txt", "w") as f:
            f.write("Costel Marcel\n")

        added_count = self.service.import_players("test_existent.txt")
        self.assertEqual(added_count, 0)

if __name__ == "__main__":
    unittest.main()