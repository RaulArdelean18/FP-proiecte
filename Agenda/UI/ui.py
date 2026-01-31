class Console:
    def __init__(self,service):
        self.__service = service

    def __add_contact(self):
        id = int(input("ID: "))
        nume = input("Nume: ")
        nr_telefon = input("nr telefon: ")
        grup = input("Grup: ")

        self.__service.add_contact(id,nume,nr_telefon,grup)
        print("S-a adaugat cu succes")

    def __find_number_by_a_name(self):
        nume = input("Nume: ")
        nr_telefon = self.__service.find_number(nume)
        print(f"{nr_telefon}")

    def __print_from_group(self):
        grup = input("Grup: ")
        lista = self.__service.filter_by_group(grup)

        if lista is None:
            print("No contact found")
        else:
            for contact in lista:
                print(str(contact))

    def __export(self):
        grup = input("Grup: ")
        filename = input("filename: ")
        lista = self.__service.export_by_group(grup)
        with open(filename,"w+") as f:
            for contact in lista:
                f.write(f"{contact.name},{contact.nr_telefon}\n")


    def run(self):
        while True:
            print("\n 1. Add contacte | 2. Find number | 3. Print all contacts from a group sorted by names | 4. Export | 5. Exit")
            choice = input("Enter your choice: ")
            try:
                if choice == "1":
                    self.__add_contact()
                elif choice == "2":
                    self.__find_number_by_a_name()
                elif choice == "3":
                    self.__print_from_group()
                elif choice == "4":
                    self.__export()
                elif choice == "5":
                    break
                else:
                    print("Optiune invalida")
            except Exception as e:
                print(f"[Error] {e}")