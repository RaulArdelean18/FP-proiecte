from Service.service import CartiService
from Repository.Repo import CartiRepo
from UI.ui import Console
from Teste.teste import Teste


def main():
    try:
        tester = Teste()
        tester.teste_all()
        print("Testele au rulat!\n")
    except AssertionError as e:
        print("Testele au puscat!")
        return
    repo = CartiRepo("data.txt")
    service = CartiService(repo)
    ui = Console(service)
    ui.run()

if __name__ == "__main__":
    main()