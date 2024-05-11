import csv
from datetime import datetime
def checkid(aID):
    """
       Sprawdza, czy identyfikator klienta istnieje w bazie danych klientów.

       Argumenty:
           aID (int): Identyfikator klienta do sprawdzenia.

       Zwraca:
           bool: True, jeśli identyfikator klienta istnieje w bazie danych, False w przeciwnym razie.

       Przykład użycia:
           >>> checkid(12345)
           Witamy ponownie!
       """
    with open("Library/customer.csv", mode="r") as csv_file:
        checkifclientindatabase = csv.reader(csv_file)
        next(checkifclientindatabase)  # pominięcie pierwszego wiersza (nagłówka)
        datatocheck = list(checkifclientindatabase)
        clientinbase = False
        for row in datatocheck:
            if(int(row[0])==aID):
                clientinbase=True
                break
        if(clientinbase):
            print("Witamy ponownie!")
            return True
        if(not clientinbase):
            print("Nie jestes w bazie uzytkownikow!")
            return False
def borrowabook(aID,abookID):
    """
       Wypożycza książkę z biblioteki i aktualizuje rekord książek klienta.

       Argumenty:
           aID (int): Identyfikator klienta.
           abookID (int): Identyfikator książki do wypożyczenia.

       Przykład użycia:
           >>> borrowabook(12345, 9876)
           Książka istnieje i zostaje wypożyczona!

       Uwagi:
           - Funkcja wymaga wcześniejszego wywołania funkcji checkid(aID) w celu sprawdzenia, czy klient istnieje w bazie danych.
           - Książka zostaje usunięta z bazy danych książek (plik "book.csv") i dodana do pliku klienta o nazwie "{id_str}.csv".
           - W pliku klienta zostaje zapisana data wypożyczenia jako aktualny czas.
           - Jeśli książka o podanym identyfikatorze nie istnieje, zostanie wyświetlony komunikat "Nie znaleziono takiej książki".
           - Po zaktualizowaniu bazy danych książek, plik "book.csv" zostaje nadpisany zaktualizowanymi danymi.

       Wyjątki:
           FileNotFoundError: Wyrzucany, gdy plik "Library/customer.csv" lub "Library/book.csv" nie istnieje.
           ValueError: Wyrzucany, gdy podane identyfikatory klienta lub książki nie są liczbami.

       """
    id_str = str(aID)
    now = datetime.now()
    created = now.strftime("%Y-%m-%d %H:%M:%S")
    if_find_book=False
    with open("Library/book.csv",mode="r") as csv_file:
        bookreader=csv.reader(csv_file)
        next(bookreader)
        booksdata=list(bookreader)
        for i,row in enumerate(booksdata):
            if(int(row[0])==abookID):
                if_find_book=True
                book=booksdata.pop(i)
                row[5]=created
                with open(f"DATABASE/{id_str}.csv", mode="a", newline="") as client_file:
                    clientbook = csv.writer(client_file)
                    clientbook.writerow(book)
                print("Ksiazka istnieje i wypozyczam!")
                break
    if not if_find_book:
        print("Nie znaleziono takiej ksiazki")
    with open("Library/book.csv", mode="w", newline="") as csv_file:
        bookwriter = csv.writer(csv_file)
        bookwriter.writerow(["ID", "AUTHOR", "TITLE", "PAGES", "CREATED", "UPDATED"])
        bookwriter.writerows(booksdata)




