"""
This idea came from a lack of understanding in some methods of coding Python,
so i decided to create a quiz that will give various prompts to code in python from bsaic to advanced.
My goal is to have users be able to activley learn in real time at their own pace 
& hone their skills 
"""

print("Welcome to Python P! \n A learning experience that will \n help you improve your Python coding")

# I will ask the user what they would like to practice, the will need a variable 
# using "Input" will allow the user to actively type in the console when prompted 
studying = input("Do you want to practice writing code? ")

# a if statement would be required for their repsonse, if they say anything other than yes then close the code 
if studying.lower() != "yes":
    quit()
    
print("Okay! Let's Begin")
score = 0

# All code up to line 20 is good what ever error i encounter will be from line 21 and on 

answer = input ("Define a function that prints a ''Hello, World!' \n ")
expected_answer =  "def greet(): print('Hello, World!')"
if answer.strip() == expected_answer:
      print("Correct!")
      score += 1
else: 
      print("Incorrect")



answer2 = input("Define function that takes a name as anargument and prints a personalized greeting \n")
expected_answer2 = "def greet(name): print('Hello, {Juanye}!')"
if answer2.strip() ==expected_answer2:
     print('Correct!')
     score += 1
else:
     print('Incorrect')



def square(number):
     return number ** 2
answer3 = input("Define a function that returns the square of the number 2 (in one line): \n ")
expected3 = "def square(number): return number ** 2"
if answer3.strip().lower() == expected3.strip().lower():
     print('Correct')
     score += 1
else:
    print('Incoreect')

 
answer4 = input("Define a function that takes two numbers (4,4) and returns their sum (in one line): \n ")
expected4 = "def add(a+b): return 4+4"
if answer4.strip().lower() == expected4.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer5 = input("Define a function that returns the maximum of two numbers (29,11) (in one line): \n ")
expected5 = "def maximum(a,b): return a if 11 > 29 else b"
if answer5.strip().lower() == expected5.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer6 = input("Define a function that prints a ist of umbes from 1 to 10 (in one line): \n ")
expected6 = "def print_numbers(): for i in range(1,11) print(i):"
if answer6.strip().lower() == expected6.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')



def factorial(n):
     if n == 0:
          return 1
     return n*factorial(n-1)
answer7 = input("Define a function that calculates the factorial of a number (in one line): \n ")
expected7 = "def factorial(n): if n == 0  return 1  return n*factorial(n-1)  print(factorial(5))"
if answer7.strip().lower() == expected7.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')
     

answer = input('Define a function that checks if a number is even (in one line): \n ')
expected = "def is_even(): return n % 2 == 0 print(is_even(4))"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input("Define a function that returns the fibonacci sequence up to 'n' terms (in one line)")
expected = "def fibonacci(n): sequence = [] a, b = 0, 1 while len(sequence)< n:  sequence.append(a) a,b = b,a + b  return sequence    print(fibonacci(5))"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Define a function that takes a string and returns it in uppercase (in one line): ')
expected = "def to_uppercase(s): return s.upper()  print(to_uppercase('hello'))"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Print the numbers from 1 to 10 (in one line)')
expected = "for i in range(1,6):  print(i)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Print the even number from 2 to 20 (in one line)')
expected = "for i in range(2, 21, 2):  print(i)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Print the odd numbers from 1 to 19 (in one line)')
expected = "for i in range(1, 20, 2): print(i)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input("Print the numbers from 10 down to 1 (in one line)")
expected = "for i in range(10, 0, -1):  print(i)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')



answer = input("Print the numbers from 1 to 100, but only print the numbers that are divisible by 3 (in one line only)")
expected = "f i in range(1, 101): if i % 3 == 0:   print(i)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input("Print the squares of the numbers from 1 to 10 (in one line)")
expected = "fro i in range(1, 11):  print(i * i)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input("Print a multiplication table for the number 5 (from 5x1 to 510) (in one line)")
expected = "for i in range(1, 11):  print(f'5x{i} = {5*i}')"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input("Print the factorial of the number 5 (in one line)")
expected = "factorial = 1  for i in range(1,6):  factorial *=i   print(factorial)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input("Print the first 10 fibonacci numbers (in one line)")
expected = "a,b = 0,1  for i in range(10):   print(a)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input("Print a trianlge of stars with 8 rows (in one line)")
expected = "for i in range(1,9):  print('*' * i)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')




answer = input('Check if the number 8 is positive or negative (in one line )')
expected = "number = 8  if number > 0:  print('positive')   else:   print('negative') "
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Check if the number 8 is even or odd (in one line)')
expected = "number = 8  if number % 2 == 0  print('even')   else:   print('odd')"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Check if a 10 is equal to 10 (in one line)')
expected = "number = 10  if number == 10:  print('equal to 10')   else:   print('not equal to 10')"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Check if a person is old enough to drive (age 16 or older) with the age given being 11 (in one line)')
expected = "age = 11  if age >= 16:  print('can drive')   else:   print('cannot drive')"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')



answer = input("Check if a number (29) is greater than 100 (in one line)")
expected = "number = 29  if number > 100:  print('Greater than 100')   else:   print('Less than 100') "
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Check if a number (98) is less than 50 (in one line)')
expected = "number = 98  if number < 50:  print('Greater than 50')   else:   print('Less than 50')"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Determine if a string ("apple") contains the letter "a" (in one line)')
expected = "string = apple  if 'a' in string:  print('Contains 'a'')   else:   print('Does not contain 'a'')"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Check if a number(11) is between 10 and 20(inclusive) (in one line)')
expected = "number = 11  if 10 <= number <= 20:  print('Between 10 and 20')   else:   print('Outsidethe range')"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Check if a stringis empty (in one line)')
expected = "string = ""  if not string:  print('Empty string')   else:   print('Non-empty string')"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input("Check if a string ('hello') starts with a specific character in this case letter h (in one line)")
expected = "string = 'hello'  if string.stratswith('h')  print('Starts with 'h')   else:   print('Does not start with 'h')" 
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Create a list of integers from 1 to 5')
expected = "numbers = [1,2,3,4,5]"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Access the first element of the list above')
expected = "numbers = [1,2,3,4,5]  print(numbers[0])"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Access the last element of the list [1,2,3,4,5]')
expected = "number = [1,2,3,4,5]  print(numbers[-1])"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Change the second value in the list above to the number 10')
expected = "numbers = [1,2,3,4,5]  numbers[1] = 10  print(numbers)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')



answer = input('Add a element at the end of the original list (29)')
expected = "numbers = [1,2,3,4,5]  numbers.append(6) = 29   print(numbers)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Insert an element at the sixth position of the original list')
expected = "numbers = [1,2,3,4,5]  numbers.insert(5,6)   print(numners)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Remove the 4 from the list of 1 to 5')
expected = "numbers = [1,2,3,4,5]  number.remove(4)    print(numbers)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Remove a element by the index remove the index 2')
expected = "numbers = [1,2,3,4,5]  del numbers[2]   print(numbers)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Find the index of the third element in the list of 1 to 5')
expected = "numbers = [1,2,3,4,5]  index = numbers.index(3)   print(index)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Count how many times a element appears in a list with a list of 1 to 5 ')
expected = "numbers = [1,2,3,4,5]  count = numbers.count(2)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Add the numbers 3 and 5 (in one line)')
expected = "a=3 b=5  result = a+b print(result)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Subtract 12 from 4 (in one line)')
expected = "a = 12 b = 4  result = a - b  print(result)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Multiply 2 and 49 (in one line)')
expected = "a=2 b=49  result= 2*49   print(result)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Divide 20 by 4 (in one line)')
expected = "a=20 b=4  result = a/b   print(result)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')



answer = input('Find the remainder when divivding 17 by 5 (in one line)')
expected = "a=17 b=5  result= a%b   print(result)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Calculate 3 to the fourth power (in one line)')
expected = "base = 3  exponent = 4   results = base ** exponent"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Calculate the square root of the number 25 (in one line)')
expected = "import math  number = 25  result = math.sqrt(number)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Calculate the absolute value of the number 10 (in one line)')
expected = "number = 10  result= abs(number)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Round the number 8.8 to the nearest integer')
expected = "number = 8.8  result = round(number)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


answer = input('Floor the number 8.8 to the nearest integer')
expected = "import math  number = 8.8   result = math.floor(number)"
if answer.strip().lower() == expected.strip().lower():
     print('Correct')
     score += 1
else:
     print('Incorrect')


# If i want to add more areas to cove for learning add questions about the various packages/models


print("You Got " + str(score) + " questions correct!" )
print("You Got " + str((score/4) * 100) + " %." )