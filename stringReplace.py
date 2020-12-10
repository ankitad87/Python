
s1 = input("Enter the main string: ")
s2 = input("Enter occurance string: ")
s3 = input("Enter the replacement: ")

#method 1
print(s1.replace(s2, s3))
print(s1)

#method 2
a1 = s1.split()
a2 = s2.split()
a3 = s3.split()
print(a3)
i = 0
news = ""

for word in a1:
    if word == s2:
        word = s3
    i += 1
    news += str(word) + " "

print("New string is :")
print(news)
