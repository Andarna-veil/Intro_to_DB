#!/usr/bin/python3
"""
Script that connects to a MySQL server and creates a database called alx_book_store.
If the database already exists, the script does not fail.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',          # change this if needed
        password='Signature2005_'  # replace with your real password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it doesn’t exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the connection properly
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
