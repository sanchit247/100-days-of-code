#  We have an array [3, 0, 1, 0, 5, 9, 0, 6, 7]. We need push all the zeros to end [3, 1, 5, 9, 6, 7, 0, 0, 0].
#But we need to maintain the relative order of all the items inside array.

a=[3,0,1,0,5,9,0,6,7]
for i in range(len(a)):
    for j in range(i):
        if(a[j]==0):
           a[i],a[j] = a[j],a[i]
print("pushed array is :\n",a)

