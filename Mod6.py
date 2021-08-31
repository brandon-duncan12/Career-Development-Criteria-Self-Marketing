# Brandon M. Duncan
# MIS480: Capstone - Business Analytics and Information Systems
# Dr. Kimberly Ford

# Imports the Connector
import mysql.connector

# Establishes Connection With the Database
mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "dbe@MDH09200614",
database = "classicmodels",
)

# Obtains a Cursor
my_cursor = mydb.cursor()

# Queries the payments Table From the classicmodels Database
my_cursor.execute(
    "SELECT customerNumber, PaymentDate, amount FROM payments "
    "WHERE month(paymentDate) = 12 "
    "ORDER BY PaymentDate;")

# Used to Retrieve All Rows
db_result = my_cursor.fetchall()

# Used to Center and Print String
brbt= "PAYMENT AMOUNT BEFORE REBATE \n" + "x" * 45
brbt= brbt.center(90)
print(" ", brbt)

# Used to Align and Print Column Names and Data Before Rebate
print("{: <14} {: <18} {: <15}".format("CustomerID", "PaymentDate", "Amount"))
for x in db_result:
    print("{: <14} {: <17} {: <19}".format(x[0], str(x[1]), x[2]))

print("\n")

# Used to Center and Print String
arbt= "PAYMENT AMOUNT AFTER REBATE \n" + "x" * 45
arbt= arbt.center(90)
print(" ", arbt)

# Used to Align, Add Rebate, and Print Column Names and Data After Rebate
print("{: <14} {: <18} {: <15}".format("CustomerID", "PaymentDate", "Amount"))
for x in db_result:
    Amount = float(x[2])
    Amount = Amount - (Amount / 100.0)
    print("{: <14} {: <17} {: <19.2f}".format(x[0], str(x[1]), Amount))
