# Exercise 2 :  Cumulative Sum of a Range

array=[1,2,3,4,5,6,7,8,9,10]

for index,value in enumerate(array):
    if(index!=0):
        print("sum is : ", array[index]+array[index-1])
    else:
        print("sum is : ", array[index])
     