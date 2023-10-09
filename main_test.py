import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="db"
    )

if __name__ == "__main__":
    connection = create_connection()

    print("Connect to database")

    connection.close()