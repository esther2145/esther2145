
####1 Write a python program to determine the length of a string without using the built-in len()function
# Define the input string
string = "hello, world!"

# Initialize a counter to 0
length = 0

# Iterate through each character in the string
for char in string:
    # Increment the counter for each character
    length += 1

# Print the result
print("String: ",string)
print("The length of the string is:", length)

#2 write a python program to count the occurrences of each character in string
# Define the input string
input_string = "programming"

# Initialize an empty dictionary to store character counts
char_count = {}

# Iterate through each character in the string
for char in input_string:
    # If the character is already in the dictionary, increment its count
    if char in char_count:
        char_count[char] += 1
    # Otherwise, add the character to the dictionary with a count of 1
    else:
        char_count[char] = 1

# Print the result
print("String ; ",input_string)
print("Character counts:")
for char, count in char_count.items():
    print(f"{char}: {count}")

#4 write a python programm to concatenate two strings and swap their first two characters
# Define the input strings
string1 = "abc"
string2 = "xyz"

# Swap the first two characters of each string and concatenate the results
swapped_string1 = string2[:2] + string1[2:]
swapped_string2 = string1[:2] + string2[2:]
concatenated_string = swapped_string1 + " " + swapped_string2

# Print the result
print("Strings:",string1,string2)
print("Concatenated string after swapping first two characters:", concatenated_string)

#7 write a python program to remove characters at odd indices from a string
# Define the input string
input_string = "Computer Science"

# Initialize an empty string to store the result
output_string = ""

# Iterate through the string with a step of 2
for index in range(0, len(input_string), 2):
    # Append characters at even indices to the output string
    output_string += input_string[index]

# Print the result
print("String:",input_string)
print("String after removing characters at odd indices:", output_string)

#10 write a python program to reverse a string
# Define the input string
string_1 = "Python"

# Initialize an empty string to store the reversed string
reversed_string = ""

# Iterate through the input string in reverse order and append each character to reversed_string
for i in range(len(string_1) - 1, -1, -1):
    reversed_string += string_1[i]

# Print the reversed string
print("String:",)
print("Reversed string:", reversed_string)

#12 write a python program to reverse words in a given string
# Define the input string
string_2 = "Hello World"

# Split the input string into words
words = string_2.split()

# Reverse the list of words
reversed_words = words[::-1]

# Join the reversed words back into a string
reversed_string = ' '.join(reversed_words)

# Print the reversed string
print("String:",string_2)
print("String with reversed words:", reversed_string)

#16 write a python program to compute the sum of digits in a string
# Define the input string
string_3 = "Hello 1234"

# Initialize sum of digits to 0
sum_of_digits = 0

# Iterate through each character in the string
for char in string_3:
    # Check if the character is a digit
    if char.isdigit():
        # Convert the character to an integer and add to sum_of_digits
        sum_of_digits += int(char)

# Print the sum of digits
print("String:",string_3)
print("Sum of digits in the string:", sum_of_digits)

#18 write a python program to count uppercase, lowercase, special characters and numericc values in a string
# Define the input string
string_4 = "Hello123!@#"

# Initialize counters
uppercase_count = 0
lowercase_count = 0
special_count = 0
numeric_count = 0

# Iterate through each character in the string
for char in string_4:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        numeric_count += 1
    else:
        special_count += 1

# Print the counts
print("String:",string_4)
print("Uppercase letters:", uppercase_count)
print("Lowercase letters:", lowercase_count)
print("Numeric values:", numeric_count)
print("Special characters:", special_count)

#20 write a python program to find the index of a substring in a string
# Define the main string and the substring to search for
main_string = "python is powerful"
substring = "is"

# Find the index of the substring in the main string
index = main_string.find(substring)

#getting the output
print("String:",main_string)
print("substring:",substring)
print("index of substring:",index)

#21 write a python program to swap caes of characters in a string
# Define the input string
string_5 = "Hello World!"

# Initialize an empty string to store the result
swapped_string = ""

# Iterate through each character in the input string
for char in string_5:
    # Check if the character is uppercase
    if char.isupper():
        # Convert it to lowercase and append to swapped_string
        swapped_string += char.lower()
    # Check if the character is lowercase
    elif char.islower():
        # Convert it to uppercase and append to swapped_string
        swapped_string += char.upper()
    else:
        # Append non-alphabetic characters directly to swapped_string
        swapped_string += char

# Print the result
print("String:",string_5)
print("String after swapping cases:", swapped_string)

