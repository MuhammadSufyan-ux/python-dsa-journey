#In this lecture we are going to learn about the dictionary and its all methods in Python programming language for example:

from unicodedata import name


std1={
    "name":"sufyan",
    "class":"BS Artificial Intelligence and Data Science" ,
    "age":18
    }
print(std1)



# The difference between List and Dictionary in python programming is that List is a collection of items in particular order and Dictionary is a collection  of items in key value pair format :

# like 

# LIST:
# in list we can have data like this:
# std2=["sufyan", " ali ", " ahmed ", " salman "]
# key:index(1,2,3,4)
# student[0]


# DICTIONARY:
# in dictionary we can have data like this:
# std3={name:"sufyan", "class":"BS Artificial Intelligence and Data Science" , "age":18}
# key:name , class , age 
# student["name"] 


# to acces value from teh dictionary we use this method in python for example:
std2={
    "name":"sufyan",
    "class":"BS Artificial Intelligence and Data Science" ,
    "age":18
    }


# print keyword then use parentheses then indetifiers getting the value from dic and then us the square bracketes that print specefic key and its vlaue 
print(std2["name"])
print(std2["age"])




# to add data further which are not cyrrently existing in the dic we us ethis method 
std3={
    "name":"Umair",
    "age":25,
    "designation":"Software Engineer"
    }

std3["city"]="Swabi"
std3["experience"]=11

print(std3)











# to change existing value in python DIC we use this method :
std4={
    "name":"Umair",
    "age":25,
    "designation":"Software Engineer"
    }

std4["age"]=26
std4["name"]="khan Umair"

print(std4)





# In Dic the data is also in the list like the following code :

std5={
    "name":"M Sufyan",
    "age":18,
    "skill":["python", "DSA", "Web and App Dev" , "AI model embeding "]

}

print(std5.get("age"))
# also we can use this synthax and method like the below:
print(std5["name"])
print(std5.get("skill"))







# The Difference between Print(())   and Print([]) in python is that , that given below :

# Print(())                                     |           Print([])
# this is uesed with                            |          this is used with
# getting key value from                        |         getting key value from
# dcitionary list data                          | dictionary list but not exit then give me erROR of synthax error and not                      give                                            |key value is not existing in the dic 
# not give me error if                          |None           
# key value is not
# existing in the dic
# KeyError: 'city'



student={
    "name":"sufyan",
    "age":18,

}

# print(student["city"])
print(student.get("city"))
