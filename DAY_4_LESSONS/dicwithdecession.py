std1={
    "name":"sufyan",
    "age":18,
    "class":12,
    "marks":
    {
        "english":30,
        "Urdu":45,
        "Computer":90
    }     
}


for subject, mark in std1["marks"].items ():
    if mark >= 33:
        print(subject, "Pass")
    else:
        print(subject, "Fail")