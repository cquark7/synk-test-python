import sqlite3

def process_user_input():
    user_input = input("Enter a command: ")
    
    # Insecure use of eval
    result = eval(user_input)
    
    # Hardcoded credentials
    username = "admin"
    password = "super_secret_password"
    
    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    # Command injection vulnerability
    import os
    os.system(f"echo {user_input}")
    
    # Insecure random number generation
    import random
    secret_key = random.randint(1, 1000000)
    
    # Weak cryptography
    def encrypt(data):
        return ''.join(chr(ord(c) + 1) for c in data)
    
    encrypted_password = encrypt(password)
    
    print(f"Result: {result}")
    print(f"Query: {query}")
    print(f"Secret Key: {secret_key}")
    print(f"Encrypted Password: {encrypted_password}")


def user_login(username, password):
    # Connect to the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable SQL query
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    
    # Execute the query
    cursor.execute(query)
    
    # Fetch the result
    result = cursor.fetchone()
    
    # Close the connection
    conn.close()
    
    # Check if user exists
    if result:
        return "Login successful"
    else:
        return "Login failed"

# Example usage


if __name__ == "__main__":
    process_user_input()
    username = input("Enter username: ")
    password = input("Enter password: ")
    print(user_login(username, password))
