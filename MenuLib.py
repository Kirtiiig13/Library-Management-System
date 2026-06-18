import Book
import Member
import issue


def pause():
    input("\nPress Enter to continue...")


def MenuBook():
    while True:
        Book.clrscreen()
        print("\t\tBook Record Management")
        print("=" * 55)
        print("1. Add Book Record")
        print("2. Display Book Records")
        print("3. Search Book Record")
        print("4. Delete Book Record")
        print("5. Update Book Record")
        print("6. Return to Main Menu")
        print("=" * 55)
        choice = input("Enter choice: ")
        if choice == "1":
            Book.insertData()
            pause()
        elif choice == "2":
            Book.display()
            pause()
        elif choice == "3":
            Book.SearchBookRec()
            pause()
        elif choice == "4":
            Book.deleteBook()
            pause()
        elif choice == "5":
            Book.UpdateBook()
            pause()
        elif choice == "6":
            return
        else:
            print("Wrong choice.")
            pause()


def MenuMember():
    while True:
        Book.clrscreen()
        print("\t\tMember Record Management")
        print("=" * 55)
        print("1. Add Member Record")
        print("2. Display Member Records")
        print("3. Search Member Record")
        print("4. Delete Member Record")
        print("5. Return to Main Menu")
        print("=" * 55)
        choice = input("Enter choice: ")
        if choice == "1":
            Member.insertData()
            pause()
        elif choice == "2":
            Member.display()
            pause()
        elif choice == "3":
            Member.SearchMember()
            pause()
        elif choice == "4":
            Member.deleteMember()
            pause()
        elif choice == "5":
            return
        else:
            print("Wrong choice.")
            pause()


def MenuIssueReturn():
    while True:
        Book.clrscreen()
        print("\t\tIssue / Return Book")
        print("=" * 55)
        print("1. Issue Book")
        print("2. Display Issued Book Records")
        print("3. Return Issued Book")
        print("4. Return to Main Menu")
        print("=" * 55)
        choice = input("Enter choice: ")
        if choice == "1":
            issue.issueBookData()
            pause()
        elif choice == "2":
            issue.ShowIssuedBooks()
            pause()
        elif choice == "3":
            issue.returnBook()
            pause()
        elif choice == "4":
            return
        else:
            print("Wrong choice.")
            pause()
