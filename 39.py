# Exercise 39. External File Word Counter

try:
    with open("note.txt","r") as file:
        Content=file.read()
        words=Content.split()
        count=len(words)
        print(count)
except FileNotFoundError:
    print("File Not Found")