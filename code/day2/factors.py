# Find all the factors of a given number, like 25 (1, 5, 25). 40(1, 2, 4, 5, 8, 10, 20, 40)
x = int(input("input the number"))

for i in range(1,x+1):
    if(x%i==0):
        print(i,'\t',end="")
