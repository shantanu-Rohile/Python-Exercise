# Exercise 35. Digit Detection in Strings

text = "Python3"
contain_digit=False
for i in text :
    if i.isdigit():
        contain_digit=True

print(contain_digit)