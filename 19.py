# Exercise 19 : Multi-Tiered Income Tax Calculation

value = 20000

result=0

def income_tx(value) :
    if(value<=10000) :
        tax =0
        result = 0
    elif(value<=20000):
        tax=10
        result =(tax/100) * value
    else:
        tax=20
        result = (tax/100) * value
    
    return result


print(income_tx(45000))