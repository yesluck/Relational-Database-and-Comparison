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
    people_rdbt = RDBDataTable("People", "People.rdb", ["playerID"], cnx)
    people_rdbt.load()
    t = {"nameFirst": "Ted", "birthMonth": "10"}
    f = ["playerID", "nameFirst", "nameLast", "birthYear", "birthMonth", "birthDay"]  # Screenshot_rdb2-1
    # f = []  # Screenshot_rdb2-2
    # f = ["firstName"]   # Screenshot_rdb2-3
    # f = "playerID"      # Screenshot_rdb2-4
    print("Testing template ", t, ", fields", f, " on table", "People")
    start = time.time()
    result = people_rdbt.find_by_template(t, f)
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in RDB method is: {0:.3f}s".format(end - start))
except Exception as e:
    print("Got exception = ", str(e))