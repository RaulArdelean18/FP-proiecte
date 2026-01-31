import unittest
from repository.repo import RepoMagazin
from Service.service import Service, ProduseError
from utils.file_utils import clear_file_content, copy_file_content
from validator.validator import ValidatorMagazin

class TesteMagazin(unittest.TestCase):
    def setUp(self):
        try:
            copy_file_content("data_default.txt","test_data.txt")
        except FileNotFoundError:
            with open("data_default.txt", "w") as f:
                f.write("1,Mere,3.53\n")
            copy_file_content("data_default.txt", "test_data.txt")
        self.repo = RepoMagazin("test_data.txt")
        self.validator = ValidatorMagazin()
        self.service = Service(self.repo,self.validator)

    def tearDown(self):
        clear_file_content("test_data.txt")

    def test_add_persist(self):
        """
        verifica daca adaugarea persista intre service si repo
        """
        size = len(self.service.filter_operation())
        self.service.adaugare("1","Mere",3.53)
        self.assertEqual(len(self.service.filter_operation()), size+1)

        repo2 = RepoMagazin("test_data.txt")
        self.assertEqual(len(repo2.get_all()), size+1)

    def test_add_duplicate(self):
        """
        verifica cazul cand adaugam duplicate
        """
        self.service.adaugare("1", "Mere", 3.53)

        with self.assertRaises(Exception):
            self.service.adaugare("1", "Pere", 3.42)

    def test_delete(self):
        """
        verificam daca delete se comporta corect
        """
        self.service.adaugare("1","Mere",3.53)
        self.service.adaugare("2","Pere",13.42)
        self.service.adaugare("3","Prune",4.83)

        self.service.stergere("3")
        self.assertEqual(len(self.service.filter_operation()), 2)

        for item in self.service.filter_operation():
            self.assertNotEqual(item.id,"3")

        repo2 = RepoMagazin("test_data.txt")
        self.assertEqual(len(repo2.get_all()), 2)
        for item in repo2.get_all():
            self.assertNotEqual(item.id,"3")

        self.service.adaugare("323","Tuica",13.49)
        self.service.stergere("3")

        self.assertEqual(len(self.service.filter_operation()), 2)

    def test_undo(self):
        """
        verificam daca undoo se comporta corect
        """
        self.service.adaugare("1","Mere",3.53)
        self.service.adaugare("2","Pere",13.42)
        self.service.adaugare("3","Prune",4.83)
        self.service.stergere("3")

        self.service.undoo()
        self.assertEqual(len(self.service.filter_operation()), 3)
        gasit = False
        for item in self.service.filter_operation():
            if item.id == "3":
                gasit = True
                break

        self.assertTrue(gasit)
        self.service.stergere("3")
        self.service.stergere("2")
        self.service.stergere("1")
        self.assertEqual(len(self.service.filter_operation()), 0)
        self.service.undoo()
        self.assertEqual(len(self.service.filter_operation()), 1)
        self.service.undoo()
        self.assertEqual(len(self.service.filter_operation()), 2)

        self.service.adaugare("343","Prune",4.83)
        self.service.stergere("3")
        self.assertEqual(len(self.service.filter_operation()), 2)


    def test_filter(self):
        """
        verificam daca filter ul functioneaza corect
        """
        self.service.adaugare("1","Mere",3.53)
        self.service.adaugare("2","Pere",13.42)

        ans = self.service.filter_operation()

        self.assertEqual(len(ans), 2)
        self.service.adaugare("3","Mere",4.83)
        self.service.set_filter("Mere",4)

        ans = self.service.filter_operation()

        self.assertEqual(len(ans), 1)

    def test_undo_empty(self):
        """
        verificam cand undo ii empty
        """
        with self.assertRaises(Exception):
            self.service.undoo()

    def test_filter_reset(self):
        """
        verificam resetul filterului
        """
        self.service.adaugare("1", "Mere", 10.0)
        self.service.set_filter("Mere", 15.0)
        self.assertEqual(len(self.service.filter_operation()), 1)

        self.service.set_filter("", -1)
        self.assertEqual(len(self.service.filter_operation()), 1)

if __name__ == '__main__':
    unittest.main()