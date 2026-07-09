# Exercise 31. Print Alternate Prime Numbers

counter = 0

n = 100 + 1

prime = [2]
devisibles=[]
for i in range (2, n):
    for j in (2,i):
        if(i%j==0) :
            devisibles.append(j)
    if(len(devisibles)==0):
        prime.append(i)

    divisble.clear()


print(prime)

