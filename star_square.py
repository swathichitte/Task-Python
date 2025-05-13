rows = int(input("Enter no. of rouwas: "))
for r in range(1, rows + 1):
    res=""
    for c in range(1, rows + 1):
        if r==1 or r==rows or c==1 or c==rows or (r ==(rows//2+1) and c==(rows//2+1)):
            res+="*"+" "
        else:
            res += " "+" "
    print (res)