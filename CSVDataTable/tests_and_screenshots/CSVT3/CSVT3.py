import sys
sys.path.append("../../../CSV/src")
from CSVTenGreatestHitters import *
import time


try:
    people_csvt = CSVDataTable("Batting", "Batting.csv", ["playerID", "yearID", "teamID", "stint"])
    people_csvt.load()
    pk = ['bellast01', "1871", "TRO", "1"]      # Screenshot_csv3-1
    # pk = ['bellast01', "1871", "TRO"]           # Screenshot_csv3-2
    # pk = ['bellast01', "1871", "WRONG", "1"]    # Screenshot_csv3-3
    # pk = 'bellast'                              # Screenshot_csv3-4
    f = ["playerID", "yearID", "teamID", "stint", "AB", "H"]
    print("Testing primary key ", pk, " on table", "Batting")
    start = time.time()
    result = people_csvt.find_by_primary_key(pk,f)
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in CSV method is: {0:.3f}s".format(end - start))
except Exception as e:
    print("Got exception = ", str(e))