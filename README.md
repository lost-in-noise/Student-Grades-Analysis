# Student Grades Analysis 📝

This Python project analyzes a list of students with unique names and their test scores to extract useful insights such as unique grades, top performers, and students who failed.

## Project Objective 🎯

The goal is to analyze the given data to:
- Extract and print all unique grades.
- Identify and print the names of the top three students with the highest scores.
- Identify and print the names of students who scored below 51, along with their scores.

## Data 📊

The student data is represented as a list of tuples containing student names and their respective scores:

```python
students = [
    ("Alice", 85),
    ("Bob", 78),
    ("Charlie", 92),
    ("David", 85),
    ("Eve", 78),
    ("Frank", 85),
    ("Mark", 50),
    ("George", 21)
]
```

## Features 🚀
1. Unique Grades
Extracts and prints all unique grades from the list of student scores, sorted in descending order.

2. Top Performers
Identifies and prints the names of the top three students with the highest scores.

3. Failed Students
Identifies and prints the names of students who scored below 51, along with their scores.

## How It Works ⚙️
Unique Grades: A set is used to store unique scores, which are then sorted in descending order.
Top Performers: The list of students is sorted by score in descending order, and the top three are selected.
Failed Students: A list comprehension is used to filter out students who scored below 51.

## Requirements 🛠️
Python 3.12.5