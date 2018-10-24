import sys
sys.path.append("../../../CSV/src")
from CSVTenGreatestHitters import *
import time

try:
    # insert people -> insert batting -> delete battling -> delete people -> delete people(raise error)

    people_csvt = CSVDataTable("People", "People.csv", ["playerID"])
    people_csvt.load()
    battling_csvt = CSVDataTable("Batting", "Batting.csv", ["playerID", "yearID", "teamID", "stint"])
    battling_csvt.load()

    r1 = {"playerID": "zl2737", "nameFirst": "Zikun", "nameLast": "Lin"}
    people_csvt.insert(r1)
    print("Inserting ", r1, " into table", "People")

    r2 = {"playerID": "zl2737", "yearID": "2018", "teamID": "2737", "stint": "1"}
    battling_csvt.insert(r2)
    print("Inserting ", r2, " into table", "Batting")

    pk1 = ["zl2737"]
    f = ["playerID", "nameFirst", "nameLast"]
    start = time.time()
    result = people_csvt.find_by_primary_key(pk1, f)
    print("Testing primary key ", pk1, " on table", "People")
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in CSV method is: {0:.3f}s".format(end - start))

    pk2 = ["zl2737", "2018", "2737", "1"]
    start = time.time()
    result = battling_csvt.find_by_primary_key(pk2)
    print("Testing primary key ", pk2, " on table", "Batting")
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in CSV method is: {0:.3f}s".format(end - start))

    battling_csvt.delete(r2)
    print("Deleting ", r2, " from table", "Batting")

    people_csvt.delete(r1)
    print("Deleting ", r1, " from table", "People")

    start = time.time()
    result = people_csvt.find_by_primary_key(pk1, f)
    print("Testing primary key ", pk1, " on table", "People")
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in CSV method is: {0:.3f}s".format(end - start))

    start = time.time()
    result = battling_csvt.find_by_primary_key(pk2)
    print("Testing primary key ", pk2, " on table", "Batting")
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in CSV method is: {0:.3f}s".format(end - start))

    people_csvt.delete(r1)
    print("Deleting ", r1, " from table", "People")

except Exception as e:
    print("Got exception = ", str(e))