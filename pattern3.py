#pattern N
rows = 5
for i in range(1, rows + 1):
    res = ""
    for j in range(1, rows + 1):
        if j == 1 or j == rows or i == j:
            res += "* "
        else:
            res += "  "
    print(res)

#pattern Z

rows = 5
for i in range(1, rows + 1):
    res = ""
    for j in range(1, rows + 1):
        if i == 1 or i == rows or i + j == rows + 1:
            res += "* "
        else:
            res += "  "
    print(res)

#pattern R
rows = 5
mid = rows // 2 + 1

for i in range(1, rows + 1):
    res = ""
    for j in range(1, rows + 1):
        if i <= mid:
            if i == 1 or i == mid or j == 1 or j == rows:
                res += "*"+" "
            else:
                res += " "+" "
        else:
            if j == 1 or i == j:
                res += "* "
            else:
                res += "  "
    print(res)