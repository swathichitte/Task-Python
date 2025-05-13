# find the missing number in the list

def find_missing_number(nums):
    n = len(nums) + 1  
    total = n * (n + 1) // 2  
    return total - sum(nums)

numbers = [1, 2, 4, 5, 6]
missing = find_missing_number(numbers)
print("Missing number is:", missing)


# Take a dictionary with salaries and Find percentage of the salaries

salaries = {
    "Alice": 50000,
    "Bob": 60000,
    "Charlie": 90000,
    "David": 40000
}

 
total_salary = sum(salaries.values())

 
salary_percentages = {}
for name, salary in salaries.items():
    percentage = (salary / total_salary) * 100
    salary_percentages[name] = round(percentage, 2)

 
for name, percent in salary_percentages.items():
    print(f"{name}: {percent}%")
