from UI.ui import Console
from repository.repo import RepoMagazin
from Service.service import Service

def main():
    repo = RepoMagazin("data.txt")
    service = Service(repo)
    ui = Console(service)
    ui.run()

if __name__ == '__main__':
    main()