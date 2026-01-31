import unittest

from Repository.Repo import CartiRepo
from Service.service import CartiService, CartiError
from utils.file_utils import clear_file_content, copy_file_content


class TestsBibliotecaService(unittest.TestCase):
    def setUp(self):
        copy_file_content("data_default.txt", "test_data.txt")

        self.repo = CartiRepo("test_data.txt")
        self.srv = CartiService(self.repo)

    def tearDown(self):
        clear_file_content("test_data.txt")

    def test_add_persists(self):
        initial_size = len(self.srv.get_filtru())
        self.srv.adaugare("10", "Carte", "Autor", "2000")

        self.assertEqual(len(self.srv.get_filtru()), initial_size + 1)

        repo2 = CartiRepo("test_data.txt")
        self.assertEqual(len(repo2.get_all()), initial_size + 1)

    def test_add_duplicate_id_raises(self):
        self.srv.adaugare("1", "Carte1", "Autor", "2000")
        with self.assertRaises(CartiError):
            self.srv.adaugare("1", "Carte2", "AltAutor", "2001")

    def test_delete_by_digit(self):
        self.srv.adaugare("1", "C1", "A", "2005")
        self.srv.adaugare("2", "C2", "B", "2010")
        self.srv.adaugare("3", "C3", "C", "1995")

        self.srv.stergere("5")

        for c in self.srv.get_filtru():
            self.assertNotIn("5", str(c.anAparitie))

        repo2 = CartiRepo("test_data.txt")
        for c in repo2.get_all():
            self.assertNotIn("5", str(c.anAparitie))

    def test_undo_restores_last_delete(self):
        self.srv.adaugare("1", "C1", "A", "2005")
        self.srv.adaugare("2", "C2", "B", "2010")

        self.srv.stergere("5")
        self.assertEqual(len(self.srv.get_filtru()), 1)

        self.srv.undo()
        self.assertEqual(len(self.srv.get_filtru()), 2)

        # persistenta dupa undo
        repo2 = CartiRepo("test_data.txt")
        self.assertEqual(len(repo2.get_all()), 2)

    def test_filter(self):
        self.srv.adaugare("1", "Python Programming", "A", "2010")
        self.srv.adaugare("2", "Java", "B", "2000")

        self.srv.set_filter("python", 2015)
        rez = self.srv.get_filtru()
        self.assertEqual(len(rez), 1)
        self.assertEqual(rez[0].titlu, "Python Programming")

    def test_undo_without_delete_raises(self):
        with self.assertRaises(Exception):
            self.srv.undo()


if __name__ == "__main__":
    unittest.main(verbosity=2)
