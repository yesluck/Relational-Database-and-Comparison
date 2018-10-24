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
    t = {"nameFirst": "Ted", "nameLast": "Williams"}    # Screenshot_rdb1-1
    # t = {}                                              # Screenshot_rdb1-2
    # t = {"firstName": "Ted", "nameLast": "Williams"}    # Screenshot_rdb1-3
    # t = ["Ted", "Williams"]  # Screenshot_1-4
    print("Testing template ", t, " on table", "People")
    start = time.time()
    result = people_rdbt.find_by_template(t)
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in RDB method is: {0:.3f}s".format(end - start))
except Exception as e:
    print("Got exception = ", str(e))