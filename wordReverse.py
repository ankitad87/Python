str1 = input("Enter a string:")
a = str1.split(" ")
for i in a:
    print(i[::-1], end=" ")
print('\n')

#Given a sentence, return a sentence with the words reversed
#master_yoda('I am home') --> 'home am I'
#master_yoda('We are ready') --> 'ready are We'

str1 = input("Enter the string: ")
# str2 = ""
arr1 = str1.split()
#method 2
# for i in arr1:
#     str2 = str2 + i[::-1] + " "
# print(str2[::-1])

#method 3
arr2 = arr1[::-1]
s2 = " "
print(s2.join(arr2))
