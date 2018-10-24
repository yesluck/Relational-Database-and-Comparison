import sys
sys.path.append("../../../RDB/src")
from RDBTenGreatestHitters import *
import time


try:
    cnx = pymysql.connect(host='localhost',
                          port=3306,
                          user='root',
                          password='database',
                          db='Lahman2017',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
    people_rdbt = RDBDataTable("Batting", "Batting.rdb", ["playerID", "yearID", "teamID", "stint"], cnx)
    people_rdbt.load()
    pk = ['bellast01', "1871", "TRO", "1"]      # Screenshot_3-1
    # pk = ['bellast01', "1871", "TRO"]           # Screenshot_3-2
    # pk = ['bellast01', "1871", "WRONG", "1"]    # Screenshot_3-3
    # pk = 'bellast'                              # Screenshot_3-4
    f = ["playerID", "yearID", "teamID", "stint", "AB", "H"]
    print("Testing primary key ", pk, " on table", "Batting")
    start = time.time()
    result = people_rdbt.find_by_primary_key(pk,f)
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in RDB method is: {0:.3f}s".format(end - start))
except Exception as e:
    print("Got exception = ", str(e))