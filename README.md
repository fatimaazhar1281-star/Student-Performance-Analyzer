# Student Performance Analyzer

A console-based Python application that collects student marks, analyzes individual academic performance, and generates class-level statistics for multiple students.

## Objective

The objective of this project is to practice fundamental Python programming concepts by building a small data-processing application.

The program allows users to enter multiple students and their subject marks, then calculates individual performance metrics and overall class statistics.

## Features

### Student Performance Analysis

For each student, the program calculates:

* Average marks
* Highest mark
* Lowest mark
* Letter grade
* Pass/Fail status

### Multiple Student Support

The program can process multiple students during a single session and stores their records in a nested dictionary.

### Subject Management

* Subjects are entered once at the beginning of the program.
* Subjects are separated using commas.
* Empty and invalid subject entries are rejected.
* Duplicate subjects are automatically removed.

### Input Validation

The program validates:

* Student names
* Subject names
* Marks between 0 and 100
* Invalid numerical input
* Duplicate student names
* Empty inputs

### Class-Level Statistics

After entering all students, the program calculates:

* Total number of students
* Number of passed students
* Number of failed students
* Overall class average
* Class topper based on average marks
* Lowest individual mark in the class

## Python Concepts Used

This project applies the following Python concepts:

* Variables and data types
* Strings and string methods
* Lists
* Dictionaries
* Nested data structures
* Functions
* Function parameters and return values
* `for` loops
* `while` loops
* `if / elif / else`
* `try / except`
* User input
* Input validation
* Dictionary iteration
* Basic data aggregation
* String formatting with f-strings

## Data Structure

Student records are stored using a nested dictionary structure.

Conceptually:

```text
class_records
│
├── Student 1
│   ├── Subject 1 → Marks
│   ├── Subject 2 → Marks
│   └── Subject 3 → Marks
│
├── Student 2
│   ├── Subject 1 → Marks
│   ├── Subject 2 → Marks
│   └── Subject 3 → Marks
│
└── ...
```

This structure allows the program to associate each student with their individual subject marks and later perform class-level aggregation.

## How It Works

The program follows these steps:

1. The user enters the subjects, separated by commas.
2. The program validates and cleans the subject list.
3. The user enters a student's name.
4. Marks are collected for each subject.
5. Input validation ensures that marks are whole numbers between 0 and 100.
6. The student's marks are stored in the class records.
7. Individual performance statistics are calculated and displayed.
8. The process continues until the user enters `exit`.
9. The program then iterates through all stored student records.
10. Class-level statistics are calculated and displayed.

## Grading System

The program uses the following grading scale:

|  Average | Grade |
| -------: | :---: |
|   90–100 |   A   |
|    80–89 |   B   |
|    70–79 |   C   |
|    60–69 |   D   |
| Below 60 |   F   |

A student is considered **Passed** when their average is 50 or above.

## Example Output

```text
=== Welcome to the Class Performance Analyzer ===

Enter Subjects (separated by commas): English, Biology, Mathematics
Validated Subjects Tracked: English, Biology, Mathematics

Enter Name (or type "exit" to view final class stats): Sara
Enter marks for English: 92
Enter marks for Biology: 88
Enter marks for Mathematics: 95

------------------------------
Student    : Sara
Average    : 91.67
Highest    : 95
Lowest     : 88
Grade      : A
Status     : Passed
------------------------------

Enter Name (or type "exit" to view final class stats): Ali
Enter marks for English: 75
Enter marks for Biology: 68
Enter marks for Mathematics: 82

------------------------------
Student    : Ali
Average    : 75.00
Highest    : 82
Lowest     : 68
Grade      : C
Status     : Passed
------------------------------

Enter Name (or type "exit" to view final class stats): exit

=========================================
         FINAL CLASS STATISTICS
=========================================
Total Students Processed : 2
Students Passed          : 2
Students Failed          : 0
Overall Class Average    : 83.33
Class Topper             : Sara (Avg: 91.67)
Lowest Mark in Class     : 68 (Scored by: Ali)
=========================================
```

## Future Improvements

Possible extensions for future versions include:

* Exporting student records to CSV
* Subject-wise class statistics
* Student ranking
* Performance visualization using Matplotlib
* Reading and processing existing datasets
* Storing records in a database
* Converting the project into a pandas-based data analysis workflow

## Project Status

**Completed — Python Week 01 Project**

This project is part of my Python learning journey, with a focus on developing programming fundamentals through practical projects.

