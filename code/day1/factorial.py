#Write a program to calculate factorial without recursion.
n=int(input("enter the number\n"))
fac=1
while(n!=1):
    fac = n*fac
    n-=1
print( "The factorial is : "fac)
