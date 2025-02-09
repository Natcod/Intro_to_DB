import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (Update credentials if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",  # Change to your MySQL username
            password="your_password"  # Change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Creating the database (ensures no failure if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:  # ✅ Catching mysql.connector.Error explicitly
        print(f"Error: {e}")

    finally:
        # Ensure cursor and connection are properly closed
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

# Execute the function
create_database()
