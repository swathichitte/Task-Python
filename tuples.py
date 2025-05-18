# Task1 Take a list of dictionary{Name: ,age: ,citize: } check whether that person is eligible for vote or not and also check the citizen.if both conditions are True add { eligible: True}
people = [
    {"Name": "Ramya", "age": 40, "citizen": "Indian"},
    {"Name": "John", "age": 17, "citizen": "Indian"},
    {"Name": "Asha", "age": 25, "citizen": "Canadian"},
    {"Name": "Rahul", "age": 30, "citizen": "Indian"}
]

for person in people:
    if person["age"] >= 18 and person["citizen"] == "Indian":
        person["eligible"] = True
    else:
        person["eligible"] = False

for person in people:
    print(person)



#Task2: Take a tuple of elements, print the unique elements in the new list

data = (1, "hello", "world", True, False, 3.14, 2, 9.8, "hello", 3.14)

strings = []
integers = []
floats = []
booleans = []

for item in data:
    if isinstance(item, str) and item not in strings:
        strings.append(item)
    elif isinstance(item, bool) and item not in booleans:
        booleans.append(item)
    elif isinstance(item, int) and not isinstance(item, bool) and item not in integers:
        integers.append(item)
    elif isinstance(item, float) and item not in floats:
        floats.append(item)

print("Strings:", strings)
print("Integers:", integers)
print("Floats:", floats)
print("Booleans:", booleans)


