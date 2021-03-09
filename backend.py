import sqlite3

def connect():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, genre text, page integer )")
    conn.commit()
    conn.close()

#This function insert element to database by given title, author, genre, page
def insert(title, author, genre, page):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title, author, genre, page))
    conn.commit()
    conn.close()

#This function will return database's rows as tuples in list
def view():
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

#This function will search given title/author/genre/page in database
def search(title="", author="", genre="", page=""):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book wHERE title=? OR author=? OR genre=? OR page=?", (title, author, genre, page))
    rows = cur.fetchall()
    conn.close()
    return rows

#This function will delete the element on given id. 
def delete(id):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

#This function will update the element on database based on given title, author, genre, page
def update(id, title, author, genre, page):
    conn=sqlite3.connect("book.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, genre=?, page=? WHERE id=?", (title, author, genre, page,id))
    conn.commit()
    conn.close()

connect()


