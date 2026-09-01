# today i learn about teh function in the python programming langugae that what is function and how many type is founded in python so let gets started 
# the word def is use to defined function it is used for declaring for machine that this is function and you run it as a function 
def greet():  #here the greet is called function name or arguments
    print("Lets begin with functions and its all method in this series of learning Python programming.")

# now we call the function wihtout the calling function the code dont give us any response
greet()
greet()
greet()


# if we self pass parameter and arguments during function calling then the code is written in belwo style 
def std_1(name , age , university , rollno):
    print("student name :" , name)
    print("student age :" , age)
    print("student university :" , university)
    print("student university :" , rollno)


# this is function arguments passing during function calling 
std_1("sufyan", 18 , "University of Swabi" , 2324)




# in this section we learn about the return function
def square(number):
    return number * number

answer = square(5)
print(answer + 10)





# let learn these concept
def modify(x):
    x.append(4)

a = [1, 2, 3]
modify(a)

print(a)


# program no2 

def modify(x):
    x = x + [4]

a = [1, 2, 3]
modify(a)

print(a)