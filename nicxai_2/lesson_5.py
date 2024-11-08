import sqlite3


class SDataBase:
    def __init__(self, name='school.db'):
        self.connect = sqlite3.connect(name)

        self.cursor = self.connect.cursor()
        self.cursor1 = self.connect.cursor()

        self.create_students()
        self.create_grades()

    def create_students(self):
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS students(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL
                        )
                        """)
    def create_grades(self):
        self.cursor1.execute("""
                    CREATE TABLE IF NOT EXISTS grades(
                        student_id INTEGER NOT NULL,
                        subject TEXT NOT NULL,
                        grade INTEGER NOT NULL
                        )
                        """)
        
    def add_stdnt(self, student):
        self.cursor.execute("""INSERT INTO students (name, age) VALUES (?,?)""",(student.name, student.age))
        self.connect.commit()

    def add_grd(self, grade):
        self.cursor1.execute("""INSERT INTO grades (student_id, subject, grade) VALUES (?,?,?)""", (grade.student_id, grade.subject, grade.grade))
        self.connect.commit()

    def get_subjects_grades(self, student_id):
        self.cursor1.execute("""SELECT subject, grade FROM grades WHERE student_id=?""",(student_id,))
        return self.cursor1.fetchall()

    def get_grades(self, student_id):
        self.cursor1.execute("""SELECT grade FROM grades WHERE student_id=?""",(student_id,))
        return self.cursor1.fetchone()
    
    def get_all_students(self):
        self.cursor.execute("""SELECT * FROM students""")
        return self.cursor.fetchall()

    def get_all_grades(self, student_id):
        self.cursor1.execute("""SELECT * FROM grades WHERE student_id=?""", (student_id,))
        return self.cursor1.fetchall()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Grade:
    def __init__(self, student_id, subject, grade):
        self.student_id = student_id
        self.subject = subject
        self.grade = grade



class School:
    def __init__(self, name='school.db'):
        self.db = SDataBase(name)

    def add_student(self, student):
        self.db.add_stdnt(student)
        print('Успешно!')
    
    def add_grade(self, grade):
        self.db.add_grd(grade)

    def show_student_grades(self, student_id):
        for subject, grade in self.db.get_subjects_grades(student_id):
            print(f'\n{grade} - {subject}')
    
    def avarage_grade(self, student_id):
        grades = self.db.get_grades(student_id)
        print(sum(grades) / len(grades))

    def _show_all(self):
        for id, name, age in self.db.get_all_students():
            print(f'\n{id} -- {name} -- {age}')
            for student_id, subject, grade in self.db.get_all_grades(id):
                print(f'{student_id} -- {subject} -- {grade}')
            print()

school = School()

while True:
    try:
        oper = int(input('\n1 - add student\n2 - add grade\n3 - show student grades\n4 - avarage grade\n'))
    except ValueError:
        print('Value Error')
    if oper == 1:
        name = input('name: ')
        age = int(input('age: '))
        school.add_student(Student(name, age))
    elif oper == 2:
        student_id = int(input('student id: '))
        subject = input('\nMathematic\nHistory\nBiology\nSciense\nGeography\nLiterature\nRussian\nEnglish\n')
        grade = int(input('grade: '))
        school.add_grade(Grade(student_id, subject, grade))
    elif oper == 3:
        student_id = int(input('student id: '))
        school.show_student_grades(student_id)
    elif oper == 4:
        student_id = int(input('student id: '))
        school.avarage_grade(student_id)
    elif oper == 69:
        school._show_all()
