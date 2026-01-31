from Repository.repo import JucatorRepo
from Service.service import ServiceJucator
from UI.console import Console
from Validator.validator import JucatorValidator

def main():
    repo = JucatorRepo("data.txt")
    validator = JucatorValidator(repo)
    service = ServiceJucator(repo,validator)
    ui = Console(service)
    ui.run()

if __name__ == "__main__":
    main()