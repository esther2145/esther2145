#creating a sign up program
print("SIGN UP")
#ask the user for their names
fname = input("What is your first name: ")
lname = input("What is your last name: ")
#asking for email and password
email = input("what is your email address : ")
password = input("create a password: ")

print("NEW SIGN IN")
ask_email = input("Enter you email: ")

if ask_email ==email:
    new_password =input("Enter the password: ")
    if new_password == password:
        print("SUCCESS")
    else:
        print("INCORRECT PASSWORD")    
else:
    print("INCORRECT EMAIL ADDRESS")   

print("WELCOME TO MY SYSTEM")     