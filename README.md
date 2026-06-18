# Library Management System

A console-based Library Management System made with Python and MySQL.

## Features

- Add, display, search, update, and delete books
- Add, display, search, and delete members
- Issue books to members
- Return books
- MySQL database integration

## Technologies Used

- Python
- MySQL
- mysql-connector-python

## Project Structure

```text
Library-Management-System/
├── LIBRMGMT.py
├── MenuLib.py
├── Book.py
├── Member.py
├── issue.py
├── db_config.py
├── database.sql
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Install Python.
2. Install MySQL Server.
3. Install Python package:

```bash
pip install -r requirements.txt
```

4. Import the database:

```bash
mysql -u root -p < database.sql
```

5. Open `db_config.py` and update your MySQL password if needed.

6. Run the project:

```bash
python LIBRMGMT.py
```

## Author

Kirti Gautam
