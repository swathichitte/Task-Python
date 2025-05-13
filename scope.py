# scope:
#     Scope refers to the region of a program where a variable is recognized and can be accessed or modified.

# Types of Scopes with Examples

# 1. Local Scope
# Defined inside a function and only accessible within that function.
 
# def my_func():
#     x = 10
#     print(x)  

# my_func()
 
# 2. Enclosing Scope
# Scope of a non-local variable in nested functions.
 
# def outer():
#     x = "enclosed"
#     def inner():
#         print(x)   
#     inner()

# outer()

# 3. Global Scope
# Declared outside all functions. Accessible everywhere.

# x = "global"

# def display():
#     print(x)

# display()
# To modify global variables inside a function, use global keyword:

# x = 5

# def modify():
#     global x
#     x = 10

# modify()
# print(x)  # 10

# 4. Built-in Scope
# Functions like max(), sum(), len() etc. are in built-in scope.


# print(len("Hello"))  # 5
