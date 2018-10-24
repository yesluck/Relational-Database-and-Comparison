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

    # insert people -> insert batting -> delete battling -> delete people -> delete people(raise error)

    people_rdbt = RDBDataTable("People", "People.rdb", ["playerID"], cnx)
    people_rdbt.load()
    battling_rdbt = RDBDataTable("Batting", "Batting.rdb", ["playerID", "yearID", "teamID", "stint"], cnx)
    battling_rdbt.load()
    
    r1 = {"playerID" : "zl2737", "nameFirst" : "Zikun", "nameLast" : "Lin"}
    print("Inserting ", r1, " into table", "People")
    people_rdbt.insert(r1)

    r2 = {"playerID": "zl2737", "yearID": "2018", "teamID": "2737", "stint" : "1"}
    print("Inserting ", r2, " into table", "Batting")
    battling_rdbt.insert(r2)

    pk1 = ["zl2737"]
    f = ["playerID", "nameFirst", "nameLast"]
    start = time.time()
    result = people_rdbt.find_by_primary_key(pk1,f)
    print("Testing primary key ", pk1, " on table", "People")
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in RDB method is: {0:.3f}s".format(end - start))

    pk2 = ["zl2737", "2018", "2737", "1"]
    start = time.time()
    result = battling_rdbt.find_by_primary_key(pk2)
    print("Testing primary key ", pk2, " on table", "Batting")
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in RDB method is: {0:.3f}s".format(end - start))

    battling_rdbt.delete(r2)
    print("Deleting ", r2, " from table", "Batting")

    people_rdbt.delete(r1)
    print("Deleting ", r1, " from table", "People")

    start = time.time()
    result = people_rdbt.find_by_primary_key(pk1,f)
    print("Testing primary key ", pk1, " on table", "People")
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in RDB method is: {0:.3f}s".format(end - start))

    start = time.time()
    result = battling_rdbt.find_by_primary_key(pk2)
    print("Testing primary key ", pk2, " on table", "Batting")
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in RDB method is: {0:.3f}s".format(end - start))

    people_rdbt.delete(r1)
    print("Deleting ", r1, " from table", "People")

except Exception as e:
    print("Got exception = ", str(e))