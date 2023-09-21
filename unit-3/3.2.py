class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(students):
    return sorted(students, key=lambda student: student.cgpa, reverse=True)

# creating student objects
s1 = Student('Peter', '1', 3.2)
s2 = Student('Amy', '2', 3.8)
s3 = Student('John', '3', 3.5)

# sorting students
sorted_students = sort_students([s1, s2, s3])

# printing sorted students
for student in sorted_students:
    print(f'{student.name}, {student.roll_number}, {student.cgpa}')
