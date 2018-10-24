import sys
sys.path.append("../../../CSV/src")
from CSVTenGreatestHitters import *
import time


try:
    people_csvt = CSVDataTable("People", "People.csv", ["playerID"])
    people_csvt.load()
    t = {"nameFirst": "Ted", "nameLast": "Williams"}    # Screenshot_csv1-1
    # t = {}                                              # Screenshot_csv1-2
    # t = {"firstName": "Ted", "nameLast": "Williams"}    # Screenshot_csv1-3
    # t = ["Ted", "Williams"]                             # Screenshot_csv1-4
    print("Testing template ", t, " on table", "People")
    start = time.time()
    result = people_csvt.find_by_template(t)
    print("Query result is: ")
    end = time.time()
    print(result)
    print("Query time in CSV method is: {0:.3f}s".format(end - start))
except Exception as e:
    print("Got exception = ", str(e))