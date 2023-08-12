import os
import pyodbc

def get_connection_string():
    azure_db = os.environ.get('DB_CONNECTION_STRING')
    return azure_db
    
def create_connection():
    return pyodbc.connect(get_connection_string())

def main():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM FOODS"
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    connection.close()

if __name__ == '__main__':
    main()