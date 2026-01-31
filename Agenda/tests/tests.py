import unittest
from Domain.domain import Contact
from Repository.repo import RepositoryContact
from Service.service import Service, ContactError
from validator.validator import ValidatorError, Validator


class DomainTests(unittest.TestCase):
    def testDomain(self):
        contact = Contact(1,"Raul","0898311331","Familie")
        self.assertEqual(contact.id,1)
        self.assertEqual(contact.name,"Raul")
        self.assertEqual(contact.nr_telefon,"0898311331")
        self.assertEqual(contact.grup,"Familie")

class RepositoryContactTests(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoryContact("test_contact.txt")
    def tearDown(self):
        with open("test_contact.txt","w") as f:
            f.write("1,Raul,0898311331,Familie")

    def test_get_all(self):
        contact = self.repo.get_all()
        self.assertTrue(contact[0].id==1)
        self.assertTrue(contact[0].name == "Raul")
        self.assertTrue(contact[0].nr_telefon == "0898311331")
        self.assertTrue(contact[0].grup == "Familie")

    def test_add(self):
        """
        Verificam daca add_contact functioneaza corect
        :return:
        """
        n = len(self.repo.get_all())
        contact = Contact(2,"Mario","4242242243","Familie")
        self.repo.add(contact)
        self.assertEqual(n+1,len(self.repo.get_all()))
        with self.assertRaises(Exception):
            self.repo.add_contact(Contact(3,"Mario","123","Familie"))

        with self.assertRaises(Exception):
            self.repo.add_contact(Contact(4,"Marcel","1234","Familiea"))

        with self.assertRaises(Exception):
            self.repo.add_contact(Contact("12","Maria","122323123","Familie"))

        with self.assertRaises(Exception):
            self.repo.add_contact(Contact(5,"Maria","121a123","Job"))

    def test_verify_name(self):
        with self.assertRaises(Exception):
            self.repo.add_contact(Contact(2,"Raul","123","Job"))

    def test_verify_id(self):
        with self.assertRaises(Exception):
            self.repo.add_contact(Contact(1,"Mario","1234","Job"))

    def test_find_number(self):
        self.assertEqual(self.repo.find_number("Raul"),"0898311331")

class ServiceTests(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()
        self.repo = RepositoryContact("test_contact.txt")
        self.serv = Service(self.repo,self.validator)
    def tearDown(self):
        with open("test_service.txt","w") as f:
            f.write("1,Raul,0898311331,Familie")

    def test_add(self):
        with self.assertRaises(ContactError):
            self.serv.add_contact(2,"Raul","123","Job")
        with self.assertRaises(ContactError):
            self.serv.add_contact(1,"Mario","123","Familie")

    def test_find_number(self):
        self.assertEqual(self.serv.find_number("Mario"),"Nu exista in contacte")
        self.assertEqual(self.serv.find_number("Raul"),"0898311331")

    def test_filter_by_group(self):
        self.serv.add_contact(2,"Marian","1234555","Familie")
        self.serv.add_contact(3,"Maria","1234","Familie")
        self.serv.add_contact(4,"Marcel","12345","Job")
        lista = self.serv.filter_by_group("Familie")
        self.assertEqual(len(lista),3)
        self.assertEqual(lista[0].name,"Maria")
        self.assertEqual(lista[1].name,"Marian")
        self.assertEqual(lista[2].name,"Raul")



if __name__ == '__main__':
    unittest.main()