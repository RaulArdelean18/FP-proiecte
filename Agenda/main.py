from Repository.repo import RepositoryContact
from Service.service import Service
from UI.ui import Console
from validator.validator import Validator

def main():
    repo = RepositoryContact("date.txt")
    validator = Validator()
    serv = Service(repo,validator)

    ui = Console(serv)
    ui.run()

if __name__ == "__main__":
    main()