# # Program no: 1
# # to take input from user and then print it on screen 

std_name=input("Enter your name : ")
std_age=int(input("Enter your age : "))

print(f"Your name is : {std_name} and your age is : {std_age}  ")




# # program no: 2
# To take input 2 nbumber from user for add sub multiply and divison 
a=int(input("Enter your first number : "))
b=int(input("Enter your second number : "))

add=a+b 
sub=a-b
mult=a*b
modu=a%b

print(f"The addtion of {a} and {b} is :  " , add)
print(f"The subtraction of {a} and {b} is :  " , sub)
print(f"The multiplication of {a} and {b} is :  " , mult)
print(f"The modulos of {a} and {b} is :  " , modu)



# program no: 3
# Take the input from user and then print the sum of integer and float number
a=int(input("Enter an integer number: " ))
b=float(input("Enter your floating number: " ))
c=a+b
print(type(float(c)))
# print(type(c))



# Program no: 4
# Take the number from user and print it with different data type
# take input 
user_input=input("Enter your number : ")

# change type of each
as_int=int(user_input)
as_float=float(user_input)
as_str=str(user_input)


print("The integer value is : ", as_int , " and its datatype is : ", type(as_int))
print("The float value is : ", as_float , " and its datatype is : ", type(as_float))
print("The string value is : ", as_str , " and its datatype is : ", type(as_str))







# Porgram no :5
# To evaluate the expression and print it rsult on screen as a output
x=10+3*2**2
print("The result of the expression is : ", x)
print(f"The result is {x} because accoridng to BODMAS rule it is evaluate first : 2**2=4 then \n multiply it with 3 and  then plus it result with 10 therefore teh final result is {c}")


# Program no :6
# enter two number by user and then swap it and print the result on screen
int1=int(input("Enter your first number : "))
int2=int(input("Enter your second number : "))

int1 , int2 = int2 , int1
print(f"The first number is : {int1} and the second number is : {int2} after swapping it")







# Program no :7
# WAP to take input in string type and then chage it to float type , tyen calculate and print it.
celsius_temp=str(input("Enter your temperature in celsius : "))
as_float=float(celsius_temp)
faren_temp=(as_float*9/5)+32
print(f"The tempreture finally in Farenheit is: {faren_temp}")








# Program no : 8
# Take the radius (r) as user input and print the area. Use the formula: Area = π×r2 (value of π = 3.14)
# to take the radius from os import write

radius=int(input("Enter the radius of circle : "))
area=3.14*radius**2
print(f"The area of circle with radius {radius} is : {area}")



# Program no:9
# Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest: SI = (P ×R×T)/100
rate=float(input("Enter the rate of interest : "))
principle=float(input("Enter the principle amount : "))
time=float(input("Enter the time in years : "))
simple_interest=(principle*rate*time)/100
print(f"The simple interest is : {simple_interest}")






# Program no: 10
# Take a decimal number as input (like 45.78) and output its: • integer part– 45 • fractional part– .78
decimal_no=float(input("Enter your decimal number : "))
integer_part=int(decimal_no)
fractional_part=decimal_no-integer_part #here we are subtracting the integer part from the decimal number to get the fractional part
print(f"The integer part is : {integer_part} and the fractional part is : {fractional_part}")

