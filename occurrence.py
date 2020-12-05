list1 = [2,3,4,4,4,5,6,6,2,7]
num = int(input("Enter the number to find its occurance: "))
counter = 0
for i in list1:
    if i == num:
        counter += 1
print(counter)
