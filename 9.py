# Exercise 9 : Vowel Frequency Counter

word = "Owl House is good but mine is better"

vowels=["a","e","i","o","u","A","E","I","O","U"]

count =0;

for i in word:
    if i in vowels:
        count +=1

print("The number of vowels in the word is : ",count)
