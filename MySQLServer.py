import MySQLdb
import sys


def create_database():
    """Create alx_book_store database if it doesn't exist"""
    try:
        db = MySQLdb.connect(
            host="localhost",
            user="root",      
            passwd="@Matyman1050",       
            port=3306
        )
        
        cursor = db.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        print("Database 'alx_book_store' created successfully!")
        
        cursor.close()
        db.close()
        
    except MySQLdb.Error as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    create_database()