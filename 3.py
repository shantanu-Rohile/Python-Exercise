# Exercise 3 : String Indexing and Even Slicing

word = input("Type the word : ")

for index,value in enumerate(word):
    if(index % 2 ==0):
        print(word[index])
    