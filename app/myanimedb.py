import sqlite3
import array

DB_FILE = "anime.db"

#Mutator Methods
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

def addGraphColumn():
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    #Note: This returns the number of columns in a data set
    c.execute("SELECT * FROM userData")
    num_cols = len(list(c.fetchone()))
    #print(num_cols)

    graphName = f"graph{num_cols - 3}"
    c.execute(f"ALTER TABLE userData ADD {graphName} INTEGER")

    db.commit()
    db.close()

#Accessor methods

def allUserData():
#For print statements only
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT * FROM userData")
    prin = c.fetchall()
    print("users: ")
    print(prin)

def getUserName(userID):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT username FROM userData where userID = {userID}")
    fin = list(res.fetchone())[1]

    db.commmit()
    db.close()
    return fin
def getPassword(userID):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT password FROM userData where userID = {userID}")
    fin = list(res.fetchone())[2]

    db.commmit()
    db.close()
    return fin
def getGraph(userID, colNum):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT graph{colNum} FROM userData where userID = {userID}")
    fin = list(res.fetchone())[0]

    db.commmit()
    db.close()
    return fin
createTable()
addUser("maq", "787")
addUser("sunjinwoo", "arise")
#addGraphColumn()
#addGraphColumn()
print("Should be: maq. Result: " + getUserName(0))
print("Should be: arise. Result: " + getPassword(1))
allUserData()
