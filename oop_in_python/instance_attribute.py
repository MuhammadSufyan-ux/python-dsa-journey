# today i learn about the different tyoe of attribute in Python OOP programming next lesson is give below
class MyClass:
    def __init__(self , name , age , subject):
        self.name=name #these three var are called "INSTANCE ATTRIBUTE" , INSTANCE ATTRIBUTE are those values which can be separate separate for everyone , Everyone  have own value ...
        self.age=age
        self.subject=subject
    def NowPrint(self):
        print(f"My name is {self.name} , I'm {self.age} old and my subject is {self.subject}")
student1=MyClass("sufyan", 18 , "BSDS")
student2=MyClass("salman", 35 , "BSCS")

student1.NowPrint()
student2.NowPrint()


