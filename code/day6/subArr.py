# Take an array of positive and negative integers. 
#Find if their is a sub array with sum zero exists or not. If exists, then return that subarray.

import random
size = int(input("enter the size of array\n"))
a=[]
for i in range(0,size):
    a.append(random.randint(-10,10))
print(a,"\n")
count = 0
for i in range(1,size):
    for j in range(0,size-i+1):
        sum = 0
        for k in range(j,j+i):
            sum+=a[k]
        if(sum==0):
            print(a[j:j+i])
            count+=1
            
print("there are total ", count , " sub-arrays having sum zero\n")
