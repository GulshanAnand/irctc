import mysql.connector as sql
import json
from encrypt import *

db = sql.connect(
  host = "localhost",
  user = "admin",
  password = "admin123",
  database = "railway"
)

def getAll():
    cursor = db.cursor(dictionary = True)
    cursor.execute("SELECT * FROM USER")
    table = cursor.fetchall()
    result = []
    for row in table:
        result.append(row)
    return result

def getWhere(uid):
    cursor = db.cursor(dictionary = True)
    cursor.execute("SELECT * FROM USER WHERE user_id = %s", (uid,))
    table = cursor.fetchall()
    result = []
    for row in table:
        result.append(row)
    return result

def checkUser(uid, passwd):
    cursor = db.cursor(dictionary = True)
    cursor.execute("SELECT * FROM USER WHERE user_id = %s", (uid,))
    table = cursor.fetchall()
    password = table[0]["password"]
    passHash = encrypt(passwd)
    if password == passHash:
        return True
    return False

def search_train(from_code, to_code):
    from_code.upper()
    to_code.upper()
    cursor = db.cursor(dictionary = True)
    cursor.execute("SELECT t1.station_code as from_station, t1.train_no, t2.station_code as to_station from STATION as t1 cross join STATION as t2 where t1.station_code = %s and t2.station_code = %s and t1.train_no = t2.train_no", (from_code, to_code,))
    table = cursor.fetchall()
    result = []
    for row in table:
        result.append(row)
    return result