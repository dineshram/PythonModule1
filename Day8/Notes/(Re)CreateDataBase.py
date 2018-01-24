

import sqlite3

def createDatabase(dbName, createSql, tableName):
    with sqlite3.connect(dbName) as myDatabase:
        cursor = myDatabase.cursor()
        #findIfExistsQuery = "SELECT name FROM sqlite_master WHERE name='" + tableName + "'"
        #https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
        cursor.execute("SELECT name FROM sqlite_master WHERE name=?", (tableName,))
        result = cursor.fetchall()
        keepTable = True
        if (len(result) == 1):
            response = input("The table {0} already exists. Do you want to recreate it? (y/n):" .format(tableName))
            if(response == "y"):
                keepTable = False
                print("The table ", tableName, " will be recreated and all existing data will be lost")
                cursor.execute("DROP TABLE {0}" .format(tableName))
                myDatabase.commit()
            else:
                print("The table ", tableName, " will be kept intact")
        else:
            keepTable = False

        if not keepTable:
            cursor.execute(createSql)
            myDatabase.commit()


createSql = """CREATE TABLE `Customer` ( `CustomerID` INTEGER, `Name` TEXT, `DateOfBirth` TEXT, `Address` TEXT, `Phone` INTEGER, PRIMARY KEY(`CustomerID`) )"""

createDatabase("ShoeStore.db", createSql, "Customer")
