import sqlite3
import cherrypy
from cherrypy import expose
from cherrypy import request

DB_NAME = "PythonCafe.db"


def insertDataIntoTable(dbName, item, sql):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        cursor.execute(sql, item)
        db.commit()

class PythonCafe:

    @expose
    def index(self):
        return open('NewProduct.html')

    @expose
    def makeNewCustomer(self, inputName, inputPrice, availability, description, sizeId, productTypeID):
        # read the posted values from the UI

        sql = 'INSERT INTO PRODUCT (Name, Price, Availability, Description, SizeId, ProductTypeId) VALUES (?, ?, ?, ?, ?, ?)'
        item = (inputName, inputPrice, availability, description, sizeId, productTypeID)
        print(item)
        # item = ("Dinesh", "Folkeuniversitet", 123457895, "dinesh", "helloWorld", 5, 9)
        insertDataIntoTable(DB_NAME, item, sql)
        return open('NewProduct.html')


cherrypy.quickstart(PythonCafe())
