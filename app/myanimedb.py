import sqlite3

DB_FILE = "anime.db"


def createTable():
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("DROP TABLE IF EXISTS userData")
    c.execute('''
        CREATE TABLE IF NOT EXISTS userData (
            userID INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL)
        ''')
    db.commit()
    db.close()

def addUser(username, password):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT userID FROM userData;")
    num = c.fetchall()
    c.execute("INSERT INTO userData (userID, username, password) VALUES (?, ?, ?);", (len(num), username, password))

    db.commit()
    db.close()

def allUserData():
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT * FROM userData")
    prin = c.fetchall()
    print("users: ")
    print(prin)

createTable()
addUser("maq", "787")
addUser("sunjinwoo", "arise")
allUserData()
