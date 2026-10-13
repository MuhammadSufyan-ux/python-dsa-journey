# in this lecture i learn about file handling 
file = open("filehandling.txt" , "w")
file.write("This is series of learning, \n file handling ")
file.close()

# now i am learn about the opening of file in read mode in this lecture
file=open("filehandling.txt" , "r")
sufyan=file.read()
print(sufyan)
file.close()



# in write function i learn about more readline and readlines function in this lecture
# "with "  here used for closes existing opened file when block is finished
with open("filehandling.txt" , "r")  as file:
    print(file.readline(4))
    print(file.readline(5))
    print(file.readline(6))
    print(file.readline(7))


    print(file.readlines())



# in thgis series of learning i learn about teh append it mean append function 
# "a" this is used to add new data in existing file without deleting the existing data
with open("filehandling.txt" , "a") as file:
    file.write("\n This is new data added in existing file without deleting the existing data")
    file.close()





# in this series o flearning i lern about the replacing of word or sentence in existing file without deleting the existing data


# this is for readinga nd checking the data \
with open("filehandling.txt" , "r") as file:
    data=file.read()

    # this is for replacing the data in existing file without deleting the existing data
    data=data.replace("This is series of learning, \n file handling" , "This is series of learning, \n file handling and this is new data added in existing file without deleting the existing data")
    file.close()

    # this is for rewriting the data in existing file without deleting the existing data
    with open("filehandling.txt", "w") as file:
        file.write(data)