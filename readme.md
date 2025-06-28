# Python Cheat Sheet

A comprehensive guide to Python fundamentals covering variables, control structures, data structures, functions, and more.

## 1. Variables
Store data in named containers for later use.

**Syntax:**
```python
variable_name = value
```

**Example:**
```python
foo = 2 
foo_bar = "hello world"
```

## 2. Print Statement
Display output to the console.

**Syntax:**
```python
print(value/variable)
```

**Example:**
```python
print("Foo Bar")
```

## 3. Selection Statements
Control program flow based on conditions.

### 3.1. IF Statement
Execute code block when condition is true.

**Syntax:**
```python
if(condition):
    # block of statements
```

**Example:**
```python
if(foo < 3):
    print("foo is less than 3")
```

### 3.2. IF-ELSE Statement
Execute different code blocks based on condition result.

**Syntax:**
```python
if(condition):
    # block of statements
else:
    # block of statements
```

**Example:**
```python
if(foo > 3):
    print("foo is greater than 3")
else:
    print("foo is less than 3")
```

### 3.3. ELIF Ladder
Test multiple conditions in sequence.

**Syntax:**
```python
if(condition):
    # block of statements
elif(condition):
    # block of statements
else:
    # block of statements
```

**Example:**
```python
if(foo == 1):
    print("foo equals 1")
elif(foo == 2):
    print("foo equals 2")
else:
    print("foo value is other than 1 and 2")
```

### 3.4. Nested IF
Place IF statements inside other IF statements for complex conditions.

**Syntax:**
```python
if(condition):
    # block of statements
    if(condition):
        # block of statements
    else:
        # block of statements
else:
    # block of statements
```

**Example:**
```python
if(foo > 0):
    if(foo > 30):
        print("foo is greater than 30")
    else:
        print("foo is not greater than 30")
else:
    print("foo is not greater than 0")
```

## 4. Iteration (Loops)
Repeat code blocks multiple times.

### 4.1. While Loop
Repeat code while condition remains true.

**Syntax:**
```python
while(condition):
    # block of statements
```

**Example:**
```python
foo = 2
while(foo <= 5):
    print(foo)
    foo = foo + 1
```

### 4.2. For Loop
Iterate over sequences or ranges.

**Syntax 1:**
```python
for <variable> in <sequence>:
    # block of statements
```

**Example 1:**
```python
for number in 1, 2, 3, 4, 5:
    print(number)
```

**Syntax 2:**
```python
for number in range(x, y): 
    # block of statements
```

**Example 2:**
```python
foo_bar = ('Apple', 'Banana', 'Mango')
for index in range(0, len(foo_bar)):
    print(foo_bar[index])
```

## 5. Break Statement
Exit from loops prematurely when condition is met.

**Syntax:**
```python
break
```

**Example:**
```python
for letter in "PYTHON":
    if(letter == "H"):
        break
    print(letter)
```

## 6. Continue Statement
Skip current iteration and continue with next iteration.

**Syntax:**
```python
continue
```

**Example:**
```python
for letter in "PYTHON":
    if(letter == "H"):
        continue
    print(letter)
```

## 7. Lists
Store multiple items in ordered, mutable collections.

**Syntax:**
```python
sample_list = []
```

**Example:**
```python
foo_bar = [1, 2, 3, 4]
```

### 7.1. Append
Add element to the end of list.

**Syntax:**
```python
sample_list.append(element)
```

**Example:**
```python
foo_bar = [1, 2, 3, 4]
foo_bar.append(5)
```

### 7.2. Insert
Add element at specific position in list.

**Syntax:**
```python
sample_list.insert(index_position, element)
```

**Example:**
```python
foo_bar = [1, 2, 3, 4]
foo_bar.insert(3, 6)
```

### 7.3. Pop
Remove and return element at specified index.

**Syntax:**
```python
sample_list.pop(index)
```

**Example:**
```python
foo_bar = [1, 2, 3, 4]
foo_bar.pop(3)
```

### 7.4. Remove
Remove first occurrence of specified element.

**Syntax:**
```python
sample_list.remove(element)
```

**Example:**
```python
foo_bar = [1, 2, 3, 4]
foo_bar.remove(4)
```

### 7.5. Sort
Arrange list elements in ascending order.

**Syntax:**
```python
sample_list.sort()
```

**Example:**
```python
foo_bar = [1, 2, 3, 4]
foo_bar.sort()
```

### 7.6. Reverse
Reverse the order of list elements.

**Syntax:**
```python
sample_list.reverse()
```

**Example:**
```python
foo_bar = [1, 2, 3, 4]
foo_bar.reverse()
```

### 7.7. Slice
Extract portion of list using start and end positions.

**Syntax:**
```python
sample_list[start_position:end_position]
```

**Example:**
```python
foo_bar = [1, 2, 3, 4]
foo_bar[1:3]
```

## 8. Tuples
Store multiple items in ordered, immutable collections.

**Syntax:**
```python
tuple_name = (value1, value2, …value_n)
```

**Example:**
```python
foo = ("Moto", "Apple", "Sony")
```

## 9. Dictionaries
Store data in key-value pairs for fast lookups.

**Syntax:**
```python
# Dictionary declaration
dict_name = {key1: value1, key2: value2, …key_n: value_n}

# Dictionary value updating
dict_name.update(dict_name1)

# Getting the value for a given key
dict_name.get(key1)
```

**Example:**
```python
foo = {"Name": "Maddy", "Age": 18}
print(foo.get("Name"))
foo_bar = {"Address": "India"}
foo.update(foo_bar)
```

## 10. Libraries
Built-in modules for common programming tasks.

### 10.1. String Methods
Manipulate and analyze text data.

**Syntax:**
```python
variable.count("count_of_string_to_find")
variable.replace("old_string", "new_string")
variable.find("string_to_find")
variable.startswith("string_to_match")
variable.endswith("string_to_match")
variable.isdigit()
variable.upper()
variable.lower()
variable.split("string_based_on_split")
variable[start_position:end_position]
```

**Example:**
```python
foo = "I love python"
foo.count("o")
foo.replace("l", "L")
foo.find("python")
foo.startswith("I")
foo.endswith("on")
foo.isdigit()
foo.upper()
foo.lower()
foo.split(" ")
foo[1:4]
```

### 10.2. Random Module
Generate random numbers and make random choices.

**Syntax:**
```python
import random
random.randrange(lower_limit, upper_limit)
```

**Example:**
```python
import random
random.randrange(10, 50)
```

### 10.3. Time Module
Work with time-related functions and data.

**Syntax:**
```python
import time
time.gmtime()
time.localtime()
time.timezone
```

**Example:**
```python
import time
print(time.gmtime())
print(time.localtime())
print(time.timezone)
```

### 10.4. Math Module
Perform mathematical operations and calculations.

**Syntax:**
```python
import math
math.ceil(decimal_value)
math.floor(decimal_value)
math.factorial(value)
math.fabs(decimal_value)
```

**Example:**
```python
import math
print(math.ceil(9.6))
print(math.floor(9.6))
print(math.factorial(5))
print(math.fabs(9.6))
```

## 11. Exception Handling
Handle errors gracefully without crashing the program.

### 11.1. Try-Except
Catch and handle exceptions that occur during execution.

**Syntax:**
```python
try:
    # block of statements
except:
    # If there is any exception, then execute this block
```

**Example:**
```python
try:
    foo = 100/0
except:
    print("Number cannot be divisible by 0")
```

### 11.2. Try-Except-Finally
Ensure certain code runs regardless of exceptions.

**Syntax:**
```python
try:
    # block of statements
except:
    # If there is any exception, then execute this block
finally:
    # This would always be executed
```

**Example:**
```python
try:
    foo = 100/0
except:
    print("Number cannot be divisible by 0")
finally:
    print("Program is terminating")
```

## 12. Functions
Create reusable blocks of code to avoid repetition.

**Syntax:**
```python
def function_name(parameters):  # Function declaration
    # function body 
    [return]      

function_name(values)  # Function call
```

**Example:**
```python
def sum(foo, foo_bar):
    print(foo + foo_bar)

sum(5, 5)
```

### 12.1. Positional Arguments
Pass arguments in specific order to function parameters.

**Syntax:**
```python
def function_name(parameter1, parameter2):                     
    # function body 
    [return]      

function_name(value1, value2)
```

**Example:**
```python
def sum(foo, foo_bar):
    print(foo + foo_bar)

sum(10, 10)
```

### 12.2. Keyword Arguments
Pass arguments by explicitly naming parameters.

**Syntax:**
```python
def function_name(parameter1, parameter2):                     
    # function body 
    [return]
      
function_name(parameter1=value1, parameter2=value2)
```

**Example:**
```python
def sum(foo, foo_bar):
    print(foo + foo_bar)

sum(foo_bar=10, foo=5)
# (or)
sum(foo=5, foo_bar=10)
```

### 12.3. Default Arguments
Provide default values for parameters when not specified.

**Syntax:**
```python
def function_name(parameter1, parameter2=value):                     
    # Function body
    [return]   
       
function_name(value1)
```

**Example:**
```python
def sum(foo, foo_bar=10):
    print(foo + foo_bar)

sum(2)
# (or)
sum(2, 4)
```

### 12.4. Variable Number of Arguments
Accept unlimited number of arguments using *args.

**Syntax:**
```python
def function_name(*variable_tuple):                     
    # Function body 
    [return]      

function_name(value1/value1, value2, …value_n)
```

**Example:**
```python
def sum(*foo):
    foo_bar = 0
    for i in foo:
        foo_bar += i
    print(foo_bar)

sum(2, 4, 6)
# (or)
sum(1, 2)
```

## 13. Variable Scope
Control where variables can be accessed in your program.

### 13.1. Global Variables
Variables accessible from anywhere in the program.

**Syntax:**
```python
variable1 = value  # Global variable, can be accessible anywhere.

def function_name():
    # function body
    [return]
```

**Example:**
```python
foo = 100

def function1():
    global foo
    foo += 1

print(foo)
function1()
print(foo)
```

### 13.2. Local Variables
Variables only accessible within the function where they're defined.

**Syntax:**
```python
def function_name():
    variable1 = value  # Local variable, can accessible only inside this function.
```

**Example:**
```python
def function1():
    foo = 100
    foo += 1
    print(foo)

function1()
# print(foo)  # This statement will give an error as variable foo is local
```

## 14. Packages
Import and use external modules or custom modules.

**Syntax:**
```python
from packagename import modulename
# (or)
import packagename.modulename
```

**Example:**
```python
from Flights import ManageFlights
# (or)
import Flights.ManageFlights
```

## 15. File Handling
Read from and write to files on the system.

### 15.1. Opening a File
Open file for reading, writing, or appending.

**Syntax:**
```python
file = open(file_name [, access_mode])
```

**Example:**
```python
sample_file = open("sample.txt", "r")
```

### 15.2. Closing a File
Close file to free up system resources.

**Syntax:**
```python
file.close()
```

**Example:**
```python
sample_file.close()
```

### 15.3. Writing into a File
Write text content to a file.

**Syntax:**
```python
file.write(string)
```

**Example:**
```python
sample_file.write("Welcome to files…")
```

### 15.4. Reading from a File
Read content from a file.

**Syntax:**
```python
file.read()
```

**Example:**
```python
sample_file.read()
```

## 16. Regular Expressions
Pattern matching and text manipulation using regex patterns.

**Examples:**
```python
import re

re.search(r"come", "Welcome")
# Output: come

re.search(r"c..e", "Welcome")
# Output: come

re.search(r"c\dme", "Welc0me")
# Output: c0me

re.search(r"W[0-9]e", "W2elcome")
# Output: W2e

re.search(r"Wel|Fel", "Welcome")
# Output: Wel

re.search(r"Welcome\s", "Welcome to Regular Expression")
# Output: Welcome  # Will check whether space is there after "Welcome"

re.search(r"e$", "Welcome")
# Output: e

re.search(r"^W", "Welcome")
# Output: W

re.sub(r"Felcome", r"Welcome", "Felcome to Regular Expression")
# Output: Welcome to Regular Expression
```

## 17. Lambda Expressions
Create small anonymous functions for simple operations.

**Syntax:**
```python
lambda_name = lambda variable1, variable2, …variable_n : lambda_operation
```

**Example:**
```python
sum = lambda foo, foo_bar: foo + foo_bar
print(sum(3, 3))
```

## 18. Iterators
Traverse through collections and sequences efficiently.

**Examples:**

```python
# Printing list data
list = [10, 2, 100, 5]

for i in range(0, len(list)):
    print(list[i])
    
print("--------------------")

# Alternative way to print list data
list = [10, 2, 100, 5]
for i in range(0, len(list)):
    print(list[i])
    
print("--------------------")

# Printing characters of string
name = "INFOSYS"
for char in name:
    print(char)

# Alternative way to print characters
name = "INFOSYS"
for char in "INFOSYS":
    print(char)   
    
dict = {"a": 100, "b": 500, "c": 300}

# Get all keys from the dictionary
list = dict.keys()
print(list)

dict = {"a": 100, "b": 500, "c": 300}

# Iterating through the dictionary
for key in dict:
    print(key)
    print(dict[key])

dict = {"a": 100, "b": 500, "c": 300}

# Iterating through the dictionary using .items()
for key, value in dict.items():
    print(key, value)
```

