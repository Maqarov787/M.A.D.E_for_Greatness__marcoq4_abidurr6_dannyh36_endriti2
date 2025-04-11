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
    c.execute("INSERT INTO userData (userID, username, password) VALUES (?, ?, ?)", (len(num), username, password))

    db.commit()
    db.close()

def addGraph(userID, file_name):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    c.execute("SELECT * FROM userData")
    num_cols = len(list(c.fetchone()))
    last = num_cols - 3
    i = 0
    col = 0

    while i <= last:
        if i == last:
            c.execute(f"ALTER TABLE userData ADD graph{last} INTEGER")
            last = last + 1

        c.execute(f"SELECT graph{i} FROM userData WHERE userID = '{userID}'")
        graph = c.fetchone()
        print("Current graph: " + str(graph))
        if list(graph)[0] is None:
            fin = list(graph)[0]
            col = i
            #graphName = graph + str(col)
            i += last + 1

        i = i + 1


    c.execute(f"UPDATE userData SET graph{col} = ? WHERE userID = ?", (file_name, userID))

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

def getUserName(username):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT username FROM userData where username = '{username}'")
    try:
        fin = res.fetchone()[0]
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        fin = None
    db.commit()
    db.close()
    return fin
def getPassword(username):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT password FROM userData where username = '{username}'")
    fin = list(res.fetchone())[0]

    db.commit()
    db.close()
    return fin
def getGraph(username, colNum):
    db = sqlite3.connect(DB_FILE, check_same_thread=False)
    c = db.cursor()
    res = c.execute(f"SELECT graph{colNum} FROM userData where username = '{username}'")
    fin = list(res.fetchone())[0]

    db.commit()
    db.close()
    return fin

#Testing Area
# createTable()
# addUser("maq", "787")
# addUser("sunjinwoo", "arise")
# #addGraphColumn()
# #addGraphColumn()
# addGraph(0, "test.jpg")
# addGraph(0, "test2.jpg")
# addGraph(1, "pie.jpg")
# print("Should be: maq. Result: " + str(getUserName(0)))
# print("Should be: arise. Result: " + str(getPassword(1)))
# allUserData()
#getUserName("maq")
