age=18
if age==18:
  print("You are eligible for voting")



# using elif
age=int(input("Enter Your age: "))
if age>=18:
  print("You are eleigible")
elif age<=18:
  print("You are not eligible")
else:
  print("You are eligible after few years")



#   using IF , ELIF , ELSE 

mark = int(input("Enter Your mark: "))

if mark >= 60:
    print("You are eligible for BS admission")

# elif mark == 60:
#     print("You are not eligible for BS admission")

elif mark == 50:
    print("You are eligible if you increase your marks greater than", mark)
