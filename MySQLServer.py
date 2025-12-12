import mysql.connector
import sys


def create_database():
    """Create alxbookstore database if it doesn't exist"""
    try:
        # Connect to MySQL server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Matyman1050"
        )
        
        # Create cursor
        cursor = conn.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
        
        print("Database 'alxbookstore' created successfully!")
        
        # Close cursor and connection
        cursor.close()
        conn.close()
        
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    create_database()