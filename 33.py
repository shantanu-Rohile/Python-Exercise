# Exercise 33. Character Replacer (Data Sanitization)

text = "I love coding in Python"
word=""
for i in text:
    if i==" ":
        word += "_"
    else:
        word +=i

print(word)