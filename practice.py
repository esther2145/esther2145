
import random

tries = 0

def roll_dice_until_doubles():
    global tries  # Declare tries as global
    
    doubles = False

    while not doubles:
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)

        print(f'Rolled {roll1} and {roll2}')

        if roll1 == roll2:
            print(f'Doubles! in {tries} tries!')
            doubles = True

        tries += 1

roll_dice_until_doubles()

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def find_primes(limit):
    primes_found = 0
    for num in range(2, limit+1):
        if is_prime(num):
            primes_found += 1
            print(f"{num} is a prime number.")

            if primes_found == 5:
                print("Found 5 primes. Stopping.")
                break
        
        else:
            pass 

find_primes(50)

# Accept a series of numbers from the user, separated by spaces
numbers = (13,25,39,65,52)                                                              

# Initialize a counter for numbers divisible by 13
count_divisible_by_13 = 0

# Iterate through the list and count numbers divisible by 13
for num in numbers:
    if num % 13 == 0:
        count_divisible_by_13 += 1

# Display the count
print("Number of numbers divisible by 13:", count_divisible_by_13)



# Accept a number from the user
number = int(input("Enter a number to create its multiplication table: "))

# Specify the range for the multiplication table
table_range = 10  # This will create a table from 1 to 10

# Generate and display the multiplication table
print(f"Multiplication table for {number}:")
for i in range(1, table_range + 1):
    print(f"{number} x {i} = {number * i}")
