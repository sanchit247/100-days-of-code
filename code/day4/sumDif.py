"""
1. Create a program that randomly generated problems of (sum of two numbers and
difference of two numbers) randomly. User sees a problem and then answer. Then
prompt user with next problem. No need to terminate program by code, we shall
solve that part later.
"""
import random
while(1):
    x = random.randint(1,150)
    y = random.randint(1,150)
    print("enter the sum of ", x," + ",y,"\n")
    summ = int(input())
    print("enter the difference ", x," - ",y,"\n")
    dif =int(input())

