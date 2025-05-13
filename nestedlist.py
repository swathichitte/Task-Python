nested_list = [
    [5, 8, 3],
    [12, 1, 9],
    [7, 14, 2],
    [4, 4, 4]
]

for index, sublist in enumerate(nested_list, start=1):
    min_val = min(sublist)
    max_val = max(sublist)
    print(f"Sublist {index}: Min = {min_val}, Max = {max_val}")
