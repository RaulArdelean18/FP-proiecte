from UI.ui import Console
from Repository.repo import PiesaRepo
from Services.service import PiesaService

def main():
    repo = PiesaRepo("piese.txt")
    srv = PiesaService(repo)
    ui = Console(srv)
    ui.run()

if __name__ == "__main__":
    main()