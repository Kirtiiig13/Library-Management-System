import Book
import MenuLib


def main():
    while True:
        Book.clrscreen()
        print("\t\tLibrary Management System")
        print("=" * 55)
        print("1. Book Management")
        print("2. Members Management")
        print("3. Issue / Return Book")
        print("4. Exit")
        print("=" * 55)
        choice = input("Enter choice: ")
        if choice == "1":
            MenuLib.MenuBook()
        elif choice == "2":
            MenuLib.MenuMember()
        elif choice == "3":
            MenuLib.MenuIssueReturn()
        elif choice == "4":
            print("Thank you for using Library Management System.")
            break
        else:
            print("Wrong choice.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
