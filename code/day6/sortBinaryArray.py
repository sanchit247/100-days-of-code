# We have a binary array [1, 0, 1, 1, 1, 0, 0, 1, 0],
#we need to sort it as [0, 0, 0, 0, 1, 1, 1, 1, 1]. But we need to sort it in O(n) time.


size = 10
a=[]
for i in range(size):
    a.append(random.randint(0,1))
for i in range(len(a)):
    for j in range(i):
        if(a[i]<a[j]):
            a[i],a[j] = a[j],a[i]
print("sorted array\n",a)
