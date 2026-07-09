# Exercise 38. File Creation and Basic I/O


with open("note.txt","w") as file:
    file.write("The greek mythology. \n")
    file.write("Best mythology. \n")
    file.write("Best Heroes. \n")


print("Reading the File.")

with open("note.txt","r") as file:
    Content =file.read()

    print(Content)