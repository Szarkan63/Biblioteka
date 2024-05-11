import customerservice
from datetime import datetime
import csv
import os
def addnewBook():
    bookid = input("Podaj ID książki: ")
    author = input("Podaj autora: ")
    title=input("Podaj tytul: ")
    pages = int(input("Podaj liczbę stron: "))
    now = datetime.now()
    created = now.strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists("Library/book.csv"):
        with open("Library/book.csv", mode="a", newline="") as csv_file:
            bookdefaultdata = csv.writer(csv_file)
            bookdefaultdata.writerow(["ID", "AUTHOR", "TITLE", "PAGES", "CREATED", "UPDATED"])
    with open("Library/book.csv", mode="a", newline="") as csv_file:
        bookdata = csv.writer(csv_file)
        bookdata.writerow([bookid, author, title, pages, created, created])
        print("Pomyślnie dodano nową książkę")


def showBooks():
    with open("Library/book.csv", mode="r", newline="") as csv_file:
        bookdata = csv.reader(csv_file)
        next(bookdata)
        bookdataread=list(bookdata)
        for book in bookdataread:
            print(" | ".join(book))

def showlendBooks(aID):
    id_str = str(aID)
    with open(f"DATABASE/{id_str}.csv", mode="r", newline="") as client_file:
        bookdata = csv.reader(client_file)
        next(bookdata)
        bookdataread = list(bookdata)
        if not bookdataread:
            print("Nie masz wypożyczonych książek.")
        else:
            for book in bookdataread:
                print(" | ".join(book))
def returnBook(aID, abookID):
    now = datetime.now()
    updated = now.strftime("%Y-%m-%d %H:%M:%S")
    id_str = str(aID)
    try:
        book_id = int(abookID)
    except ValueError:
        print("Invalid book ID")
        return
    with open(f"DATABASE/{id_str}.csv", mode="r") as csv_file:
        client_reader = csv.reader(csv_file)
        next(client_reader)
        client_books = list(client_reader)
        for i, row in enumerate(client_books):
            if int(row[0]) == book_id:
                row[5] = updated
                with open("Library/book.csv", mode="a", newline="") as book_file:
                    book_writer = csv.writer(book_file)
                    book_writer.writerow([book_id, row[1], row[2], row[3], row[4], updated])
                print("Książka zwrócona pomyślnie.")
                break
        else:
            print("Nie znaleziono takiej książki na Twoim koncie.")
            return
    with open(f"DATABASE/{id_str}.csv", mode="w", newline="") as csv_file:
        client_writer = csv.writer(csv_file)
        client_writer.writerow(["ID", "AUTHOR", "TITLE", "PAGES", "CREATED", "UPDATED"])
        client_writer.writerows(client_books)



