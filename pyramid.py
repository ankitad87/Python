rows = int(input("Enter number of rows : "))
l = int(rows*2) - 2
for i in range(1, rows+1):
    print(l*" ", end="")
    print(i*"* ")
    l = l -1
