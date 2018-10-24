import sys
sys.path.append("../")
from RDBTenGreatestHitters import *
import time

try:
    print("Query result for Top Ten hitters is: ")
    start = time.time()
    result = top_ten_hitters()
    end = time.time()

    col_lst = list(result[0].keys())
    row_format = "{:<20}" * (len(col_lst) + 1)
    s = row_format.format("", *col_lst) + "\n"
    s += "-" * 20 * (len(col_lst) + 1) + "\n"
    for i, r in enumerate(result):
        if i == 100:
            break
        for item in r.keys():
            if r[item] == None:
                r[item] = ''
        s += row_format.format("", *list(r.values())) + "\n"
    print(s)

    print("Query time in RDB method is: {0:.3f}s".format(end-start))
except Exception as e:
    print("Got exception = ", str(e))