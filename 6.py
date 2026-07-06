# Exercise 6 : 
n=int (input("Type the number for factorial : "))
def factorial(n) :
    if(n==0):
        return 1
    else:
        factorial=1
        for value in range(n,1,-1):
            factorial=factorial*value
        return factorial

print("The factorial of the number is : ",factorial(n))