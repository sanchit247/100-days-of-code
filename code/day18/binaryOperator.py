# Day 18 problem for Python Developers.

1. Reverse the bits of a given integer by using binary operators.

This problem is a bit basic problem and need to dig a bit deeper. So, you guys are free to write program in
C or C++ as well.

Input :
-100 has binary representation as '11111111111111111111111110011100'
On reversing bits, it should be '00111001111111111111111111111111'

#solution

n= int(input("enter the number\n"))
a=[]
def binary(m):   # calculates  in reverse already
    b=[]
    while(m>=1):
        b.append(int(m%2))
        m = m/2
    return b
if(n==0):
    a.append(0)
elif(n>0):
    a=binary(n)
else:
    a = binary(2**32 + n)   # to represent it in 32 bits
print("Reverse of the bits ",a)


# another approach

rev = 0
if(n<0):
    rev = 2**32 + n
else:
    while(n>0):
        rev = rev << 1  # rev = rev*2
        if(n & 1 ==1): # n is odd
            rev = rev^1 # rev = rev XOR 1
        n=n>>1 # n = n/2
print("reverse of bits another approach " binary(rev))        
