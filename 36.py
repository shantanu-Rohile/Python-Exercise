# Exercise 36. Capitalize First Letter (Title Case)

text="hello world from python"
text_split=text.split()
cap=[]
for word in text_split:
    cap.append(word.capitalize())
result=" ".join(cap)

print(result)