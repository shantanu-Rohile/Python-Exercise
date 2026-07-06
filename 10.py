# Exercise 10 : Finding Extremes (Min/Max) in a List

list = [1,2,3,4,5,6,7,8,9]


def min_max(list):
    min_value=(2**31)-1
    max_value=0
    for i in list:
        if(i>max_value ):
            max_value=i
            if(i<min_value):
                min_value=i
        
    print("Maximum Value in list : ",max_value)
    print("Minimum Value in list : ", min_value)

# min_max(list)

def easy_min_max(list):
    largest=max(list)
    smallest=min(list)
    print("Maximum Value in list : ",largest)
    print("Minimum Value in list : ", smallest)

easy_min_max(list)

