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

def search_train(from_code, to_code, date_s):
    from_code.upper()
    to_code.upper()
    weekday = 4 
    wdn = "%" + str(weekday) + "%"
    cursor = db.cursor(dictionary = True)
    cursor.execute("SELECT a.train_no, a.station_code as from_stat, b.station_code as to_stat,a.departure_t, b.arrival_t, %s as date from STATION as a, STATION as b, AVAILABLE as c where a.train_no=b.train_no and a.station_code=%s and b.station_code=%s and c.train_no = a.train_no and c.week_day like %s", (date_s, from_code, to_code, wdn,))

    # cursor.execute("SELECT t1.station_code as from_station, t1.train_no, t2.station_code as to_station from STATION as t1 cross join STATION as t2 where t1.station_code = %s and t2.station_code = %s and t1.train_no = t2.train_no", (from_code, to_code,))
    table = cursor.fetchall()
    result = []
    for row in table:
        result.append(row)
    return result
    # return table


def bookTicket():
    
    cursor db.cursor()
    cursor.execute("INSERT INTO TICKET VALUES(%s, %s, %s, %s, %s, %s, %s)", ("10001"))

# abcd = 
# abcd = search_train("CNB", "DHN", "2022-11-11")
# for e in abcd:
#     print(e)


'''
select a.train_no,a.station_code, b.station_code,a.departure_t, b.arrival_t,"2022-10-28" as date from STATION as a, STATION as b, AVAILABLE as c where a.train_no=b.train_no and a.station_code="CNB" and b.station_code="PNBE" and c.train_no = a.train_no and c.week_day like '%4%'
'''