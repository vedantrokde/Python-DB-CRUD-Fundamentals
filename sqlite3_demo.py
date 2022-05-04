import sqlite3


def create_table():
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books (item TEXT, quantity INTEGER, price REAL);"
    )
    conn.commit()


def insert_book(item, quantity, price):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books (item, quantity, price) VALUES (?,?,?)",
        (item, quantity, price),
    )
    conn.commit()


def update_book(item, quantity, price):
    cur = conn.cursor()
    cur.execute(
        "UPDATE books SET quantity=?, price=? WHERE item=?;", (quantity, price, item)
    )
    conn.commit()


def delete_book(item):
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE item=?;", (item,))
    conn.commit()


def view_books():
    cur = conn.cursor()
    cur.execute("SELECT * FROM books;")
    rows = cur.fetchall()
    conn.commit()
    return rows


def drop_books():
    cur = conn.cursor()
    cur.execute("DROP TABLE books;")
    conn.commit()


conn = sqlite3.connect("db.sqlite3")

create_table()

insert_book("Wine Glass", 38, 10.5)
insert_book("Book with thing", 14, 24.4)
insert_book("Value of money", 23, 17.2)
print("\nBooks in db after inserting:\n", view_books())

update_book("Wine Glass", 12, 14.6)
print("\nBooks in db after updating:\n", view_books())

delete_book("Wine Glass")
print("\nBooks in db after deleting:\n", view_books())

drop_books()
print("\nBooks were dropped!")

conn.close()
