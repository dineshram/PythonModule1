
#it is important to note that you must add the foreign key as a regular attribute of the table before you attempt to add the foreign key statement
createProductTableSQL = """CREATE TABLE Product(
             ProductID Integer,
             Name text,
             Price real,
             ProductTypeID Integer,
             Primary Key(ProductID),
             Foreign Key(ProductTypeID) references
                        ProductType(ProductTypeID))"""

createProductTypeTableSQL = """CREATE TABLE ProductType(
             ProductTypeID Integer,
             Description text,
             Primary Key(ProductTypeID))"""


#SQLite PRAGMA command is a special command to be used to control various environmental
# variables and state flags within the SQLite environment. A PRAGMA value can be read and it can also be set based on the requirements.
# It is important to keep in mind that by default SQLite does not check for foreign key constraints
# and therefore you must explicitly turn this feature on using the following statement:
#Doing this will ensure that you do not get any unexpected inconsistency in your data.
pragma = """PRAGMA Foreign_Keys = ON"""

# --select name from sqlite_master where name = 'film'

#--PRAGMA Foreign_Keys = ON

#--SELECT * from sys.tables
#SELECT * FROM sqlite_master WHERE type='table'
