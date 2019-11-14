# Zadanie 1) Napisz program, który poda statystki dowolnego tekstu pobranego z pliku, wypisze takie dane jak:
# ilość użyć poszczególnych literek i cyfr, ilość wyrazów, zdań etc.
# Niech program tworzy też plik ze statystyką swojej pracy.

num_lines = 0
num_words = 0
num_chars = 0
num_a = 0
num_z = 0
num_space = 0
num_et = 0
num_open = 0

# Statystyki pliku tekstowego lipsum.txt:
with open("lipsum.txt", "r") as file:
    # iteracji w for będzie tyle, ile linii w pliku tekstowym
    for line in file:
        # tworzy liste słów dla każdej kolejnej linii
        word_list = line.split()
        num_lines += 1
        num_words += len(word_list)  # ilosc wyrazow to dlugosc listy słów
        num_chars += len(line)  # liczba znakow to suma ilości znakow w linii z kazdej iteracji
        # liczy od 0, wiec jest roznica 1 w porownaniu do liczenia od 1
        num_a += line.count("a")
        num_z += line.count("z")
        num_space += line.count(" ")
        num_et += line.count("et")
results = (f"\nNumber of lines: {num_lines} \nNumber of words: {num_words} "
           f"\nNumber of characters: {num_chars} \nNumber of letters a: {num_a} \nNumber of letters z: {num_z} "
           f"\nNumber of spaces: {num_space} \nNumber of word et: {num_et}")

# Statystyki programu: licznik uruchomień
# Prawdopodobnie moj licznik wyzeruje się po 99 uruchomieniu ;)
with open("test.txt", "r+") as file:
    file.seek(0)
    num_open = file.readline()
    # wyciąga znaki 20 i 21, zapisuje jako integer, żeby móc dodać do tej wartości 1 za każdym uruchomieniem programu
    num_open = int(num_open[20:22]) + 1

statistics = f"Number of openings: {num_open}"
# test czy bedzie zapisywac:
# file.seek(0)
# file.write(f"Number of openings: {num_open} \n")
# print(f"Number of openings: {num_open} \n")

print(f"{statistics}{results}")

# Zapisanie wyników w pliku tekstowym test.txt:
with open("test.txt", "w") as file:
    file.seek(0)
    file.write(statistics + results)





