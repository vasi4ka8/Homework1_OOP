class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if self.grades:
            total_grades = sum([sum(grades) for grades in self.grades.values()])
            num_grades = sum([len(grades) for grades in self.grades.values()])
            return round(total_grades / num_grades, 2)
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_grade}\n'
                f'Курсы в процессе изучения: {in_progress}\n'
                f'Завершенные курсы: {finished}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if self.grades:
            total_grades = sum([sum(grades) for grades in self.grades.values()])
            num_grades = sum([len(grades) for grades in self.grades.values()])
            return round(total_grades / num_grades, 2)
        return 0

    def __str__(self):
        avg_grade = self.average_grade()
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {avg_grade}')

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_grade_students(students, course):
    total_grades = 0
    count_grades = 0
    for student in students:
        if course in student.grades:
            total_grades += sum(student.grades[course])
            count_grades += len(student.grades[course])
    if count_grades == 0:
        return 0
    return round(total_grades / count_grades, 2)

def average_grade_lecturers(lecturers, course):
    total_grades = 0
    count_grades = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades += sum(lecturer.grades[course])
            count_grades += len(lecturer.grades[course])
    if count_grades == 0:
        return 0
    return round(total_grades / count_grades, 2)

student1 = Student('Ruoy', 'Eman', 'male')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Введение в программирование']

student2 = Student('John', 'Doe', 'male')
student2.courses_in_progress += ['Python']
student2.finished_courses += ['Git']

lecturer1 = Lecturer('Some', 'Lecturer')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Another', 'Lecturer')
lecturer2.courses_attached += ['Python']

reviewer1 = Reviewer('Some', 'Reviewer')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Another', 'Reviewer')
reviewer2.courses_attached += ['Python']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 8)

student1.rate_lecturer(lecturer1, 'Python', 10)
student1.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 8)

print(student1)
print()
print(student2)
print()
print(lecturer1)
print()
print(lecturer2)
print()
print(reviewer1)
print()
print(reviewer2)

students = [student1, student2]
lecturers = [lecturer1, lecturer2]

print("\nСредняя оценка студентов по курсу 'Python':", average_grade_students(students, 'Python'))
print("Средняя оценка лекторов по курсу 'Python':", average_grade_lecturers(lecturers, 'Python'))

print("\nСравнение студентов:")
print(student1 > student2)

print("\nСравнение лекторов:")
print(lecturer1 > lecturer2)