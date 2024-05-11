import customerservice
import Bookservice
import Borrowingabook
def logintoSystem():
    """
       Pozwala użytkownikowi zalogować się do systemu jako Klient lub Admin.

       Umożliwia wykonanie różnych operacji, takich jak dodawanie klienta, usuwanie klienta,
       dodawanie nowej książki do bazy, rejestracja nowego klienta, wypożyczanie książek,
       wyświetlanie wypożyczonych książek i zwracanie książek.

       W przypadku błędu wartości lub nieznanej wyjątkowej sytuacji, funkcja wyświetla odpowiedni komunikat.

       Przykład użycia:
           >>> logintoSystem()
           Klient
           Admin
           Wybierz konto na które chcesz się zalogować: Admin
           Prosze podac haslo: 123
           Witamy w panelu admina!
           1. Dodaj klienta
           2. Usun klienta
           3. Dodaj nowa ksiazke do bazy
           Wybierz opcje 1, 2 lub 3: 1
           ...

       Wyjątki:
           ValueError: Wyrzucany, gdy podana opcja wyboru jest niepoprawna.
           Exception: Wyrzucany, gdy wystąpi nieznany błąd.

       Uwagi:
           - Wartość hasła jest ustawiona na stałe (123) dla uproszczenia.
           - Funkcja korzysta z innych modułów i funkcji, takich jak `customerservice.addCustomer()`,
             `customerservice.removeCustomer()`, `Bookservice.addnewBook()`, `customerservice.registrationofanewClient()`,
             `Borrowingabook.checkid()`, `Bookservice.showBooks()`, `Bookservice.showlendBooks()`,
             `Bookservice.returnBook()`, które muszą być zdefiniowane wcześniej.

       """
    try:
        print("Klient")
        print("Admin")
        choice = str(input("Wybierz konto na ktore chcesz sie zalogowac: "))
        password = 123
        if (choice == "Admin"):
            password_check = int(input("Prosze podac haslo: "))
            if (password_check == 123):
                print("Witamy w panelu admina!")
                print("1.Dodaj klienta")
                print("2.Usun klienta")
                print("3.Dodaj nowa ksiazke do bazy")
                choice1 = int(input("Wybierz opcje 1,2 lub 3: "))
                if (choice1 == 1):
                    customerservice.addCustomer()
                elif (choice1 == 2):
                    customerservice.removeCustomer()
                elif (choice1 == 3):
                    Bookservice.addnewBook()
                else:
                    raise ValueError("Niepoprawna opcja wyboru")
        elif (choice == "Klient"):
            print("Witamy w bibliotece!")
            print("1.Zarejestruj sie")
            print("2.Wypozycz ksiazke")
            print("3.Pokaz swoje wypozyczone ksiazki")
            print("4.Zwroc ksiazke")
            choice_client = int(input("Wybierz opcje: "))
            if (choice_client == 1):
                customerservice.registrationofanewClient()
            elif choice_client == 2:
                client_id = int(input("Wpisz swoje ID, jeśli jesteś w bazie: "))
                if Borrowingabook.checkid(client_id):
                    Bookservice.showBooks()
                    book_ids = input("Podaj ID książek, które chcesz wypożyczyć, oddzielone przecinkami: ").split(",")
                    book_ids = [int(id.strip()) for id in book_ids]
                    Borrowingabook.borrowabook(client_id, book_ids)
            elif(choice_client==3):
                client_id_2 = int(input("Wpisz swoje ID,jesli jestes w bazie: "))
                if(Borrowingabook.checkid(client_id_2)==True):
                    Bookservice.showlendBooks(client_id_2)
            elif(choice_client==4):
                client_id_3 = int(input("Wpisz swoje ID,jesli jestes w bazie: "))
                if (Borrowingabook.checkid(client_id_3)==True):
                    Bookservice.showlendBooks(client_id_3)
                    print("Ktora ksiazke chcesz zwrocic?")
                    zwrot = int(input("Wpisz ID ksiazki ktora chcesz zwrocic: "))
                    pomoc = int(client_id_3)
                    pomoc2 = int(zwrot)
                    Bookservice.returnBook(pomoc,pomoc2)
            else:
                raise ValueError("Niepoprawna opcja wyboru")
    except ValueError as ve: #niepoprawny typ zmiennej
        print("Wystąpił błąd: ", ve)
    except Exception as e:   #nie da sie opisac
        print("Wystąpił nieznany błąd: ", e)
        "Funkcja logintoSystem() do logowania się do systemu bibliotecznego." \
        "W zależności od wyboru użytkownika (klient lub admin), funkcja wyświetla opcje dostępne dla danego konta." \
        "Po podaniu poprawnego hasla logujemy sie na konto admina, admin może wykonać opcje związane z obsługą klientów (dodawanie/usuwanie klientów) oraz książek." \
        "Dla klienta dostępne są opcje związane z rejestracją nowego klienta, wypożyczeniem książki, wyświetleniem listy wypożyczonych książek oraz zwrotem książki." \
        "Funkcja korzysta z modułów customerservice, Bookservice i Borrowingabook, które zawierają metody odpowiedzialne za obsługę klientów, książek oraz wypożyczeń." \
        "W przypadku wystąpienia błędów, program wyświetla odpowiedni komunikat."""




