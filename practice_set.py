"""
#input/output
#1 
user_name = input("what is your name: ")
print(f"Hello {user_name}! :)")

#2
num_1 = float(input("give a number:"))
num_2 = float(input("give another number:"))
sum = num_1 + num_2
diff = num_2 - num_1
prd = num_1*num_2
quo = num_1//num_2
remainder = num_1%num_2
print(f"the sum of {num_1} and {num_2} is {sum}")
print(f"the difference of {num_1} and {num_2} is {diff}")
print(f"the product of {num_1} and {num_2} is {prd}")
print(f"the quotient of {num_1} and {num_2} is {quo}")
print(remainder)
"""
#3 
sent = ("am gonna have a good day")
length = str(len(sent))
print(f"the number of letters in ({sent}) is ",length)
#one way of calculating the number of words
fun = sent.split()
count_sent = len(fun)
print(count_sent)
#second way of calculating the number of words
fun = len(sent.split())
print(fun)
# calculating using only one line of code
print(len((input("ether a sentence: ")).split()))
#calculating using a fuction 
def count_words(sent):
    words = sent.split()
    num_words = len(words)
    return num_words
print(count_words(sent))

#conditional statements
#1
num = 23
if num %2 ==0:
    print("it is an even number")
else:
    print("it is an odd number")    

#2 ask a year and determine if its a leap year
enter = int(input("give a year: "))


