# to check that the string is ending with my sam ekey word or not 
str="This is day 4 of learning python from different source through internet and other sources"
print(str.endswith("ces"))
print(str.endswith("sources"))
print(str.endswith("python"))






# in session i learn about teh capitalization of start charater of teh word
str1="this is day 4 of learning python from different source through internet and other sources"
print(str1.capitalize())

# another method
str1="this is day 4 of learning python from different source through internet and other sources"
str2 = str1.capitalize()
print(str2)








#  In this series of learning i learn about the replace any character in the word through the following code
str3="Hmair khan developer"
str4 = str3.replace("H", "U")
print(str4)
# another way of writing code
print(str3.replace("H","U"))




#  In this series of learning i learn about the find any word through the following code
str3="Hmair khan developer"
str4 = str3.find("khan")
print(str4)
# another way of writing code
print(str3.find("developer"))



# in this series  of learning code i learn about the count() function of finding wording accurence in string that word exist how many time 
str="in this series  of learning code i learn about the count() function of finding wording accurence in string that word exist how many time "
print(str.count("in"))
print(str.count("the"))
str2=str.count("of")
print(str2)