# Exercise 25 : Check Leap Year

num = 2024

if (num % 4==0 and (num%4==100 and num%400 !=0)) :
    print("Not leap year")
elif num%4==0 :
    print("Leap year")
else :
    print ("Not leap year")