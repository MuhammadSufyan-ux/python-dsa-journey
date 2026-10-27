# let start here from object and class in python language
class Student:
    def __init__(self, name , age , rollno , program):
        self.name= name 
        self.age = age
        self.rollno = rollno
        self.program= program

    def introduce(self):
        print(f"My name is {self.name} , I'm {self.age} old , my roll number is {self.rollno} and my program name is {self.program}")
student1 = Student("Muhammad Sufyan" , 13  , 3445 , "BS Data Science and AI.")
student2 = Student("Muhammad Salman" , 14 , 3435 , "BS Data Science.")
student3 = Student("Muhammad Umair" , 15 , 3453 , "BS CS.")
student4 = Student("Muhammad Sudais" , 16 , 3435 , "BS SE.")

student1.introduce()
student2.introduce()
student3.introduce()
student4.introduce()
