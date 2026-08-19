value1=int(input("Enter your 1st number: "))
operator=input("Enter your operator: ")
value2=int(input("Enter your 2nd number: "))

addition=(value1+value2)
subtract=(value1-value2)
multiply=(value1*value2)
division=(value1/value2)


if(operator=="+"):
    print(addition)
elif(operator=="-"):
    print(subtract)
elif(operator=="*"):
    print(multiply)
elif(operator=="/"):
    print(division)



else:
    print("enter correct operation please!")



