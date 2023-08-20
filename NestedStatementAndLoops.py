'''
LEGB Rule :
Below is the order how pythonc chekcs for a referenced variable.
L : Check first in local scope and if not marked as global
E : Check in enclosing funciton local scope
G : Check Global
B : Check in built ins.
'''

myfile = open("myfile.txt", mode="w+")
myfile.write("This is first file created by me in python.")
myfile.close()
myfile = open("myfile.txt", mode="r+")
print(myfile.read())