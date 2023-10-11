import pyodbc
import bcrypt

def sql_newlogin(username, password):
    try:
        connection = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=MSI;DATABASE=CorpPoke'
        )
        cursor = connection.cursor()

        # Check if the username already exists
        cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("Username already exists. User not inserted.")
            return 0
        else:
            if len(password) > 0:  # Replace with a function to verify password security???
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
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

def sql_login(username, entered_password):
    try:
        connection = pyodbc.connect('DRIVER={SQL Server};SERVER=MSI;DATABASE=CorpPoke')
        cursor = connection.cursor()

        # Check if the user is in the 'users' table
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            stored_password = user.password

            if bcrypt.checkpw(entered_password.encode('utf-8'), stored_password.encode('utf-8')):
                return "user"
            else:
                print("Invalid password.")
                return 0

        # Check if the user is in the 'line_manager' table
        cursor.execute("SELECT * FROM line_manager WHERE username = ?", (username,))
        user = cursor.fetchone()

        if user:
            stored_password = user.password

            if bcrypt.checkpw(entered_password.encode('utf-8'), stored_password.encode('utf-8')):
                return "admin"
            else:
                print("Invalid password.")
                return 0

        print("Username not found.")
        return 0

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
