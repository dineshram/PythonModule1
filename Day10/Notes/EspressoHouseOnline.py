
import os, os.path
import random
import string

import sqlite3
import cherrypy
from cherrypy import expose

def databaseInsert(sqlStatement):
    with sqlite3.connect("expressoHouse.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(sqlStatement)
        myDatabase.commit()
        pass

def databaseExtract(sqlStatement):
    with sqlite3.connect("expressoHouse.db") as myDatabase:
        cursor = myDatabase.cursor()
        cursor.execute(sqlStatement)
        myDatabase.commit()
        rows = list(cursor.fetchall())
        print(rows)
        return rows
        pass

head = """<head>
                    <title>ExpressoHouse</title>
                     <link href="/static/css/style.css" rel="stylesheet">
                </head>"""
top = """"""
bottom = """        <form method="get" action="index">
                      <button type="submit">Back to front menu!</button>
                    </form>"""
productButton = """        <form method="get" action="products">
                      <button type="submit">Back to product menu!</button>
                    </form>"""

class ExpressoHouse():
    #decorate the function
    @expose
    def index(self):
        return """<html>
                """,head,"""
                  <body>
                    <div>Welcome to Expresso House</div>
                    <br /> 
                    <form method="get" action="addOrder">
                      <button type="submit">Adding new order!</button>
                    </form>
                    <br /> 
                    <form method="get" action="showCustomers">
                      <button type="submit">Show customers!</button>
                    </form>
                    <br /> 
                    <form method="get" action="addCustomerForm">
                      <button type="submit">Adding new customer!</button>
                    </form>
                    <br /> 
                    <form method="get" action="searchCustomers">
                      <button type="submit">Search customers!</button>
                    </form>
                    <br /> 
                    <form method="get" action="products">
                      <button type="submit">Products!</button>
                    </form>
                    <br /> 
                    <br /> 
                  </body>
                </html>"""

    @expose()
    def addOrder(self):
        return("Creating a order")

    @expose
    def addCustomerForm(self):
        paymentSQL = """SELECT * FROM PaymentType"""
        paymentType = databaseExtract(paymentSQL)
        payment = ""
        for i in range(0, len(paymentType)):
            pay = paymentType[i][1]
            payment = payment + "<option value='"+pay+"'>"+pay+"</option>"
        membershipSQL = """SELECT * FROM Membership"""
        membershipType = databaseExtract(membershipSQL)
        membership = ""
        for i in range(0, len(membershipType)):
            member = membershipType[i][1]
            membership = membership + "<option value='"+member+"'>"+member+"</option>"
        return """<html>
                """,head,"""
                  <body>
                    <div>Welcome to Expresso House</div>
                    <br /> 
                    <form method="get" action="addCustomer">
                        <input type="text" value="Customer Name" name="personName" /><br/>
                        <input type="text" value="Customer Adress" name="adress" /><br/>
                        <input type="text" value="Customer Phone" name="phone" /><br/>
                        <input type="text" value="Customer Username" name="username" /><br/>
                        <input type="text" value="Customer Password" name="password" /><br/>
                        <select name="paymentTypeid">"""+payment+"""</select><br/>   
                        <select name="membershipid">"""+membership+"""</select><br/>  
                      <button type="submit">Adding new customer!</button>
                    </form>
                    <br /> 
                  </body>"""+bottom+"""
                </html>"""

    @expose()
    def addCustomer(self,personName, adress, phone, username, password, paymentTypeid, membershipid):
        name = personName
        customer = """INSERT INTO Customer (Name, Adress, Phone, Username, Password, PaymentTypeid, Membershipid) VALUES (\""""+name+"""\",\""""+adress+"""\","""+phone+""", \""""+username+"""\",\""""+password+"""\",1,1)"""
        print(customer)
        databaseInsert(customer)
        pass
        return "Customer added"

    @expose()
    def showCustomers(self):
        showCustomer = """SELECT c.Customerid, c.Name, c.Adress, c.Phone, c.Username, p.NameOfPayment, m.MembershipName from Customer c JOIN Membership m ON c.MembershipID = m.Membershipid JOIN PaymentType p ON c.PaymentTypeID=p.PaymentTypeid"""
 #       showCustomer = """SELECT c.Customerid, c.Name, c.Adress, c.Phone, c.Username from Customer c """
        print(showCustomer)
        showCust = databaseExtract(showCustomer)
        table = ""
        for i in range(0, len(showCust)):
            table = table+ "<tr>"
            for j in range(0, 1):
                tableContent = str(showCust[i][j])
                table = table + """<th><a href="./showCustomer?Customerid="""+tableContent+"""">"""+tableContent+"""</a></p></th>"""
            for j in range(1, len(showCust[i])):
                tableContent = str(showCust[i][j])
                table = table + "<th>" + tableContent + "</th>"
            table = table + "</tr>"
        return """<html>
                """, head, """
                  <body>
                    <br /> 
                     <table style="width:100%">
                      <tr>
                        <th>Customer ID</th>                      
                        <th>Name</th>
                        <th>Adress</th>
                        <th>Phone</th>
                        <th>Username</th>
                        <th>Payment Type</th>
                        <th>Membership Type</th>
                      </tr>
                    """+table+"""
                    </table>                                        
                  </body>"""+bottom+"""
                </html>"""

    @expose()
    def showCustomer(self, Customerid):
        showCustomer = """SELECT c.Customerid, c.Name, c.Adress, c.Phone, c.Username, c.password, p.NameOfPayment, m.MembershipName from Customer c JOIN Membership m ON c.MembershipID = m.Membershipid JOIN PaymentType p ON c.PaymentTypeID=p.PaymentTypeid WHERE c.Customerid='"""+Customerid+"""'"""
        print(showCustomer)
        showCust = databaseExtract(showCustomer)
        table = ""
        userID = str(showCust[0][0])
        print (userID)
        for i in range(0, len(showCust)):
            table = table + "<tr>"
            for j in range(0, len(showCust[i])):
                tableContent = str(showCust[i][j])
                table = table + "<th>" + tableContent + "</th>"
            table = table + "</tr>"
        return """<html>
                        """, head, """
                          <body>
                            <br /> 
                             <table style="width:100%">
                              <tr>
                                <th>UserID</th>
                                <th>Name</th>
                                <th>Adress</th>
                                <th>Phone</th>
                                <th>Username</th>
                                <th>Password</th>
                                <th>Payment Type</th>
                                <th>Membership Type</th>
                              </tr>
                            """ + table + """
                             <br /> 
                            </table> 
                             <br />
                            <form method="get" action="customerHistory">
                                <input type="hidden" value="""+userID+""" name="CustomerID" />
                              <button type="submit">Orders made by customer!</button>
                            </form>
                            <br />                                                       
                            <form method="get" action="updateCustomer">
                            <input type="hidden" value="""+userID+""" name="CustomerID" />
                              <button type="submit">Update customer information!</button>
                            </form>
                            <br /> 
                            <form method="get" action="deleteCustomer">
                                <input type="hidden" value="""+userID+""" name="CustomerID" />
                              <button type="submit">Delete customer!</button>
                            </form>
                            <br />                           
                          </body>""" + bottom + """
                        </html>"""
    @expose()
    def updateCustomer(self, CustomerID):
        return("Update customer information.")

    @expose()
    def deleteCustomer(self,CustomerID):
        deleteSQL = """SELECT * FROM Customer WHERE CustomerID = """+CustomerID+""""""
        deletePerson = databaseExtract(deleteSQL)
        personName = str(deletePerson[0][1])
        personID = str(deletePerson[0][0])
        return """<html>
                """, head, """
                  <body>
                  <div>Are you sure you want to delete """+personName+""" from database?</div> 
                    <form method="get" action="customerDelted">
                        <input type="hidden" value="""+personID+""" name="Customerid" />
                         <input type="hidden" value="""+personName+""" name="CustomerName" />
                        <button type="submit">Yes, remove customer!</button>
                    </form>
                     <form method="get" action="showCustomer">
                        <input type="hidden" value="""+personID+""" name="Customerid" />
                        <button type="submit">No, keep record.</button>
                    </form>
                  </body>
                </html>"""

    @expose()
    def customerDelted(self,Customerid, CustomerName):
        customerID = Customerid
        deleteSQL = """DELETE FROM Customer WHERE CustomerID = """+customerID+""""""
        databaseInsert(deleteSQL)
        return """<html>
                """, head, """
                  <body>
                  <div>"""+CustomerName+""" was removed from database.</div> 
                  </body>"""+bottom+"""
                </html>"""


    @expose()
    def customerHistory(self,CustomerID):
        return("Orders made by customer")


    @expose()
    def searchCustomers(self):
        paymentSQL = """SELECT * FROM PaymentType"""
        paymentType = databaseExtract(paymentSQL)
        payment = "<option value="">""</option>"
        for i in range(0, len(paymentType)):
            pay = paymentType[i][1]
            payment = payment + "<option value='"+pay+"'>"+pay+"</option>"
        membershipSQL = """SELECT * FROM Membership"""
        membershipType = databaseExtract(membershipSQL)
        membership = "<option value=""></option>"
        for i in range(0, len(membershipType)):
            member = membershipType[i][1]
            membership = membership + "<option value='"+member+"'>"+member+"</option>"
        return """<html>
                """,head,"""
                  <body>
                    <div>Welcome to Expresso House</div>
                    <br /> 
                    <form method="get" action="searchCustomer">
                      <fieldset>
                        <legend>Search criteria:</legend>
                        <table>
                        <tr>
                        <td>Customer ID</td><td><input type="text" value="" name="customerid" /></td></tr>
                        <td>Customer Name</td><td><input type="text" value="" name="personName" /></td></tr>
                        <tr><td>Customer Adress</td><td><input type="text" value="" name="adress" /></td></tr>
                        <tr><td>Customer Phone</td><td><input type="text" value="" name="phone" /></td></tr>
                        <tr><td>Customer Username</td><td><input type="text" value="" name="username" /></td></tr>
                        <tr><td>Payment Type</td><td><select name="paymentType">"""+payment+"""</select></td></tr>
                        <tr><td>Membmership Type</td><td><select name="membershipType">"""+membership+"""</select></td>
                        </tr>
                        </table>  
                      <button type="submit">Search within the parameters!</button>
                      </fieldset>
                    </form>
                    <br /> 
                  </body>"""+bottom+"""
                </html>"""

    @expose
    def searchCustomer(self,customerid, personName, adress, phone, username, paymentType, membershipType):
        if(customerid=="" and personName=="" and adress =="" and phone == "" and username == "" and paymentType == "" and membershipType == ""):
            return """<html>
                """,head,"""
                  <body>
                    <div>Welcome to Expresso House</div>
                    <br />
                    <br />The search requires information, field out at least one field!.
                    <br />
                    <form method="get" action="searchCustomers">
                      <button type="submit">Back to customer search!</button>
                    </form> 
                  </body>"""+bottom+"""
                </html>"""
        else:
            select = ""
            whereList = ["c.Customerid", "c.Name", "c.Adress", "c.Phone,", "c.Username", "p.NameOfPayment", "m.MembershipName"]
            customerList = [customerid, personName, adress, phone, username,paymentType, membershipType]
            notFirst = False
            for i in range(0, len(customerList)):
                if(customerList[i] != ""):
                    print(whereList[i])
                    if(notFirst != False):
                        select = select + " and "
                    select = select + """"""+whereList[i]+""" LIKE'%"""+customerList[i]+"""%'"""
                    notFirst = True
#        showCustomer = """SELECT c.Name, c.Adress, c.Phone, c.Username, p.NameOfPayment, m.MembershipName from Customer c JOIN Membership m ON c.MembershipID = m.Membershipid JOIN PaymentType p ON c.PaymentTypeID=p.PaymentTypeid WHERE c.Name="""+personName+"""
            showCustomer = """SELECT c.Customerid,c.Name, c.Adress, c.Phone, c.Username, p.NameOfPayment, m.MembershipName from Customer c JOIN Membership m ON c.MembershipID = m.Membershipid JOIN PaymentType p ON c.PaymentTypeID=p.PaymentTypeid WHERE """ + select + """"""
            print(showCustomer)
            showCust = databaseExtract(showCustomer)

            table = ""
            for i in range(0, len(showCust)):
                table = table + "<tr>"
                for j in range(0, 1):
                    tableContent = str(showCust[i][j])
                    table = table + """<th><a href="./showCustomer?Customerid=""" + tableContent + """">""" + tableContent + """</a></p></th>"""
                for j in range(1, len(showCust[i])):
                    tableContent = str(showCust[i][j])
                    table = table + "<th>" + tableContent + "</th>"
                table = table + "</tr>"
            return """<html>
                    """, head, """
                      <body>
                        <br /> 
                         <table style="width:100%">
                          <tr>
                            <th>Customer ID</th>
                            <th>Name</th>
                            <th>Adress</th>
                            <th>Phone</th>
                            <th>Username</th>
                            <th>Payment Type</th>
                            <th>Membership Type</th>
                          </tr>
                        """ + table + """
                        </table>                                        
                      </body>""" + bottom + """
                    </html>"""


#decorate the function
    @expose
    def products(self):
        return """<html>
                """,head,"""
                  <body>
                    <div>Welcome to Expresso House</div>
                    <br /> 
                    <form method="get" action="showProducts">
                      <button type="submit">Show all products!</button>
                    </form>
                    <br /> 
                    <form method="get" action="addProduct">
                      <button type="submit">Add a product!</button>
                    </form>
                    <br /> 
                    <form method="get" action="searchProducts">
                      <button type="submit">Search for a product!</button>
                    </form>
                    <br /> 
                    <br /> 
                  </body>"""+bottom+"""
                </html>"""
    @expose()
    def showProducts(self):
        allProductsSQL = """SELECT p.ProductID, p.Name, p.Price, p.Availability,p.Description,s.Name, s.Description, t.Name, t.Description FROM Product p JOIN ProductType t ON p.ProductTypeID=t.ProductTypeid JOIN ProductSize s ON p.SizeID=s.ProductSizeid"""
        allProducts = databaseExtract(allProductsSQL)
        productList = ["Produckt ID", "Product Name", "Price", "Description","Availability", "Size", "Size Description","Product Type","Product Description"]
        table = ""
        for i in range(0, len(allProducts)):
            table = table+ "<tr>"
            for j in range(0, 1):
                tableContent = str(allProducts[i][j])
                table = table + """<th><a href="./showProduct?ProductID="""+tableContent+"""">"""+tableContent+"""</a></p></th>"""
            for j in range(1, len(allProducts[i])):
                tableContent = str(allProducts[i][j])
                table = table + "<th>" + tableContent + "</th>"
            table = table + "</tr>"
        return """<html>
                """, head, """
                  <body>
                    <br /> 
                     <table style="width:100%">
                      <tr>
                        <th>Product ID</th>                      
                        <th>Product Name</th>
                        <th>Price</th>
                        <th>Availability</th>
                        <th>Description</th>
                        <th>Size</th>
                        <th>Size Description</th>                        
                        <th>Product Type</th>
                        <th>Product Description</th>
                      </tr>
                    """+table+"""
                    </table>                                        
                  </body>"""+productButton+bottom+"""
                </html>"""

    @expose()
    def showProduct(self, ProductID):
        return("Showing a product.")

    @expose()
    def updateProduct(self):
        return("Update a product.")

    @expose()
    def deleteProduct(self):
        return("Removing a product.")

    @expose()
    def addProduct(self):
        return("Adding a new product")

    @expose()
    def searchProducts(self):
        return("Search products.")

if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(ExpressoHouse(), '/', conf)


#http://127.0.0.1:8080/celsiusToFahrenheit?temperature=100

#Make pages for inserting into database expresso house (CRUD, create, read, update, delete), main menu with linkes?, various types of transactions and insertions, customers, purchases, etc, populate teh database, the ones without dependencies first
