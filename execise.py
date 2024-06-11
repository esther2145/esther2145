print("Welcome to simple calculator:)")
print("huuray lets get started")
#asking the user for the first number
num_1=int(input("Please enter the first number:"))
#asking the user for the operator to use
print("select 1 for addition, 2 for subtraction, 3 for multiplication and 4 for division")
print("1.+")
print("2.-")
print("3.*")
print("4./")
#storing the operator
operator = int(input("what operator: "))
#asking for the second number
num_2=int(input("Please enter the second number:"))
print("Wonderful:)")

right_number = 0
#performing addition
if operator ==1:
    print("What is",num_1,"+",num_2)
    right_number = num_1 + num_2
#performing subtration    
if operator == 2:
    print("What is",num_1,"-",num_2)
    right_number = num_1 - num_2
#performing multiplication
if operator == 3:
    print("What is",num_1,"*",num_2)
    right_number = num_1 * num_2
#performing division    
if operator == 4:
    print("What is",num_1,"/",num_2)
    right_number = num_1 / num_2

#storing the users answer
ans=int(input())
if right_number == ans:
    print("correct keep it up :)")
else:
    print("wrong answer. the right answer =",right_number)    

