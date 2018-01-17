

import sqlite3

def createDatabase(createSql):
    with sqlite3.connect("ShoeStore.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(createSql)
        myDatabase.commit()



createSql = """CREATE TABLE `Customer` ( `CustomerID` INTEGER, `Name` TEXT, `DateOfBirth` TEXT, `Address` TEXT, `Phone` INTEGER, PRIMARY KEY(`CustomerID`) )"""

createDatabase(createSql)
