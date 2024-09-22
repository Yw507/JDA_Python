#print("This line will be printed.")

#import matplotlib.pyplot as plt

# a=[1,2,3,4]
# b=[-1,-2,-3,-4]

# plt.plot(a,b)
# plt.show()
a = "America"
print(a[-2])
print(a[2:4])
print(a[::2])
print(a[0:4:2])


#string
name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
print("My name is %s and I am %d years old." % (name, age))
x = 10
y = 20
print(f"The sum of x and y is {x+y}.")
#In the regular string regular_string variable, 
#the backslashes (\n) are interpreted as escape sequences.
raw_string = r"C:\new_folder\file.txt"
print("Raw String:", raw_string)

A=(1,2,3,4,5)
print(A[1:4])

A = [1]
A.append([2,3,4,5])
print(len(A))
print(A)