import pyodbc
import bcrypt

def sql_newlogin(username, password):
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=MSI;DATABASE=CorpPoke' #personal, can change
        )
        cursor = connection.cursor()

        # Check if the username already exists
        cursor.execute("SELECT 1 FROM line_manager WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username already exists. User not inserted.")
            return 0
        else:
            if len(password) > 0:  # Replace with a function to verify password security???
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                cursor.execute("INSERT INTO line_manager (username, password) VALUES (?, ?)", (username, hashed_password))
                connection.commit()
                print("User inserted successfully.")
                return 1
            else:
                print("Invalid password.")
                return 0

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()



username = input("Enter username: ")
password = input("Enter password: ")
sql_newlogin(username, password)