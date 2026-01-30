from Repository.repo import EmisiuneRepo
from Services.service import EmisiuneService, EmisiuneError
from UI.ui import Console

def test_stergere():
    repo = EmisiuneRepo("test.txt")
    srv = EmisiuneService(repo)
    try:
        srv.sterge_emisiune("Inexistent", "Tip")
        assert False
    except EmisiuneError as e:
        assert str(e) == "Avertisment: Emisiunea nu există!"  #

    srv.blocheaza_tipuri("Stiri")
    try:
        srv.sterge_emisiune("Orice", "Stiri")
        assert False
    except EmisiuneError as e:
        assert str(e) == "emisiune blocată"  #

def main():
    test_stergere()
    repo = EmisiuneRepo("emisiuni.txt")
    srv = EmisiuneService(repo)
    ui = Console(srv)
    ui.run()

if __name__ == "__main__":
    main()