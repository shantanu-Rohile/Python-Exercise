# Exercise 23 : Check Palindrome Number

num = int (input ("Give a number : "))
num_orignal=num
rev=0
while (num > 0) :
    digit = num % 10
    rev = rev *10 + digit
    num = (num//10)

print(rev)
print(num_orignal)

if(rev == num_orignal) :
    print("number is palindrone")
else :
    print("number is not palindrone")
