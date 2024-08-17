# Data
students = [("Alice", 85), ("Bob", 78), ("Charlie", 92), ("David", 85), ("Eve", 78), ("Frank", 85), ("Mark", 50), ("George", 21)]

# 1. Unique Grades
def get_unique_grades(students):
    grades = {score for _, score in students}
    return sorted(grades, reverse=True)

# 2. Top Performers
def get_top_performers(students, top_n=3):
    sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
    return sorted_students[:top_n]

# 3. Failed Students (Score below 51)
def get_failed_students(students, passing_score=51):
    failed_students = [(name, score) for name, score in students if score < passing_score]
    return failed_students

# Output
print("Unique Grades:", get_unique_grades(students))

top_performers = get_top_performers(students)
print("\nTop Performers:")
for name, score in top_performers:
    print(f"{name}: {score}")

failed_students = get_failed_students(students)
print("\nFailed Students:")
for name, score in failed_students:
    print(f"{name}: {score}")
