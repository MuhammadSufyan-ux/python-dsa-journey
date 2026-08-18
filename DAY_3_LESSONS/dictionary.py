#In this lecture we are going to learn about the dictionary and its all methods in Python programming language for example:

from unicodedata import name


std1={
    "name":"sufyan",
    "class":"BS Artificial Intelligence and Data Science" ,
    "age":18
    }
print("------ This is result of general Dictionary data ------")
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
print("------ This is result of specific key vlaue accesing in Dictionary data ------")
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


print("------ This is result of adding further key and its vlaue to Dictionary data ------")
print(std3)











# to change existing value in python DIC we use this method :
std4={
    "name":"Umair",
    "age":25,
    "designation":"Software Engineer"
    }

std4["age"]=26
std4["name"]="khan Umair"



print("------ This is result of of changing key anb its value in Dictionary data ------")
print(std4)





# In Dic the data is also in the list like the following code :

std5={
    "name":"M Sufyan",
    "age":18,
    "skill":["python", "DSA", "Web and App Dev" , "AI model embeding "]

}
print("------ This is result of for showing print.get(())  and print([]) in Dictionary data ------")
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










# in this i leanr about the keys() method and then practice on it 
# This is give me the list all data that are in left side of teh key value pair in the dic in python programming language for example:
keyExp={
    "name":"Zaif UR Rehman",
    "age":35,
    "Designation":"Graphic designer and computer Operator ",
    "city":"Swabi"
}
print("------ This is result of showing only key of Dictionary data ------")
print(keyExp.keys())

# the OUTPUT is this 
# dict_keys(['name', 'age', 'Designation', 'city'])







# in this session im learn about the value() method that used with Dic key list printing 
# value give me right side data that are declared in the Dic in key list
student1={
    "name":"Salman",
    "age":34,
    "Designation":"Business Man", 
    "City":"Swabi",
    "Income":3000000

}
print("------ This is result of showing key value of Dictionary data ------")
print(student1.values())


# This is output of the above code in python programming language for example:
# dict_values(['Salman', 34, 'Business Man', 'Swabi', 3000000])







# In this session im learn about teh items() method that used with Dic key list printing
# this is used to print Key and value pair in teh Dic in Python programming language for example:
# This concept is used mostly in the for loop in python programming language for example:
student2={
    "name":"Salman",
    "age":34,
    "Designation":"Business Man", 
    "City":"Swabi",
    "Income":3000000
}
print("------ This is result of showing key and its vlaue both showing in this form name:Sufyan in Dictionary data ------")
print(student2.items())










# If i want to update multiple key value pair in the Dic we used this method update() in python programming language for example:
student3={
    "name":"Salman",
    "age":34,
    "Designation":"Business Man", 
    "City":"Swabi",
    "Income":3000000
}


student3.update({
    "name":"Sufyan",
    "age":18,
    "Designation":"Student"

})

print("------ This is result of updating old data with new data in Dictionary data ------")
print(student3)

# OUTPUT is this 
# {'name': 'Sufyan', 'age': 18, 'Designation': 'Student', 'City': 'Swabi', 'Income': 3000000}


# first make the dictionary data with key and list and then make another Dic with function method student3.update and no using of = equal sign and then use teh parenthesis and then curly barckets and then add the different data for the updating current data 







# in this series of learning im learn about pop() method that drop item from teh Dic key and list both remove 
student4={
    "name":"Salman",
    "age":34,
    "Designation":"Business Man", 
    "City":"Swabi",
    "Income":3000000
}

student4.pop("Designation")
print("------ This is result of removing items with key and its value from Dictionary data ------")
print(student4)

# OUTPUT is this 
# {'name': 'Salman', 'age': 34, 'City': 'Swabi', 'Income': 3000000}







# in this series of learning im learn about popitem() method that drop item from teh end of Dic key and list both remove 
student5={
    "name":"Salman",
    "age":34,
    "Designation":"Business Man", 
    "City":"Swabi",
    "Income":3000000
}

student5.popitem()
print("------ This is result of removing last item from  Dictionary data ------")
print(student5)

# OUTPUT is this 
# {'name': 'Salman', 'age': 34, 'Designation': 'Business Man', 'City': 'Swabi'} in this is teh last item removed succesfully







# to delete the items from teh Dic list we can use this method del()

student6={
    "name":"Salman",
    "age":34,
    "designation":"Business Man", 
    "city":"Swabi",
    "income":3000000
}

del student6["age"]
del student6["income"]
print("------ This is result of deleting any mentioned items from Dictionary data ------")
print(student6)

# OUTPUT is this 
# {'name': 'Salman', 'designation': 'Business Man', 'city': 'Swabi'}










# In this series of learning im learn about teh clear() that clear all data 
student7={
    "name":"Salman",
    "age":34,
    "Designation":"Business Man", 
    "City":"Swabi",
    "Income":3000000
}
student7.clear()

print("------ This is result of clearing all data that are written in Dictionary data ------")
print(student7)

# The OUTPUT is :
# {}













# This is summary of all above method and code concepts
# | Method / operation | Kaam                |
# | ------------------ | ------------------- |
# | `dict["key"]`      | Value access        |
# | `get()`            | Safely value access |
# | `keys()`           | All keys            |
# | `values()`         | All values          |
# | `items()`          | Keys + values       |
# | `update()`         | Add/update multiple |
# | `pop()`            | Specific key remove |
# | `popitem()`        | Last item remove    |
# | `clear()`          | Everything remove   |
# | `del`              | Specific key delete |
