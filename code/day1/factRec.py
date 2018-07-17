#Write a recursive program to calculate factorial of a given number.

n= int(input("enter the number\n"))
def facto(n):
    if(n==1):return 1
    else: return n*facto(n-1)
print( "The factorial is : " ,facto(n))
