from random import shuffle
print("This is a sample Python file.") 
mylist = [x for x in range(1,101) if x%2 == 0]
shuffle(mylist)

help(mylist.insert) # help function can be used to see the documentation about a function.
'''
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.
'''

# Methods and Functions.
# Three Cup Monte Game function:

mylist = ['O', "" , ""]
shuffle(mylist)
choice = input("Select an Option out of 1, 2 or 3 : ")
if choice not in ['1','2','3']:
    print("Invalid Choice !")
elif mylist[int(choice) - 1] == "O":
    print(f"You are a Winner !  {mylist}", end="\n\n")
else:
    print(f"You are a looser !  {mylist}", end="\n\n")

#*args and **kwargs in Python
def five_percent_of_sum(*args):
    print(sum(args) * 0.05)

five_percent_of_sum(1,3,4,34) #any numbers of functions can be passed here.


