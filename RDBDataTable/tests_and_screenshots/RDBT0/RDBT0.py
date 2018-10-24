import sys
sys.path.append("../../../RDB/src")
from RDBTenGreatestHitters import *


try:
    cnx = pymysql.connect(host='localhost',
                          port=3306,
                          user='root',
                          password='database',
                          db='Lahman2017',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
    people_rdbt = RDBDataTable("People", "People.rdb", ["playerID"], cnx)
    people_rdbt.load()
    print(people_rdbt)
except Exception as e:
    print("Got exception = ", str(e))