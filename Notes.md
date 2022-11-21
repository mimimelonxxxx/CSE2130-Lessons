# CSE2130 - Files and File Structures Notes 

Files are used in programs to store data. That data is often processed by the program to create *information* usable by the program or user. The main advantage to incorporating files into the program is *data persistence*, which means the data lasts beyond the running of the program. 

Files can be used to store settings information for the program, which can be more easily edited using an external editor. It can also be used to store data created by the program for future use. Therefore, files can act as both inputs and outputs to the program, similar to user inputs and outputs. 

Another major advantage to implementing files is that those files can have structures that validate data being inputted. Therefore, the file ensures the integrity of the data. Data Interity is the degere of reliability of the data set. (Databases)

## CRUD in Text Files 

1. Create a text file in Python. To create a file, the file must be opened with write permissions. 

```python
FILE = open("filename.ext", "x") # x indicates that the file is being opened in write mode 

# used to create a default file with parameters 
```

The above function will return a *FileExistsError* if the file already exists. An alternative method is to use the "write plus" setting: 

```python
FILE = open("filename.ext", "w") # w indicates that the file is opened with write settings that will overwrite all of the existing data 

# can change things within a template
# can first read all the data, then overwrite the old data with the new data 
```

NOTE: The program will look for the file relative to its location from the program file. 

If information needs to be added to the end of the text file, use the "a" settings to append. 

```python
FILE = open("filename.ext", "a") # a indicates that the file is being opened and the text is being added to the end of the file 

# let them access the file without actually editing the information in the file 
```

2. Writing to a file requires the `.write(String)` dot function. Once the file is open, new content can be written into the file. NOTE: You can only write a string to a file. 

```python 
FILE = open("filename.ext", "w")
FILE.write("Hello World")
FILE.close() # closes the file after we finished writing/reading it 
```

Note: the `.close()` dot function acts as both save and close. It also removes the file from the memory. 

Note: Multiple `.write()` functions can be written *before* closing the file without deleting the newly written content. It will keep writing where the insertion point is. 

3. Reading a file will extract the text into a list to manipulate. 

```python 
FILE = open("filename.ext") # opens the file as read-only 

# same as 
FILE = open("filename.ext", "r")

CONTENT = FILE.read()
FILE.close() 
print(CONTENT)
```

After the file is opened as read-only, the content can be saved as a string using the `.read()` dot function. To separate each line in the file, `.readlines()` will create a node in a list for each line in the text. 

4. Updating a file requires reading a file to extract the text and then overwriting the file with the new text. 

5. Deleting the content of a file uses the write argument "w" and saves a blank string. For deleting the file, the os library can remove the file. 

```python
import os
os.remove("filename.ext")
``` 

## SQLite Files 

### SQLite and Python 

SQLite is a library that implements a small, fast, self-contained, highly-reliable, full-featured SQL database engine. SQL stands for *Structured Query Language* and is often pronounced *sequel*, making SQLite pronounced as "SQ-Lite" or "sequel lite". While many structures of the query language are similar, there are slight deviations between SQL, SQLite, and other database structures. 

### Databases are tables with column rules

Databases create, update, store, and generally manage data. It can also summarize the data for reporting as information. Information is the interpretation of data for a specific shareholder. 

Databases use **transactions** to manipulate data. A transaction is a group of tasks, that is the smallest possible, that manipulates data or retrieves information. An example of a transaction is withdrawing money from a bank account. 

Databases will provide several advantages over using traditional text or spreadsheet files to store data: 

1. **Concurrency**, where multiple entities can interact with the data at once. Entities in this case can be users, computer programs, or other databases. An integrated database can have multiple applications accessing the same database. 

2. **Atomicity** is the property that states that a transaction performs all tasks to complete the trnasaction or it reverts so that no tasks are complete within the transaction. 

3. **Consistency** is where a transaction cannot fundamentally change the structure of the database (i.e. there is a set number of columns with specific data types within the columns. A transaction cannot change the number of columns or the data types within them). 

4. **Isolation** is where multiple transactions can occur in parallel, but do not affect each other. 

5. **Durability** is wehre the data stored in the database can survive system failure. 

All of these characteristics contribute to **data integrity** by ensuring **data validation** (correct data type) and **verification** (correct value) with each transaction. 

Databases often use an SQL system to manage the database file. (DBMS: Database management system)

### Setup SQLite3 in Python3 

Python is a wrapper to the SQL interface. Therefore, python can interpret SQL statements, but those statements can also be interpreted by other programs. 

Note for IB: only need to include the SQL statements, not the python parts 
For IB, you only need the stuff inside the multiline comments

```python
import sqlite3

FILENAME = "databaseName.db" # an alternative extension is .sqlite

# Connect python to the database. If the database file doesn't exist, then creates the file

CONNECTION = sqlite3.connect(FILENAME) # connects in read and write mode 

# Cursor is the object that executes the SQL commands 

CURSOR = CONNECTION.cursor()
```

On first run, the database file is empty, and tables must be created within the database (think of it like a spreadsheet). 

### Create a Table in the Database 

```python
CURSOR.execute( # always a multi-line comment
    """
    CREATE TABLE student (# uppercase commands, lowercase variables
    # every table needs a primary key, it is the index of the table, the keys are all different
        id INTEGER PRIMARY KEY, 
        first_name TEXT NOT NULL, # column names cannot have spaces 
        last_name TEXT NOT NULL, 
        personal_email TEXT
    );
    """
)

CONNECTION.commit() # validates and saves the changes to the file. 
```

Tables need a primary key, which is a unique identifier of each row of data. Each table can only have one primary key, and no two rows can share the same value for a primary key. In general, primary keys are integers, but they can be more complex when linking multiple tables together. 

Each column must identify the datatype that will appear in that particular column. Common datatypes in SQLite include TEXT, INTEGER, REAL NUMBERIC (float), and BLOB. 

NOT NULL is a column property that indicates that the cell cannot be blank. 

UNIQUE is a column property that indicates that the cell cannot contain a value that is already foudn within the column. 

### Create Data into a Table

```python
CURSOR.execute("""
    INSERT INTO
        student
    VALUES (
        1. 
        "Michelle",
        "Zhang",
        "michellejiang2017@gmail.com"
    );
""")

CONNECTION.commit()
```

NOTE that CURSOR.execute() adds the transaction to the queue, but CONNECTION.commit() validates and saves the changes. 

If the data being entered into the table is arranged in an order that does not match the column order, the order of the data must be specified. Also, if the primary key column is ommitted, and the primary key is an integer value, then the table will **automatically assign** a primary key that is one higher than the highest primary key. 

```python
CURSOR.execute("""
    INSERT INTO
        student (
            last_name, 
            first_name
        )
    VALUES (
        "Zhang",
        "Michael"
    );
""")

CONNECTION.commit()
```

#### Create Data in a Table Using Python Variables 

The SQL commands are strings in python. Therefore using python techniques to insert variables into a string is possible. However, not recommended. Thus the following code block should be avoided. 

```python
INFO = ("Alice", "Wong", "alice.wong@epsb.ca")
CURSOR.execute(f"""
    INSERT INTO 
        student (
            first_name,
            last_name,
            email
        )
        VALUES (
            {INFO[0]},
            {INFO[1]},
            {INFO[2]}
        );
""")
# you could do a SQL attack by inserting SQL commands into the table, which is why this method is bad
```

Note that the above method of inserting variables is susceptible to SQL injection attacks that can alter data or destroy data. Instead, SQLite has an alternative method of introducing variables into the SQL command. 

```python
CURSOR.execute("""
INSERT INTO
    student (
        first_name,
        last_name,
        email
    )
    VALUES (
        ?,
        ?,
        ?
    );
""", INFO)

# inserts the values into the question mark in order

CONNECTION.commit()
```

This method only applies to adding values (i.e. you cannot select columns using this method, because the user won't be the one selecting columns, it is the program that is doing it). Furthermore, the value must be entered as a tuple or a list (even if it is only one value). The values will replace the question marks in the order they appear. 

### Read Data in a Table

There are two methods of reading data in a table, returning the first row that matches the search criteria, or returning all rows that match the search criteria. 

```python
FIRST_MATCH = CURSOR.execute("""
    SELECT
        id,
        first_name,
        last_name,
        email
    FROM
        student
;""").fetchone() 

print(FIRST_MATCH) # (1, Michelle, Jiang, michellejiang2017@gmail.com) 

ALL_MATCHES = CURSOR.execute("""
    SELECT
        first_name,
        last_name
    FROM
        student
;""").fetchall()

print(ALL_MATCHES) # [("Michelle", "Jiang"), ("Alice", "Wong"), ...]
```

When selecting columns, if all columns are required, an asterisk (*) is used. 

### Sort Data in a Query 

Sorting data in a query allows for the results to be returned in a specific order based on a column or series of columns. Ordering the data is most frequently the last part of the SQL query. 

```python
print(CURSOR.execute("""
    SELECT 
        *
    FROM
        student
    ORDER BY
        first_name ASC;
""").fetchall())
```

To chain multiple columns in a sort, separate identified columns with commas (i.e. last_name ASC, first_name DESC) ASC is ascending, and DESC is descending--the default ordering is ASC, so it is only necessary to use DESC.

### Filter Data in a Query

Filtering allows for a partial return of the database date based upon conditions written into the query. 

```python
print(CURSOR.execute("""
    SELECT
        *
    FROM
        student
    WHERE
        first_name = "Michelle";
""").fetchall())
```

NOTE: filtering data goes **BEFORE** sorting data. 

SQLite uses all the same conditional operations as python does (>, <, !=, =, etc), note that equals uses one equals sign, not two. SQLite also uses common logical operators such as OR, AND, and NOT. 

```python
print(CURSOR.execute("""
    SELECT
        *
    FROM
        student
    WHERE
        first_name = "Michelle" 
    AND
        id > 5;
""").fetchall())
```

SQLite can also filter from multiple values within a list 

```python
print(CURSOR.execute("""
    SELECT
        *
    FROM
        student
    WHERE
        first_name in ("Michelle", "Alice");
""").fetchall())
```

ASIDE: The query results can also be limited to a set number of rows

```python
print(CURSOR.execute("""
    SELECT
        *
    FROM
        student
    ORDER BY 
        last_name
    LIMIT 
        2;
""").fetchall())
```

#### Filter Data Using Partial Matches

Partial matches are also called *"fuzzy searches"* or *"fuzzy matches"* where only part of the data needs to match the search criteria. To specify the search pattern, the following characters are allowed. 

* Case sensitivity will remain for all specific characters

* "_" (Underscore) to indicate a single character space that can be any character 

* "%" (Percentage sign) to indicate that zero or more characters 

eg: _ _ _ 2% means that there can be any 3 letters before the 2 and then anything can be after the 2 -- will match CSE2110, SST2170, MAT2971, but will not match CSE1120. (which is why you shouldn't use %2%)

### Update Data in a Table 

**Be cautious when updating existing information.** If the update selects multiple rows, each row will receive the new information. In general, when updating a single row, use the primary key to guarantee returning only **one** value. 

```python
CURSOR.execute("""
    UPDATE
        student
    SET
        first_name = "Mike"
    WHERE
        id = 2;
""")

CONNECTION.commit()
```

### Delete Data in a Table

Similar to updating data in a table, use the primary key whenever possible to ensure deleting an exact row. 

```python
CURSOR.execute("""
    DELETE FROM
        student
    WHERE
        id = 2;
""") # deletes the entire row 

CONNECTION.commit()
```

#### Deleting a full table

To delete a table, the entire table including its title will no longer be in the database. Therefore, any code directly relating to the table name will **output an error**. To delete a table, use the following command. 

```python
CURSOR.execute("""
    DROP TABLE
        student;
""")
```

# Normalization (IB)

*Normalization* adjusts the data within a table into a standard configuration so that the SQL Queries can be more easily process information. The normalization rules are developed by *Edgar Codd*, who came up with the first three rules of normalization. 

## First Normalization Form (1NF)

Every field in the table must be filled. (Another way of saying this is that all cells cannot be empty.)

NOTE: Null cells usually do not count for 1NF. However, there is no formal rule against them. IB DOES NOT count Null as a filled cell. 

Separate tables into multiple tables using the primary key (as a foreign key) to link the rows together. 

## Second Normalization Form (2NF)

Every column of data must be related to the primary key. The *primary key* is a unique value within a column. Unique values, which is also a column setting, are ones where the column does not have a repeated value. 

NOTE: While there can be many columns set to enforce unique values, only one column (or set of columns is considered the primary key). 

Typically, each table is unique for each set of data and they all match a foreign key. 

## Third Normalization Form (3NF)

Every column does not have secondary relational data separate from the primary key. In order words, one column cannot depend on the information of another column that is not part of the primary key. 

At the end, typically you would create a conglomerate table that references all the information necessary as foreign keys. 

* All tables in 2NF and 3NF have a primary key 

    * Primary keys can also be a composition of two or more columns. Then the key is called a primary composite key. 
    
    * Foreign key is a column of primary keys from another table. The foreign key is used to create references to the other tables. 