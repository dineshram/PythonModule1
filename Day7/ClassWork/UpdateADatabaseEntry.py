import sqlite3

def updateTable(updateSql):
    with sqlite3.connect("ShoeStore.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(updateSql)
        myDatabase.commit()

updateSql = "UPDATE Customer SET Phone = 789456123 WHERE CustomerID=1"

updateTable(updateSql)
