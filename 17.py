# Exercise 17 : Merging Lists with Parity Filtering

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3=[]
list4=[]
def combining_lists(list1, list2) :
    list3 =list(set(list1 + list2))
    list3.sort()
    for i in list3:
        if( i%2 !=0) :
            list4.append(i)
    
    return list4

    


print(combining_lists(list1, list2))