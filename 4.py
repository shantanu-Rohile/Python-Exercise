# Exercise 4 : String Slicing and Substring Removal

word = input("Type the word : ")
remove_num=input("The place of letter upto which you want to remove letter :")
remove_num = int(remove_num)

def remove_letters(word, remove_num):
    word2=""
    for i in range(remove_num,len(word)):
        word2 += word[i]
    print("the new Word is : ", word2)



# Easier Solution

def remove_Letters(word,remove_num):
    new_word=word[remove_num:]
    print("the new Word is : ", new_word)

# remove_letters(word,remove_num)


# Letter before

def letter_before(word,remove_num):
    new_word=word[:remove_num]
    print("the new Word is : ", new_word)

letter_before(word,remove_num)
