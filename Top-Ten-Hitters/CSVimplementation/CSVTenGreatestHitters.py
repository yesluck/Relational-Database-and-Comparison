import sys
sys.path.append("../../CSVDataTable/src")
from CSVDataTable import *

def top_ten_hitters():
    people_csvt = CSVDataTable("People", "People.csv", ["playerID"])
    batting_csvt = CSVDataTable("Batting", "Batting.csv", ["playerID", "yearID", "teamID", "stint"])
    appearances_csvt = CSVDataTable("Appearances", "Appearances.csv", ["yearID", "teamID", "playerID"])
    people_csvt.load()
    batting_csvt.load()
    appearances_csvt.load()

    r = {}
    for row in batting_csvt.rows:
        if r.__contains__(row['playerID']):
            r[row['playerID']]['career_at_bats'] += int(row['AB'])
            r[row['playerID']]['career_hits'] += int(row['H'])
            r[row['playerID']]['first_year'] = min(r[row['playerID']]['first_year'], row['yearID'])
            r[row['playerID']]['last_year'] = max(r[row['playerID']]['last_year'], row['yearID'])
        else:
            r[row['playerID']] = {}
            r[row['playerID']]['playerID'] = row['playerID']
            r[row['playerID']]['first_name'] = list(people_csvt.find_by_template({'playerID' : row['playerID']}, fields = ['nameFirst', 'nameLast']).rows[0].values())[0]
            r[row['playerID']]['last_name'] = list(people_csvt.find_by_template({'playerID' : row['playerID']}, fields = ['nameFirst', 'nameLast']).rows[0].values())[1]
            r[row['playerID']]['career_hits'] = int(row['H'])
            r[row['playerID']]['career_at_bats'] = int(row['AB'])
            r[row['playerID']]['career_average'] = 0
            r[row['playerID']]['first_year'] = row['yearID']
            r[row['playerID']]['last_year'] = row['yearID']
    for player in list(r.items()):
        r[player[0]]['career_average'] = (r[player[0]]['career_hits'] / r[player[0]]['career_at_bats'] if r[player[0]]['career_at_bats'] != 0 else 0)
    res = list(r.values())
    res = sorted(res, key = lambda k: k['career_average'], reverse=True)
    final = list(filter(lambda k : (k['last_year'] >= '1960' and k['career_at_bats'] > 200), res))
    return final[0:10]
