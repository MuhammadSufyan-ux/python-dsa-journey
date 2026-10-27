# In this section i was learned about the class attirbute detailed are shared below :

class Teacher:
    department="Computer Scinece" # this is "CLASS ATTRIBUTE" here the university var are initialized insid eteh class and outside the main __init__ function , when we do it then it is called "CLASS ATTRIBUTE".
    def __init__(self, name , subject):
        self.name=name
        self.subject=subject
    def NowPrint(self):
        print(f"My name is {self.name} , I'm teaching {self.subject} and my department is {self.department}.")
teacher1=Teacher("Mr. Qamar Ali" , "Programming fundamentals")


teacher1.NowPrint()
