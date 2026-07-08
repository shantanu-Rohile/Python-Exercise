# Exercise 12. List Comparison and Boolean Logic

list_numbers = [10, 20, 30, 40, 110]

def comparison(list_numbers):
    if list_numbers[0]==list_numbers[-1] :
        return False
    else :
        return True

print(comparison(list_numbers))