import csv
from collections import OrderedDict
import os

class CSVDataTable:
    module_path = os.path.dirname(__file__)
    data_dir = module_path + "/../../Data/"

    # t_name: The "Name" of the collection.
    # t_file: The name of the CSV file. The class looks in the data_dir for the file.
    def __init__(self, t_name, t_file, key_columns):
        if isinstance(t_name, str):
            self.name = t_name
        else:
            raise NameError("The input file name be a string, please double check your input!")
        if isinstance(t_file, str):
            self.file = self.data_dir + t_file
        elif isinstance(t_file, list):
            self.file = "(not from file)"
            self.rows = []
            if len(t_file) > 0:
                for line in t_file:
                    ol = OrderedDict(line)
                    self.rows.append(ol)
        else:
            raise NameError("The input file should be a string or dictionary list, please double check your input!")
        self.keyCol = key_columns
        if key_columns and not isinstance(self.keyCol, list):
            raise NameError('Key columns should be a list, please double check your input!')

    # Pretty print the CSVTable and its attributes.
    def __str__(self):
        length = len(self.rows)
        if len(self.rows) == 1:
            if list(self.rows[0].values()) == ['' for _ in range(len(list(self.rows[0].values())))]:
                length = 0

        s = ""
        s += "Table Name: " + self.name + "; File Root: " + self.file
        s += "; Number of Rows: " + str(length)
        s += "; Key columns: " + str(self.keyCol) + ".\n"
        s += "Column Names" + str(list(self.rows[0].keys())) + ".\n"
        s += "First " + str(min(100,length)) + " row(s):\n"
        col_lst = [i for i in self.rows[0]]
        row_format = "{:<20}" * (len(col_lst) + 1)
        s += row_format.format("", *col_lst) + "\n"
        s += "-" * 20 * (len(col_lst) + 1) + "\n"
        for i, r in enumerate(self.rows):
            if i == 100:
                break
            for item in r.keys():
                if r[item] == None:
                    r[item] = ''
            s += row_format.format("", *list(r.values())) + "\n"
        return s

    # loads the data from the file into the class instance data.
    # You decide how to store and represent the rows from the file.
    def load(self):
        with open(self.file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            self.rows = [row for row in reader]
            pass

    # Obvious
    def save(self):
        with open(self.file, 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.rows[0].keys())
            for data in self.rows:
                writer.writerow(data.values())


    def check_primary_key(self):
        for key in self.keyCol:
            if key not in self.rows[0].keys():
                raise NameError('The primary key contains a column/attribute name not in the file!')

    def find_by_primary_key(self, values, fields=None):
        if not isinstance(values, list):
            raise NameError('Primary keys should be a list, please double check your input!')
        if fields and not isinstance(fields, list):
            raise NameError('Field should be a list, please double check your input!')
        if len(self.keyCol) == 0:
            raise NameError("You don't have a primary key!")
        self.check_primary_key()
        t = {}
        if len(self.keyCol) != len(values):
            raise NameError("The length of the string list is not equal to the supposedly full length of table's primary keys!")
        for i, key in enumerate(self.keyCol):
            t[key] = values[i]
        return self.find_by_template(t, fields)


    # The input is:
    # t: The template to match. The result is a list of rows
    # whose attribute/value pairs exactly match the template.
    # fields: A subset of the fields to include for each result.
    # Raises an exception if the template or list of fields contains
    # a column/attribute name not in the file.
    def find_by_template(self, t, fields=None):
        if not isinstance(t, dict):
            raise NameError('Template should be a dictionary, please double check your input!')
        if fields and not isinstance(fields, list):
            raise NameError('Fields should be a list, please double check your input!')
        self.check_primary_key()
        res = []
        for row in self.rows:
            if row.keys() & t.keys() != t.keys():
                raise NameError('The template contains a column/attribute name not in the file!')
            if dict(row.items() & t.items()) == t:
                if not fields:
                    res.append(dict(row))
                else:
                    d = {}
                    for field in fields:
                        if field not in row.keys():
                            raise NameError('The fields contain a column/attribute name not in the file!')
                        d[field] = row[field]
                    res.append(d)
        if len(res) == 0:
            res = []
            res.append(dict.fromkeys(fields if fields else [i for i in list(self.rows[0].keys())], ""))
        return CSVDataTable("result", res, self.keyCol)

    # Inserts the row into the table.
    # Raises on duplicate key or invalid columns.
    def insert(self, r):
        self.check_primary_key()
        if r.keys() & self.rows[0].keys() != r.keys():
            raise NameError('The row contains a column/attribute name not in the file!')
        template = {}
        for k in self.keyCol:
            if k not in r.keys():
                raise NameError('The row MUST contain a value for each primary key field!')
            template[k] = r[k]
        findrow = self.find_by_template(template).rows[0]
        for k in self.keyCol:
            if findrow[k] == r[k]:
                raise NameError('There already is a row with those primary key values!')
        d = dict.fromkeys(self.rows[0].keys(), None)
        for itm in r.items():
            d[itm[0]] = itm[1]
        self.rows.append(OrderedDict(d))
        self.save()

    # t: A template.
    # Deletes all rows matching the template.
    def delete(self, t):
        self.check_primary_key()
        dt = self.find_by_template(t).rows
        if dt[0] not in self.rows:
            raise NameError('No row matches the deleting template!')
        for r in dt:
            self.rows.remove(r)
        self.save()



if __name__ == "__main__":
    people_csvt = CSVDataTable("People", "People.csv", ["playerID"])
    people_csvt.load()
    try:
        print(people_csvt)
        # t1 = {"nameFirst": "Ted", "nameLast": "Williams"}
        # print("Testing template ", t1, " on table", "People")
        # # result = people_csvt.find_by_template(t1)
        # # print(result)
        # # people_csvt.__str__(result)
        # # print("Query result is ")
        # # print(json.dumps(result, indent=2))
        # # result2 = people_csvt.find_by_primary_key(['willite01'])
        # # print("Query result is ")
        # # print(json.dumps(result2, indent=2))
        # result3 = people_csvt.delete({"nameFirst": "add", "nameLast": "sdd", "playerID": "willite001"})
        # # t1 = {"nameFirst": "add", "nameLast": "sdd"}
        # result = people_csvt.find_by_template(t1)
        # print("Testing template ", t1, " on table", "People")
        # print("Query result is ")
        # print(json.dumps(result3, indent=2))
    except Exception as e:
        print("Got exception = ", str(e))

