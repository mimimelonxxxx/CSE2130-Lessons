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

2. Writing to a file requires the `.write(String)` dot function. Once the file is open, new content can be written into the file. 

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

