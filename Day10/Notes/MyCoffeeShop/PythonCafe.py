import sqlite3
import cherrypy
from cherrypy import expose

DB_NAME = "PythonCafe.db"


def insertDataIntoTable(dbName, item, sql):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        cursor.execute(sql, item)
        db.commit()

def readTableItems(dbName):
    with sqlite3.connect(dbName) as db:
        cursor = db.cursor()
        sql = 'SELECT * FROM Product'
        cursor.execute(sql)
        items = cursor.fetchall()
        print(items)
        db.commit()
        return items

class PythonCafe:

    @expose
    def index(self):
        return open('HomePage.html')

    @expose
    def home(self, action):
        if action == 'Create Product':
            return open('NewProduct.html')
        if action == 'Create Customer':
            return open('NewCustomer.html')
        if action == 'Get Products':
            return print(readTableItems(DB_NAME));
        return

    @expose
    def makeNewProduct(self, inputName, inputPrice, availability, description, sizeId, productTypeID):
        # read the posted values from the UI
        sql = 'INSERT INTO PRODUCT (Name, Price, Availability, Description, SizeId, ProductTypeId) VALUES (?, ?, ?, ?, ?, ?)'
        item = (inputName, inputPrice, availability, description, sizeId, productTypeID)
        print(item)
        insertDataIntoTable(DB_NAME, item, sql)
        return open('NewProduct.html')


    @expose
    def makeNewCustomer(self, name, email, phone, userName, password, paymentMode, address, membershipId):
        # read the posted values from the UI
        sql = 'INSERT INTO CUSTOMER (Name, Email, Phone, UserName, Password, PaymentMode, Address, MembershipId) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        item = (name, email, phone, userName, password, paymentMode, address, membershipId)
        print(item)
        insertDataIntoTable(DB_NAME, item, sql)
        return open('NewCustomer.html')


cherrypy.quickstart(PythonCafe())
