
class Fractional:
    def __init__(self, licznik, mianownik):
        if mianownik == 0:
            raise ValueError("Mianownik nie może być zerem!")

        # przenosimy znak do licznika -> mianownik dodatni
        if mianownik < 0:
            licznik = -licznik
            mianownik = -mianownik
        # skracamy ułamek (np. 2/4 = 1/2)
        g = self.najwiekszy_wspolny_dzielnik(abs(licznik), abs(mianownik))
        self.licznik = licznik // g #// umożliwia dzielenie zwracajac tylko część cąłkowitą, zaokragla wynik w dół
        self.mianownik = mianownik // g

    #tekstowa reprezentacja obiektu klasy:
    def __str__(self):
        return f"{self.licznik}/{self.mianownik}"

    #najwiekszy wspolny dzielnik do skracania ulamkow
    def najwiekszy_wspolny_dzielnik(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    #konwersja liczby int na ulamek, ulamek zostawia bez zmian, inny typ zglasza blad
    def konwertuj_ulamek(self, value):
        if isinstance(value, Fractional): #sprawdza czy value jest obiktem klasy Fractional
            return value
        elif isinstance(value, int):
            return Fractional(value, 1)
        else:
            raise TypeError("Obsługiwane są tylko ulamki i int")


    #operacje matematyczne na ulamkach
    def __add__(self, other):
        other = self.konwertuj_ulamek(other)
        new_licznik = self.licznik * other.mianownik + other.licznik * self.mianownik
        new_mianownik = self.mianownik * other.mianownik
        return Fractional(new_licznik, new_mianownik)

    def __sub__(self, other):
        other = self.konwertuj_ulamek(other)
        new_licznik = self.licznik * other.mianownik - other.licznik * self.mianownik
        new_mianownik = self.mianownik * other.mianownik
        return Fractional(new_licznik, new_mianownik)

    def __mul__(self, other):
        other = self.konwertuj_ulamek(other)
        return Fractional(self.licznik * other.licznik,
                          self.mianownik * other.mianownik)

    def __truediv__(self, other):
        other = self.konwertuj_ulamek(other)
        if other.licznik == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero!")
        return Fractional(self.licznik * other.mianownik,
                          self.mianownik * other.licznik)

    #czy jest równe ==
    def __eq__(self, other):
        other = self.konwertuj_ulamek(other)
        return (self.licznik == other.licznik and
                self.mianownik == other.mianownik)
    #czy jest mniejsze od <
    def __lt__(self, other):
        other = self.konwertuj_ulamek(other)
        return self.licznik * other.mianownik < other.licznik * self.mianownik

#Przykład użycia

if __name__ == "__main__": # pragma: no cover
    #Tworzenie obiektów ułamków
    a = Fractional(1, 2)
    b = Fractional(3, 4)
    c = Fractional(2, 4)

    print("Ułamki:")
    print("a =", a)
    print("b =", b)
    print("c =", c)

    #Operacje matematyczne
    print("\nOperacje:")
    print("a + b =", a + b)
    print("a - b =", a - b)
    print("a * b =", a * b)
    print("a / b =", a / b)

    # Porównania
    print("\nPorównania:")
    print("a == c:", a == c)
    print("a < b:", a < b)
    print("b < a:", b < a)


