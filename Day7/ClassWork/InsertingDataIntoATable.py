


import sqlite3

def insertIntoTable(insertSql):
    with sqlite3.connect("ShoeStore.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(insertSql)
        myDatabase.commit()

insertQuery = """INSERT INTO Customer VALUES (1, "Dinesh", "01.01.1988", "5555, Bergen", 45454545)"""

insertIntoTable(insertQuery)
