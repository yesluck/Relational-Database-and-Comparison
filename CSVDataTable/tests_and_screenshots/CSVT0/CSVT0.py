import sys
sys.path.append("../../../CSVDataTable/src")
from CSVDataTable import *


try:
    people_csvt = CSVDataTable("People", "People.csv", ["playerID"])
    people_csvt.load()
    print(people_csvt)
except Exception as e:
    print("Got exception = ", str(e))