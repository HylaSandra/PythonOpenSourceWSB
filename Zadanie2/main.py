
class Timetable:

    def __init__(self, bus, stop, day, hour):
        self.bus = bus
        self.stop = stop
        self.day = day
        self.hour = hour

    def rozklad(self):
        print(f"Linia: {self.bus}")
        print(f"Przystanek: {self.stop}")
        print(f"Dni kursów: {self.day}")
        print(f"Godziny odjazdu: {self.hour}")


class Bus:

    def __init__(self, name):
        self.name = name


class Passenger:

    def __init__(self, name, discount):
        self.name = name
        self.discount = discount

    def wydrukuj(self):
        print(f"Imię: {self.name}")
        print(f"Zniżka: {self.discount}")


class Ticket:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def cena(self):
        print(f"Nazwa: {self.name}")
        print(f"Cena: {self.price}")


tt1 = Timetable('1', 'Pętla', 'Tylko dni robocze',' ')
tt2 = Timetable('2', 'Centrum', 'Codziennie',' ')
b1 = Bus('1')
b2 = Bus('2')
p1 = Passenger('Krzysztof Krawczyk', 'tak')
p2 = Passenger('Edyta Górniak', 'nie')
t1 = Ticket('normalny', 4)
t2 = Ticket('ulgowy', 2)


b = input('* Wybierz linię [1/2]: ')
if "1" in b:
    print("* Rozkład jazdy:")
    tt1.rozklad()
    i = 7
    while i < 20:
        i += 1
        if i == 20:
            continue
        print(i, end=":00 | ")
elif "2" in b:
    print("* Rozkład jazdy:")
    tt2.rozklad()
    g = [10, 11, 12, 13, 14, 15, 16, 17, 18, 18, 20]
    m = [30, "00"]

    for godzina in g:
        for minuta in m:
            print(godzina, ":", minuta, "| ", end="")
else:
    print('Nie znaleziono linii')

print("\n___")
p = input('* Wybierz pasażera [1/2]: ')
print("* Pasażer to: ")
if "1" in p and 'tak' in p1.discount:
    p1.wydrukuj()
elif "2" in p and 'nie' in p2.discount:
    p2.wydrukuj()
else:
    print('Nie znaleziono pasażera')
print("___")
t = input("Sprawdź cenę biletu. Czy dla tego pasażera przysługuje zniżka [tak/nie]? ")
if "tak" in t:
    print("* Bilet przysługujący pasażerowi:")
    t2.cena()
elif "nie" in t:
    print("* Bilet przysługujący pasażerowi:")
    t1.cena()
else:
    print("wprowadzono nieprawidłową wartość.")


