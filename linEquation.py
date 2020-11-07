import numpy as np

num1 = input("First number: ")
num2 = input("Second number: ")
num3 = input("Third number: ")
num4 = input("Fourth number: ")
num5 = input("Fifth number: ")
num6 = input("Sixth number: ")
num7 = input("Seventh number: ")
num8 = input("Eighth number: ")
num9 = input("Ninth number: ")
print("Next, please enter the solutions to the systems.")
num10 = input("Tenth number: ")
num11 = input("Eleventh number: ")
num12 = input("Twelveth number: ")
x = ([int(num1), int(num2), int(num3)])
y = ([int(num4), int(num5), int(num6)])
z = ([int(num7), int(num8), int(num9)])
a = ([int(num10), int(num11), int(num12)])
A = np.array([x, y, z])
b = np.array(a)
g = np.linalg.solve(A, b)
print(x)
print(y)
print(z)
print(a)

#my best attempt at a python program that solves systems os linear equations for me, i want it to be interactable so that
#i dont have to edit the code everytime i want to use this program

#i have had little help from the internet, this is my attempt to use my own concepts

#it has a slew of bugs that i dont know how to fix because i dont understand them yet

#i am happy to be cataloging this so that i can look back on it in the years to come
