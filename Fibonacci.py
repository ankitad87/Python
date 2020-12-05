#Fibonacci series Program

num = int(input('Enter the number of elements in fibonacci series'))
ele = 0
arr = [0, 1]
for i in range(0,num):
    next = i +1
    ele = arr[i] + arr[next]
    arr.append(ele)
print('Series:')
print(arr)
