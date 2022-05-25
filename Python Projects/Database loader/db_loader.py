""" Write a program to continuously take input for student details from console or html form,
the user should be able to add multiple student details at once. The data should be saved in a database.
Once the data is saved, the user should be able to edit and delete.
The delete option should allow for bulk delete."""

import pandas as pd
import mysql.connector
user1= input("Enter the username of the sql user: ")
passwd1= input("Enter the password: ")
mydb = mysql.connector.connect(host='localhost', user=user1, passwd=passwd1)
mycursor = mydb.cursor(buffered=True)


# Creating Functions.
# Function to add new entries.
def st_details():

    entries = int(input("Enter the number of entries you want to add: "))
    for i in range(0, entries):
        print("Enter the details: ")
        varss = {}
        query1 = f"insert into {tabs1[tc]} values("
        for j in range(0, len(columns1)):
            key = f"{columns1[j]}1"
            value = input(f"Enter the value for {columns1[j]}: ")
            varss[key] = value
            if j == (len(columns1) - 1):
                query1 = query1 + f"\"{varss[key]}\")"
            elif j != (len(columns1) - 1):
                query1 = query1 + f"\"{varss[key]}\", "
        # query2 = f"insert into stu_data values('{name}', '{doa}', {age2}, {grade2})"
        # insert into anime values("drag's", "1", "2014", "high")
        query2 = query1
        mycursor.execute(query2)
        mydb.commit()


# Function to edit and delete the data inside the table and database
def e_n_d():
    action2 = (input("Press e to the the edit the details of the students\n"
                     "Press d to delete the entries from the database: "))

    if action2 == 'e':
        col_list = columns1.copy()
        col1 = input('Enter the name of the column: ')
        val1 = input('Enter the new value for the column: ')
        for col in col_list:

            if col == col1:
                col_list.remove(col)
        val2 = input(f'Enter the value for the {col_list[0]} in that row: ')
        val3 = input(f'Enter the value for the {col_list[1]} in that row: ')

        query2 = f"update stu_data set {col1} = '{val1}' where {col_list[0]}  = '{val2}' and {col_list[1]} = '{val3}'"
        mycursor.execute(query2)
        mydb.commit()
    if action2 == 'd':
        entries = int(input("Enter the number of entries you want to delete: "))
        for i in range(0, entries):
            val1 = input(f"Enter the name of the {columns1[0]} whose data you want to delete: ").lower()
            # val2 = int(input(f"Enter the age of {val1}: "))
            query3 = f"delete from {tabs1[tc]} where {columns1[0]} = \"{val1}\""
            mycursor.execute(query3)
            mydb.commit()


# Funtion to load the selected table
def loader():
    mycursor.execute(f"show columns from {tabs1[tc]}")
    columns1 = []
    d_col = []
    for col in mycursor:
        columns1.append(col[0])
    data2 = {}
    query7 = f"select * from {tabs1[tc]}"
    mycursor.execute(query7)
    result = mycursor.fetchall()
    for item in result:
        d_col.append(item)
    data3 = pd.DataFrame(d_col, columns=columns1)
    print(data3)


# Function to Show the List of the tables
def tables():
    mycursor.execute('show tables')
    tabs = {}
    i = 1
    for db in mycursor:
        str1 = f"{db}".split("'")
        tabs[i] = str1[1]
        i += 1
    return tabs


# Selecting Database
cond = True
while(cond):
    query4 = f"show databases"
    mycursor.execute(query4)
    dbs = {}
    print("Code: Databases")
    i = 1
    for db in mycursor:
        str1 = f"{db}".split("'")
        dbs[i] = str1[1]
        print(f"{i}: {dbs[i]}")
        i += 1
    dbc = int(input("Enter the code of the database from the list: "))
    database1 = dbs[dbc]

    # Executing with the selected database
    mydb = mysql.connector.connect(host='localhost', user=user1, passwd=passwd1, database=database1)
    mycursor = mydb.cursor(buffered=True)
    tabs1 = tables()

    if tabs1:
        cond = False

# Selecting Table and Printing it.
print("Code: Tables")
for i in range(0, len(tabs1)):
    print(f"{i+1}: {tabs1[i+1]}")
tc = int(input("Enter the code of the table from the list: "))
mycursor.execute(f"show columns from {tabs1[tc]}")
columns1 = []
d_col = []
for col in mycursor:
    columns1.append(col[0])
data2 = {}
query7 = f"select * from {tabs1[tc]}"
mycursor.execute(query7)
for item in mycursor:
    d_col.append(item)
data3 = pd.DataFrame(d_col, columns=columns1)
print(data3)

# Choosing Action Whether to Add Entries or Edit Database
cond1 = True
while cond1:
    action1 = int(input("Press 1 to add more entries\n"
                        "Press 2 to the edit and delete entries from the database: "))
    if action1 == 1:
        st_details()
        query = f"select * from {tabs1[tc]}"
        mycursor.execute(query)

    elif action1 == 2:
        e_n_d()
        query = f"select * from {tabs1[tc]}"
        mycursor.execute(query)

    loader()

    #  Creating action in such a way so that user can perform the app more efficiently.
    action2 = int(input("Press 1 to continue\n"
                        "Press 2 to go back\n"
                        "Press 3 to exit: "))
    if action2 == 1:
        if action1 == 1:
            st_details()
        elif action1 == 2:
            e_n_d()
    elif action2 == 2:
        cond1 = True
    elif action2 == 3:
        cond1 = False
        exit()


