from UI.ui import Console
from repository.repo import RepoMagazin
from Service.service import Service
from validator.validator import ValidatorMagazin

def main():
    repo = RepoMagazin("data.txt")
    validator = ValidatorMagazin()
    service = Service(repo,validator)
    ui = Console(service)
    ui.run()

if __name__ == '__main__':
    main()