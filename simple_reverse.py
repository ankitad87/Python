str1 = input("Enter a string:")
length = len(str1)
rev =""
for i in str1:
  rev += str1[length -1]
  length = length -1
print('\n')
print(rev)
