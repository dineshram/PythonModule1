#https://pythonschool.net/databases/introduction-to-databases/


import sqlite3

#Creating a new, blank database in Python using SQLite
with sqlite3.connect('example.db') as db:
    pass

def createDatabase(dbName, sql):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()


sql = """CREATE TABLE Product(
    ProductID integer,
    Name text,
    Price real,
    Primary Key(ProductID))"""

createDatabase("restaurant.db", sql)
