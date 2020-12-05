n = int(input("Enter the number of elements :\n"))
list1 = []
print("Enter the list elements :")
for i in range(0,n):
    ele = int(input())
    list1.append(ele)
print(list1)
dict1 = {}
for i in list1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
max_value = max(dict1.values())
k = [key for key, vals in dict1.items() if vals == max_value]
print("key, value : ", k, max_value)

