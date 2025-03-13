import os
import mysql.connector
from mysql.connector import Error

def setup_database():
    """Set up the database and required tables"""
    try:
        # Get database connection details from environment variables
        host = os.environ.get('DB_HOST', 'localhost')
        user = os.environ.get('DB_USER', 'root')
        password = os.environ.get('DB_PASSWORD', '775533')
        database = os.environ.get('DB_NAME', 'face_recognition')
        
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            print(f"Database '{database}' created or already exists.")
            
            # Connect to the database
            cursor.execute(f"USE {database}")
            
            # Create employees table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                face_vector LONGBLOB,
                image_url VARCHAR(255),
                emp_id VARCHAR(50) UNIQUE
            )
            """)
            print("Employees table created or already exists.")
            
            # Create attendance table
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INT AUTO_INCREMENT PRIMARY KEY,
                emp_id INT,
                name VARCHAR(255),
                entry_time DATETIME,
                FOREIGN KEY (emp_id) REFERENCES employees(id) ON DELETE SET NULL
            )
            """)
            print("Attendance table created or already exists.")
            
            cursor.close()
            connection.close()
            print("Database setup completed successfully.")
            
    except Error as e:
        print(f"Error setting up database: {e}")

if __name__ == "__main__":
    setup_database() 