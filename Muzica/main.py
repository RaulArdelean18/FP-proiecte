from Repository.repo import MusicRepo
from Services.service import MuzicaService
from UI.ui import Console

def main():
    repo = MusicRepo("muzica.txt")
    srv = MuzicaService(repo)
    ui = Console(srv)
    ui.run()

if __name__ == "__main__":
    main()