choice = input("SignUp or Login: ")
username = input("Enter your Username: ")
email = input("Enter your Email: ")
password = input("Enter your Password: ")

if choice == "SignUp":
    print(f"User {username} signed up successfully with email {email}")
elif choice == "Login":
    if email == "sufyan@gmail.com" and password == "sufyan123":
        print(f"User {email} logged in successfully")
    else:
        print("Invalid email or password")
else:
    print("Invalid choice")
