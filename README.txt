README for COMS W4111 HW1


Part 1: Design Choices

1.1 __init__(), load()
These functions serve as initialization functions of the class. Also they will raise errors immediately (see Part 3) when they detect an error in the inputs.
In CSVDataTable, “self.rows” is a dictionary list containing the whole table. However, in RDBDataTable, this variable only contains the first 100 rows of the table, which can be used in __str__() function.
In RDBDataTable, the function also need a variable to define the connection to the database.

1.2 __str()__
This function aims to pretty print the XXXDataTable and its attributes (table name, number of rows, key columns, column names, first X (at most 100) row(s) of the table).

1.3 load(), save()
This function are only used in CSVDataTable, to convert between the “.csv” file and the dictionary list “self.row”.

1.4 find_by_template()
This function checks if some rows in the data table fits the template by calculating the intersection of the rows in table and the given template t. In CSVDataTable, if the intersection is equal to t, it means all the information in t fits this row, then add this row into the result. In RDBDataTable, I used the templateToWhereClause() function to help select the rows that fits the template.

1.5 find_by_primary_key()
This function checks if some rows in the data table fits the primary key by setting a template and calling the find_by_template() function in CSVDataTable. On the other hand, in RDBDataTable, I defined a new primaryKeyToWhereClause() function to help select the rows that fits the primary keys.

1.6 insert()
This function allows users to insert a row into the table. In CSVDataTable, I append the row into the dictionary list and then call the save() function to save the new table. In RDBDataTable, I used a simple “Insert” sentence to implement this feature.

1.7 delete()
This function allows users to delete a row from the table. It calls find_by_template() function to find the needed rows according to the given template. And then in CSVDataTable, I remove the row from the dictionary list; while in RDBDataTable, I used the “Delete” sentence. However, we shouldn’t delete rows in “People” table directly due to the foreign key constraint (and this error would be raised by mysql).



Part 2: Running My Code

2.1 Top-Ten-Hitters
Run the “TenGreatestHitterTest.py” codes in “CSVimplementation” folder and “RDBimplementation” folder. And it’s easy to find that RDB takes much less time to find out the results.

2.2 Test Cases and Screenshots
In folders “CSVT0” to “CSVT4” and “RDBT0” to “RDBT4”, there are testing programs that can be used to test the functions and the outputs. Sometimes one program contains more than one test cases, in which un-used codes should be commented-out. Each test case corresponds to a screenshot.



Part 3: My Chosen Correctness Rules

3.1 When initializing the XXXDataTable
3.1.1 If the input name is not a string, it will raise an error "The input file name be a string, please double check your input!"
3.1.2 If the input file is not a string or a dictionary list, it will raise an error "The input file should be a string or dictionary list, please double check your input!"
3.1.3 If the input key columns is not a list, it will raise an error “Key columns should be a list, please double check your input!”
3.1.4 When every function is called, it will first examine whether every primary key is contains a column/attribute name in the CSVDataTable. If not, it will raise an error “The primary key contains a column/attribute name not in the file!”
3.1.5 When initializing the RDBDataTable, if the primary keys are not the same with the real primary keys, it will print out a warning “Warning: The primary key defined in the main function is different from the real primary key!” And then it will set the key_columns into the correct primary key list.
3.1.6 When initializing the RDBDataTable, if the connection is not valid, it will raise an error “Please input the right connection!”

3.2 When finding by template
3.2.1 If the input template is not a dictionary, it will raise an error “Template should be a dictionary, please double check your input!”
3.2.2 If the input fields is not a list, it will raise an error “Fields should be a list, please double check your input!”
3.2.3 If the template contains a column / attribute name not in the file, it will raise an error “The template contains a column/attribute name not in the file!”
3.2.4 If the fields contain a column / attribute name not in the file, it will raise an error “The fields contain a column/attribute name not in the file!”

3.3 When finding by primary key
3.3.1 If the input primary key values is not a list, it will raise an error “Primary keys should be a list, please double check your input!”
3.3.2 If the table don’t have a primary key, it will raise an error “You don't have a primary key!”
3.3.3 If the length of the input primary key values is not equal to the number of the primary keys, it will raise an error “The length of the string list is not equal to the supposedly full length of table's primary keys!”
3.3.4 Other errors already defined in Part 3.2.

3.4 When inserting rows
3.4.1 If the row doesn’t contain values of the primary keys, it will raise an error "The row MUST contain a value for each primary key field!"
3.4.2 Duplicate key error: “There already is a row with those primary key values!”
3.4.3 Other errors already defined in Part 3.2.

3.5 When deleting rows
3.5.1 If no row matches the deleting template, raise an error “No row matches the deleting template!”
3.5.2 Other errors already defined in Part 3.2.