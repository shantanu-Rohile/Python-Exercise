# Exercise 14 : Substring Frequency Analysis

str_x = "Emma is good developer. Emma is a writer"
word = "Emma"


def count(str_x,word):
    word2=""
    count=0
    for i in str_x :
        if(i==" " or i=="."):
            if(word2==word):
                count +=1
            
            word2=""
        else:
            word2 += i


def count_2(str_x,word):
    n=str_x.count(word)
    print(n)

count_2(str_x,word)



