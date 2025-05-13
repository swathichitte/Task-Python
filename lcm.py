import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_of_three(x, y, z):
    return lcm(lcm(x, y), z)

num1 = 12
num2 = 15
num3 = 20

result = lcm_of_three(num1, num2, num3)
print(f"The LCM of {num1}, {num2}, and {num3} is {result}")
