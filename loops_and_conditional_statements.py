#2 Write a python program to guess a number between 1 and 20
import random
# Generate a random number between 1 and 20
secretNumber = random.randint(1, 20)

print("Hello there")
print('I am thinking of a number between 1 and 20.')

# Declare integer variable to store the number of guesses
guessesTaken = 0

# Loop until the correct number is guessed
while True:
    guessesTaken += 1
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break
print("Well Guessed!:)")

#3 Write a python program to construct the following pattern,using a nested for loop
size = 5
# Triangle Pattern
for i in range(size):
    for j in range(i+1):
        print("#", end="")
    print()    
def inverted_left_triangle(n):
    for i in range(n, 0, -1):
        # Print stars for the current row
        print("#" * i)

# Example usage:
inverted_left_triangle(5)

# Function to reverse a string
def reverse_string(word):
    return word[::-1]
#4 Write a program that accepts a word from the user and reverses it 
# Main program
if __name__ == "__main__":
    # Take input from user
    user_input = input("Enter a word: ")

    # Reverse the input word
    reversed_word = reverse_string(user_input)

    # Print the reversed word
    print("Reversed word:", reversed_word)

# 5 Write a python program to count the number of numbers divisible by 13ina series of numbers.
# Accept a series of numbers from the user, separated by spaces
numbers = (13,25,39,65,52,92,88)                                                              

# Initialize a counter for numbers divisible by 13
count_divisible_by_13 = 0

# Iterate through the list and count numbers divisible by 13
for num in numbers:
    if num % 13 == 0:
        count_divisible_by_13 += 1

# Display the count
print("Number of numbers divisible by 13:", count_divisible_by_13)

# 8 Write a python program to create a multiplication table for a given number
# Accept a number from the user
number = int(input("Enter a number to create its multiplication table: "))

# Specify the range for the multiplication table
table_range = 10  # This will create a table from 1 to 10

# Generate and display the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, table_range + 1):
    print(f"{number} x {i} = {number * i}")

#12 Write a python program that accepts and calculates the number of uppercase letters and lowercase letters
# Accept a string from the user
input_string = input("Enter a string: ")

# Initialize counters for uppercase and lowercase letters
uppercase_count = 0
lowercase_count = 0

# Iterate through each character in the string
for char in input_string:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1

# Display the counts
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)

#13 Write a python program to check the validity of passwords input by users. Give feedback about the validity of the password, telling them what is missing.
import re

def check_password(password):
    # Initialize a list to collect feedback
    feedback = []
    
    # Check the length of the password
    if len(password) > 16:
        feedback.append("Password must be less than 16 characters long.")
    if len(password) < 8:
        feedback.append("Password must be atleast 8 characters long ")

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        feedback.append("Password must contain at least one lowercase letter.")
        
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        feedback.append("Password must contain at least one uppercase letter.")
        
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        feedback.append("Password must contain at least one digit.")
        
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password must contain at least one special character.")

    # Return the feedback
    if feedback:
        return "Password is not valid: " + ", ".join(feedback)
    else:
        return "Password is valid."

# Accept a password from the user
password = input("Enter a password: ")

# Check the validity of the password and provide feedback
result = check_password(password)
print(result)

#39 Write a python program to check whether a number is positive, negative or zero.
# Accept a number from the user
number = float(input("Input a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(number,"is a positive number.")
elif number < 0:
    print(number,"is a negative number.")
else:
    print(number,"is a zero.")

#14 write a python program that prints the alphabet pattern 'B'
def print_pattern_B():
    pattern=[
        "****",
        "*   *",
        "*   *",
        "****",
        "*   *",
        "*   *",
        "****"
    ]
    for line in pattern:
        print(line)
print_pattern_B()

#15 Write a python program that prints the alphabet pattern "C"
def print_pattern_C():
    pattern=[
        " ***",
        "*",
        "*",
        "*",
        "*",
        " ***"
    ]
    for line in pattern:
        print(line)
print_pattern_C()    
 # 16 Write a python program that prints the alphabet pattern "F"
def print_pattern_F():
    pattern=[
        "******",
        "*",
        "*",
        "****",
        "*",
        "*",
        "*"
    ]    
    for line in pattern:
        print(line)
print_pattern_F()        

#50 Write a python program to construct the following pattern, using a nested loop number.
list = 10
# number Pattern
for i in range(list):
    for _ in range(list -i -1):
        print(" ", end="")

    for j in range(i+1):
        print(j, end="")    
    print()

