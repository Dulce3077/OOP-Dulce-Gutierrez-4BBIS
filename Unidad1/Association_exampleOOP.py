class Student:
    def __init__(self,name):
        self.name = name

    def enroll(self,course):
        self.course = course
        
    def show_course(self):
        print(f"{self.name} is enrolled in {self.course.name}")

# def __init__ es la función automática para cada clase. A la hora de escribir student1 = Student("Carlos"),
#   le estamos diciendo a python que le enviamos "Carlos" y que queremos crear un objeto de esta clase.
#   Python automáticamente busca la función __init__ en la clase y ejecuta esta función.


class Course:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Course: {self.name}")

# Instances
student = Student("Carlos")
course = Course("Python Programming")

# Creating a relationship
student.enroll(course)

# Use the Relationship
student.show_course()
# Output expected: "Carlos is enrollen in Python Programming"