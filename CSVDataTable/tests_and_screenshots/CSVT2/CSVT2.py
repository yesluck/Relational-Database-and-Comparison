import sys
sys.path.append("../../../CSV/src")
from CSVTenGreatestHitters import *
import time


try:
    people_csvt = CSVDataTable("People", "People.csv", ["playerID"])
    people_csvt.load()
    t = {"nameFirst": "Ted", "birthMonth": "10"}
    f = ["playerID", "nameFirst", "nameLast", "birthYear", "birthMonth", "birthDay"]    # Screenshot_csv2-1
    # f = []  # Screenshot_csv2-2
    # f = ["firstName"]   # Screenshot_csv2-3
    # f = "playerID"      # Screenshot_csv2-4
    print("Testing template ", t, ", fields", f, " on table", "People")
    start = time.time()
    result = people_csvt.find_by_template(t, f)
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in CSV method is: {0:.3f}s".format(end - start))
except Exception as e:
    print("Got exception = ", str(e))