# Exercise 1 : Arithmetic Product and Conditional Logic

num1 = input ("Enter number : ")
num2 = input ("Enter Number : ")

num1 = int(num1)
num2 = int(num2)

if(num1 + num2 >1000):
    print("number is greater than 1000")
elif((num1+num2)<0):
    print("number is less than 0")
else:
    print("Arithmatic sum of number is : ",num1+num2)