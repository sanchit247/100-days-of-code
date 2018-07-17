#Write a program of simple calculator with sum, mul, sub, and div functions
def sum(x,y):
    return x+y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

def sub(x,y):
    return x-y
x = int(input("enter first value \n"))
y = int(input("enter second value \n"))
print("the sum is ",sum(x,y))
print("the mul is ",mul(x,y))
print("the div is ",div(x,y))
print("the sub is ",sub(x,y))
