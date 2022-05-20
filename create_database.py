import sqlite3


def create_db():
    con = sqlite3.connect(r'system.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, name text, email text, gender text, contact text, dob text, doj text, password text, type text, address text, salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name text, contact text, desc text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS category(id INTEGER PRIMARY KEY AUTOINCREMENT, name text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS product(id INTEGER PRIMARY KEY AUTOINCREMENT, category text, supplier text, name text, price text, qty text, status text)")
    con.commit()


create_db()
