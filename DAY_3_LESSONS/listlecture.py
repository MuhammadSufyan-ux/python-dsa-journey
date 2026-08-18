#  to print list in python i write the following code:
from operator import index


students= ["sufyan", "Ali", "Ahmed "]
print (students)


# to acces each elements of lsit i write the following code:
students= ["sufyan", "Ali", "Ahmed "]
print(students[0])


# also i can acces the elements from right side to write the following code:
students= ["sufyan", "Ali", "Ahmed "]
print(students[-2])



# writting the for sytax and rules for list in python:
# 1 sythax of list is 
s1=["sufyan ", 34, 3.4 , True]
print(s1)



# to access the elements of list we can use for loop also in python 
sufyan=["sufyan", "Ali", "Ahmed "]
for i in sufyan:
    print(i)




# to replace elements of list in python the following logic we can use for example:
replaceEle=["sufyan", " ali ", " ahmed ", " salman "]
replaceEle[1]="salman bahijan"
print(replaceEle)





# to add new elements in teh list we can use teh append() method in python for example:
addEle=["sufyan", " ali ", " ahmed ", " salman "]
addEle.append("I add the Suhail khan in the list")
print(addEle)




# ITS FOR SINGLE ELEMENTS ONLY
# The append() method usually used to add elements in teh end of list but i want to add the elements in specific index we can use the insert() method in python for example:
 
insertexp=["sufyan", " ali ", " ahmed ", " salman "]
insertexp.insert(2, "I add the slaman khan in the list on the index 2")
print(insertexp)





# for multiple elements we can use the extend() method in python for example:
# to extend teh list elements from another list in python we can us eteh extend() method for example:
std1=["sufyan", " ali ", " ahmed ", " salman "]
std2=["suhail", " ali ", " ahmed ", " salman "]
std1.extend(std2)
print(std1)




# to remove the elements from the list endiging we can use the pop() method in python for example:
# TO REMOVE ELEMENTS FROM LIST IN PYTHON WE CAN USE THE POP() METHOD FOR EXAMPLE:
std3=["sufyan", " ali ", " ahmed ", " salman "]
std3.pop(1)
print(std3)





# to remove the specific elements from the list we can use the remove() method in python for example:
std4=[1, 2, 3, 4]
std4.remove(2)
print(std4)







# to clear the list data we can use the clear() method in python for example:
std5=[1, 2, 3, 4 ,"sufyan" , " class 34" ," khushnuma"]
std5.clear()
print(std5)




# to find list elements that the elements are in whihc index 
std6=["sufyan", " ali ", " ahmed ", " salman "]
print(std6.index("sufyan"))





# to check teh elements are present in list how many ti me we can use the count() method in python for example:
std7=["sufyan", " ali ", " ahmed ", " salman ", "sufyan"]
print(std7.count("sufyan"))




# to sort un sorted data in python we can use sort() method in python on un formatted data for example:
std8=[3, 4, 5, 2,1,7,8,9]
std8.sort()
print(std8)



# to reverse data in the list we can use the reverse() method in python for example:
std9=[3, 4, 5, 2,1,7,8,9]
std9.reverse()
print(std9)






# to copy the list data in python we can use the copy() method in python for example:
std10=[3, 4, 5, 2,1,7,8,9]
std11=std10.copy()
print (std11)


# | Method      | Kaam                      |
# | ----------- | ------------------------- |
# | `append()`  | End mein 1 item add       |
# | `insert()`  | Specific position par add |
# | `extend()`  | Multiple items add        |
# | `remove()`  | Value remove              |
# | `pop()`     | Index/item remove         |
# | `clear()`   | Sab remove                |
# | `index()`   | Value ka index            |
# | `count()`   | Value ki frequency        |
# | `sort()`    | Sort                      |
# | `reverse()` | Order reverse             |
# | `copy()`    | List ki copy              |
