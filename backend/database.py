import sqlite3

# Function to initialize the database (create tables if they don't exist)
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    diagnosis TEXT,
                    recommendation TEXT
                 )''') 
    conn.commit()

# Function to store user data in the database
def store_user_data(username, diagnosis, recommendation):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, diagnosis, recommendation) VALUES (?, ?, ?)', (username, diagnosis, recommendation))
    conn.commit()

# Function to get user data from the database
def get_user_data():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    data = c.fetchall()
    conn.close()
    return data
