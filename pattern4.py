#diamond
rows = 5
for i in range(1, 2 * rows):
    res = ""
    spaces = rows - i if i <= rows else i - rows
    cols = i if i <= rows else 2 * rows - i

    for sp in range(spaces):
        res += "  "
    for j in range(cols):
        res += "* "

    print(res)

#hour glass pattern

rows = 5

for i in range(1, 2 * rows):
    res = ""
    spaces = i-1 if i <= rows else 2*rows-i-1
    cols = rows-i+1 if i <= rows else i- rows +1

    for sp in range(spaces):
        res += " "
    for j in range(cols):
        res += "* "

    print(res)