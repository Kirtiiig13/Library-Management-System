from datetime import date
from db_config import get_connection


def insertData():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        mno = input("Enter Member Code: ")
        mname = input("Enter Member Name: ")
        mobile = input("Enter Mobile Number: ")
        yy = int(input("Enter Membership Year: "))
        mm = int(input("Enter Membership Month: "))
        dd = int(input("Enter Membership Date: "))
        address = input("Enter Address: ")

        query = "INSERT INTO Member VALUES (%s, %s, %s, %s, %s)"
        data = (mno, mname, mobile, date(yy, mm, dd), address)
        cursor.execute(query, data)
        conn.commit()
        print("Member record inserted successfully.")
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
        cursor.execute("SELECT * FROM Member")
        rows = cursor.fetchall()
        if not rows:
            print("No member records found.")
            return
        for row in rows:
            print("=" * 55)
            print("Member Code:", row[0])
            print("Member Name:", row[1])
            print("Mobile:", row[2])
            print("Date of Membership:", row[3])
            print("Address:", row[4])
        print("=" * 55)
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()


def SearchMember():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        mno = input("Enter Member Code to search: ")
        cursor.execute("SELECT * FROM Member WHERE MNo = %s", (mno,))
        row = cursor.fetchone()
        if row:
            print("=" * 55)
            print("Member Code:", row[0])
            print("Member Name:", row[1])
            print("Mobile:", row[2])
            print("Date of Membership:", row[3])
            print("Address:", row[4])
            print("=" * 55)
        else:
            print("Member not found.")
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()


def deleteMember():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        mno = input("Enter Member Code to delete: ")
        cursor.execute("DELETE FROM Member WHERE MNo = %s", (mno,))
        conn.commit()
        print(cursor.rowcount, "record(s) deleted.")
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()
