import os
import platform
from datetime import date
from db_config import get_connection


def clrscreen():
    os.system("cls" if platform.system() == "Windows" else "clear")


def insertData():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        bno = input("Enter Book Code: ")
        bname = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        price = float(input("Enter Book Price: "))
        publisher = input("Enter Publisher: ")
        qty = int(input("Enter Quantity: "))
        yy = int(input("Enter Purchase Year: "))
        mm = int(input("Enter Purchase Month: "))
        dd = int(input("Enter Purchase Date: "))

        query = """
            INSERT INTO BookRecord
            (BNo, BName, Author, Price, Publisher, Qty, DateOfPurchase)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        data = (bno, bname, author, price, publisher, qty, date(yy, mm, dd))
        cursor.execute(query, data)
        conn.commit()
        print("Book record inserted successfully.")
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()


def display():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM BookRecord")
        rows = cursor.fetchall()
        if not rows:
            print("No book records found.")
            return
        for row in rows:
            print("=" * 55)
            print("Book Code:", row[0])
            print("Book Name:", row[1])
            print("Author:", row[2])
            print("Price:", row[3])
            print("Publisher:", row[4])
            print("Quantity:", row[5])
            print("Purchased On:", row[6])
        print("=" * 55)
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()


def SearchBookRec():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        bno = input("Enter Book Code to search: ")
        cursor.execute("SELECT * FROM BookRecord WHERE BNo = %s", (bno,))
        row = cursor.fetchone()
        if row:
            print("=" * 55)
            print("Book Code:", row[0])
            print("Book Name:", row[1])
            print("Author:", row[2])
            print("Price:", row[3])
            print("Publisher:", row[4])
            print("Quantity:", row[5])
            print("Purchased On:", row[6])
            print("=" * 55)
        else:
            print("Book not found.")
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()


def deleteBook():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        bno = input("Enter Book Code to delete: ")
        cursor.execute("DELETE FROM BookRecord WHERE BNo = %s", (bno,))
        conn.commit()
        print(cursor.rowcount, "record(s) deleted.")
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()


def UpdateBook():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        bno = input("Enter Book Code to update: ")
        bname = input("Enter New Book Name: ")
        author = input("Enter New Author Name: ")
        price = float(input("Enter New Price: "))
        publisher = input("Enter New Publisher: ")
        qty = int(input("Enter New Quantity: "))
        yy = int(input("Enter Purchase Year: "))
        mm = int(input("Enter Purchase Month: "))
        dd = int(input("Enter Purchase Date: "))

        query = """
            UPDATE BookRecord
            SET BName=%s, Author=%s, Price=%s, Publisher=%s, Qty=%s, DateOfPurchase=%s
            WHERE BNo=%s
        """
        data = (bname, author, price, publisher, qty, date(yy, mm, dd), bno)
        cursor.execute(query, data)
        conn.commit()
        print(cursor.rowcount, "record(s) updated.")
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()
