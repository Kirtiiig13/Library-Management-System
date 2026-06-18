from datetime import date
from db_config import get_connection


def issueBookData():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        bno = input("Enter Book Code to issue: ")
        mno = input("Enter Member Code: ")
        yy = int(input("Enter Issue Year: "))
        mm = int(input("Enter Issue Month: "))
        dd = int(input("Enter Issue Date: "))

        cursor.execute("SELECT Qty FROM BookRecord WHERE BNo=%s", (bno,))
        book = cursor.fetchone()
        if not book:
            print("Book not found.")
            return
        if book[0] <= 0:
            print("Book is out of stock.")
            return

        cursor.execute("SELECT MNo FROM Member WHERE MNo=%s", (mno,))
        if not cursor.fetchone():
            print("Member not found.")
            return

        query = "INSERT INTO IssueRecord (BNo, MNo, IssueDate, ReturnDate) VALUES (%s, %s, %s, NULL)"
        cursor.execute(query, (bno, mno, date(yy, mm, dd)))
        cursor.execute("UPDATE BookRecord SET Qty = Qty - 1 WHERE BNo=%s", (bno,))
        conn.commit()
        print("Book issued successfully.")
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()


def ShowIssuedBooks():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        query = """
            SELECT I.IssueID, B.BNo, B.BName, M.MNo, M.MName, I.IssueDate, I.ReturnDate
            FROM IssueRecord I
            JOIN BookRecord B ON I.BNo = B.BNo
            JOIN Member M ON I.MNo = M.MNo
            ORDER BY I.IssueID DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            print("No issued book records found.")
            return
        for row in rows:
            print("=" * 55)
            print("Issue ID:", row[0])
            print("Book Code:", row[1])
            print("Book Name:", row[2])
            print("Member Code:", row[3])
            print("Member Name:", row[4])
            print("Issue Date:", row[5])
            print("Return Date:", row[6] if row[6] else "Not returned")
        print("=" * 55)
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()


def returnBook():
    conn = get_connection()
    if not conn:
        return
    try:
        cursor = conn.cursor()
        issue_id = input("Enter Issue ID to return: ")
        cursor.execute("SELECT BNo, ReturnDate FROM IssueRecord WHERE IssueID=%s", (issue_id,))
        record = cursor.fetchone()
        if not record:
            print("Issue record not found.")
            return
        if record[1] is not None:
            print("This book is already returned.")
            return
        bno = record[0]
        cursor.execute("UPDATE IssueRecord SET ReturnDate=%s WHERE IssueID=%s", (date.today(), issue_id))
        cursor.execute("UPDATE BookRecord SET Qty = Qty + 1 WHERE BNo=%s", (bno,))
        conn.commit()
        print("Book returned successfully.")
    except Exception as err:
        print("Error:", err)
    finally:
        conn.close()
