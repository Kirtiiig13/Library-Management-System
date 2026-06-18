import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "password",  # Update with your MySQL password
    "database": "library_management"
}



def get_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as err:
        print("Database connection failed:", err)
        print("Please check MySQL is running and update db_config.py with your username/password.")
        return None
