# Exercise 7 :  List Manipulation: Add and Remove

fruit = input("Enter a Fruit name : ")

fruit_list = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("Fruits in the list:")
for i in fruit_list:
    print(i)


fruit_list.remove(fruit_list[1])

fruit_list.append(fruit)


print("Updated Fruits in the list:")
print(fruit_list)