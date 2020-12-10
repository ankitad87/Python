s1 = input("Enter file string: ")
fp1 = open("new1.txt", "w")
fp1.write(s1)
fp1.close()
print("file saved. ")
fp2 = open("new1.txt", "r")
d = {'a':0, 'o':0}
for line in fp2:
    a1 = list(line)
    for i in a1:
        if i == 'a':
            d['a'] +=1
        if i == 'o':
            d['o'] +=1

print(d)
