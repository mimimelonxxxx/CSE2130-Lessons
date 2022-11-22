"""
title: Grade Average Calculator
author: Michelle Jiang
date-created: 2022-11-20
"""

### VARIABLES ### 
import sqlite3
import pathlib

FILENAME = "e_grades.db"
FIRSTRUN = True

if (pathlib.Path.cwd() / FILENAME).exists(): 
    FIRSTRUN = False 

CONNECTION = sqlite3.connect(FILENAME)
CURSOR = CONNECTION.cursor()

### FUNCTIONS ###

# INPUTS # 

def menu():
    """
    view the menu and select how to interact w the database
    :return: int
    """
    print("""
1. Add course information 
2. Update course information
3. Calculate average
4. Exit 
    """)
    CHOICE = int(input("> ")) # assume intelligence 
    return CHOICE 

def addCourse():
    """
    user adds course information
    :return: None
    """
    global CURSOR, CONNECTION
    COURSEID = input("Course ID: ")
    NAME = input("Course name: ")
    CATEGORY = input("Course category: ")
    GRADE = input("Student grade: ")
    COURSES = [COURSEID, NAME, CATEGORY, GRADE]
    for i in range(len(COURSES)):
        if COURSES[i] == "":
            COURSES[i] = None
    
    CURSOR.execute("""
    INSERT INTO
        courses (
            id, 
            name, 
            category,
            student_grade
        )
    VALUES (
        ?,
        ?,
        ?,
        ?
    ); 
    """, COURSES)

    CONNECTION.commit()

def getCourse():
    """
    user chooses a course to update the grade
    :return: str -> course id 
    """
    # print out all the courses 
    COURSES = CURSOR.execute("""
    SELECT
        id,
        name,
        category,
        student_grade
    FROM
        courses
    ORDER BY
        id,
        name;
    """).fetchall()
    
    for i in range(len(COURSES)):
        print(f"{COURSES[i][0]} | {COURSES[i][1]} | {COURSES[i][2]} | {COURSES[i][3]}")

    # select a course by its course id
    ID = input("Please input the course ID: ")

    return ID

# PROCESSING # 

def setup(): 
    """
    creates the database table on first run 
    :return: None
    """
    global CURSOR, CONNECTION 
    CURSOR.execute("""
    CREATE TABLE 
        courses ( 
            id TEXT NOT NULL PRIMARY KEY, 
            name TEXT NOT NULL, 
            category TEXT NOT NULL,
            student_grade INTEGER 
        ); 
    """)
    CONNECTION.commit()

def updateGrade(COURSE):
    """
    updates grade with a new grade
    :param COURSE: str -> course id 
    :return: None
    """
    global CURSOR, CONNECTION
    GRADES = CURSOR.execute("""
    SELECT
        student_grade
    FROM
        courses
    WHERE
        id = ?;
    """, [COURSE]).fetchone()

    print("Leave blank for no changes ")
    NEWGRADE = input(f"Grade: ({GRADES[0]}) ")

    if NEWGRADE == "":
        NEWGRADE = {GRADES[0]}
    
    INFO = [NEWGRADE, COURSE]

    CURSOR.execute("""
    UPDATE
        courses
    SET
        student_grade = ? 
    WHERE
        id = ?; 
    """, INFO)

    CONNECTION.commit()

    print(f"{COURSE} sucessfully updated! ")

# OUTPUTS # 

### MAIN PROGRAM CODE ###
if __name__ == "__main__":
# INPUTS #
    if FIRSTRUN == True:
        setup()
# PROCESSING #
    while True:
        CHOICE = menu()
        if CHOICE == 1: # add course
            addCourse()
        elif CHOICE == 2: # update course 
            COURSE = getCourse()
            updateGrade(COURSE)
        elif CHOICE == 3: # calculate average 
            pass
        # OUTPUTS # 
        elif CHOICE == 4:
            exit()

