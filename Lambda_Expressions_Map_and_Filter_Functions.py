def square (num):
    return num**2
mylist = [1, 2, 3, 4, 5]
print("This is a square list : ", end="")
for item in map(square , mylist): #When map function is called, note that square not need to be called with (). Map automatically executes the Square function.
    print(item, end=" ")
print()

def check_even(num):
    return num %  2 == 0

even_list = list(filter(check_even , mylist)) #filter function filters the list based on the return value of function check_even.
print(f"This is a filtered list with even numbers - {even_list}", end="")
print()
# lambda expression :
square_func = lambda num : num ** 2
print(f"This is a lambda expression output : {square_func(5)}", end="")
print()

print(f"This is a lambda expression output using map: {list(map(lambda num : num ** 2, mylist))}", end="")
print()
print(f"This is a lambda expression output using filter: {list(filter(lambda num : num % 2 == 0, mylist))}", end="")
print()

names = ["Vivek" , "Gaurav" , "Mohan" , "Girish" , "Ankit", "Aravind"]
print("List having the first letter from each name: {}".format(list(map(lambda value : value[0], names))))
print("List having the reveresed names: {}".format(list(map(lambda value : value[::-1], names))))
print()