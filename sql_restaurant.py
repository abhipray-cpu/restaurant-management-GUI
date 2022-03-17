import mysql.connector
from mysql.connector import errorcode
from mysql.connector import Error
from datetime import datetime,date
import os
cnx = mysql.connector.connect(user='root', password=f"{os.environ(['SQL_PASSWORD'])}",
                                      host='localhost',
                                      database='hotel_management')

def insert_orders(Order,Customer,Number,Subtotal,Taxes,Total):
    try:
        data_login = (Order,Customer,Number,Subtotal,Taxes,Total)
        query = "INSERT INTO orders (Order_details,Customer,Number,Subtotal,Taxes,Total) VALUES (%s,%s,%s,%s,%s,%s)"
        cursor = cnx.cursor()
        cursor.execute(query, data_login)
        print("Abhi toe aur chlega")
        cnx.commit()
        print("Abhi bhi chl rha hai")
        return 1
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return 0
    else:
        print("Insert operation failed tu toe lut gya re gotiya")

def fetch_orders():
    try:

        query = "SELECT * from orders"
        cursor = cnx.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        #print(result)
        return result  # this is a list of tuple therfore for each value extraced you can gain further access to other two values of tuple
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Insert operation failed tu toe lut gya re gotiya")


def insert_revenue(revenue,expense,profit):
    try:
        time=date.today()
        data_login = (time,revenue,expense,profit)
        query = "INSERT INTO restaurant_revenue (Date,Revenue,Expense,Profit) VALUES (%s,%s,%s,%s)"
        cursor = cnx.cursor()
        cursor.execute(query, data_login)
        print("Abhi toe aur chlega")
        cnx.commit()
        print("Abhi bhi chl rha hai")
        return 1
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return 0
    else:
        print("Insert operation failed tu toe lut gya re gotiya")



def fetch_revenue():
    try:

        query = "SELECT * from restaurant_revenue"
        cursor = cnx.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        #print(result)
        return result  # this is a list of tuple therfore for each value extraced you can gain further access to other two values of tuple
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        print("Insert operation failed tu toe lut gya re gotiya")


def fetch_specific_order(Customer,Number):
    try:
        data = (Customer,Number)
        query = f"SELECT * FROM orders WHERE Customer = %s and Number = %s"
        cursor = cnx.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        #print(result)
        return result

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

def fetch_specific_revenue(data):
    try:
        # a word of advice never leave tuple with a single element always add a comma aftet it if the tuple you are using has only one element in it
        data = (data,)
        query = f"SELECT * FROM restaurant_revenue WHERE Tareekh = %s"
        cursor = cnx.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        #print(result)
        return result

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()




















