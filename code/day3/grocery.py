# Beginner level
"""
1. Write a program to find the LCM and HCF of 4 given numbers.
2. Write a program to store grocery list into a text file and to fetch grocery items from file.

Sample Grocery list
Flour => 10 KG
Rice => 10 KG
Sugar => 5 KG
Pulse 1 => 2 KG
Pulse 2 => 2 KG
Pulse 3 =>2 KG
....
....
// So, first ask user how many items and then ask for items and store them to
//file. Once user query file and type Pulse3, then it should return 2 KG.
"""

grocery = {}
no_of_items = int(input("enter the number of items to be inserted\n"))
for i in range(0,no_of_items):
        item = input("enter the item name\n")
        price = float(input("enter the item price per KG.\n"))
        grocery[item] = price
 # print(grocery)
def look(item):
        send = 0
        for key,value in grocery.items():
                if(key==item):
                        print("price of ", key ," is Rs.", value,"/kg \n")
                        send = 1
                        return send 
        return send
item = input("enter the name of item to be searched\n")
if(not (look(item))):
        print("item not found\n")
