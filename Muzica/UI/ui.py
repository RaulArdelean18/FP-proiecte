from Services.service import MuzicaError


class Console:
    def __init__(self,srv):
        self.__srv = srv

    def run(self):
        while True:
            print("\n 1. Modify | 2. Random generator | 3. Export | 4. Exit")
            op = input()

            try:
                if op == "1":
                    titlu = input("Titlu: ")
                    artist = input("Artist: ")
                    gen = input("Gen: ")
                    durata = int(input("Durata: "))
                    self.__srv.modify(titlu,artist,gen,durata)
                    print("S-a modificat piesa")
                elif op=="2":
                    n = int(input("Cate piese vrei sa generezi: "))
                    self.__srv.add_random(n)
                    print("S-au pus n piese random")
                elif op=="3":
                    filename = input("Unde vrei sa dai export: ")
                    self.__srv.export_file(filename)
                    print(f"S-a dat export in file-ul {filename}")
                elif op=="4":
                    break
                else:
                    print("Optiune invalida")
            except MuzicaError as e:
                print(f"\n[Error] {e}")
            except ValueError:
                print(f"\n[Error] Data introdusa nu este un numar")
