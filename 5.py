# Exercise 5 : Variable Swapping (The In-Place Method)

a  = int (input("Type the for a : "))
b = int (input("Type the for b : "))

print("The value of a before swap is : ",a)
print("The value of b before swap is : ",b)


print()
print()

def swap(a,b):
    c=b
    b=a
    a=c
    print("The value of a after swap is : ",a)
    print("The value of b after swap is : ",b)


swap(a,b)
