import sqlite3

def insertDataIntoTable(dbName, item, sql):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        cursor.execute(sql, item)
        db.commit()

#item = ("Ryan Harris", "5011, Oslo", 4241414146, "Ryan.Harris", "12345", 1, 2)
sql = 'INSERT INTO CUSTOMER (Name, Address, Phone, UserName, Password, PaymentTypeId, MembershipId ) VALUES (?, ?, ?, ?, ?, ?, ?)'
item = ("Dinesh", "Folkeuniversitet", 123457895, "dinesh", "helloWorld", 5, 9)
insertDataIntoTable("EspressoHouse.db", item)


