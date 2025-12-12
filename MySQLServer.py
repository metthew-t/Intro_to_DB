#!/usr/bin/python3
"""
ALX Task 1
"""
import mysql.connector
import sys

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Matyman1050"
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
    print("Database 'alxbookstore' created successfully!")
    cursor.close()
    connection.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    sys.exit(1