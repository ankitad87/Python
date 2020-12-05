str1 = input("Enter a string:")
a = str1.split(" ")
for i in a:
    print(i[::-1], end=" ")
print('\n')
