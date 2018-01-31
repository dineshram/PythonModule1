import sqlite3

def readTableItems(dbName):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        sql = 'SELECT * FROM Customer'
        cursor.execute(sql)
        items = cursor.fetchall()
        print(items)
        db.commit()

readTableItems("EspressoHouse.db")
