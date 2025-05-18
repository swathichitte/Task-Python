#program to separate odd & even elements from list
numbers = [10, 21, 4, 45, 66, 93, 11, 28]
even_numbers = []
odd_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)


#program to separate unique elements from list and add "*" at EOL
numbers = [4, 7, 4, 3, 9, 7, 1, 3, 2]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
for num in unique_numbers:
    print(f"{num}*")

