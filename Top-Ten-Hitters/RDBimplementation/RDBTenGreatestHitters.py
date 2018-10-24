import pymysql.cursors
import sys
sys.path.append("../../RDBDataTable/src")
from RDBDataTable import *

def top_ten_hitters():
    q = "SELECT \
            Batting.playerID, \
            (SELECT People.nameFirst FROM People WHERE People.playerID=Batting.playerID) as first_name, \
            (SELECT People.nameLast FROM People WHERE People.playerID=Batting.playerID) as last_name, \
            sum(Batting.h) as career_hits, \
            sum(Batting.ab) as career_at_bats,\
            sum(Batting.h)/sum(batting.ab) as career_average, \
            min(Batting.yearID) as first_year, \
            max(Batting.yearID) as last_year \
            FROM \
            Batting \
            GROUP BY \
            playerId \
            HAVING \
            career_at_bats > 200 AND last_year >= 1960 \
            ORDER BY \
            career_average DESC \
            LIMIT 10;"
    cnx = pymysql.connect(host='localhost',
                          port=3306,
                          user='root',
                          password='database',
                          db='Lahman2017',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
    cursor = cnx.cursor()
    cursor.execute(q)
    r = cursor.fetchall()
    return r

try:
    top_ten_hitters()
except Exception as e:
    print("Got exception = ", str(e))