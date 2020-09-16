def increment(my_number):
    if sum(my_number)==(len(my_number)*9):
        my_number.insert(0,0)
    last = len(my_number) - 1
    my_number[last] += 1
    current_index = last
    current_item = my_number[current_index]
    while current_item == 10:
        current_item = 0
        my_number[current_index] = current_item
        my_number[current_index - 1] += 1
        current_index -= 1
        current_item = my_number[current_index]
    return my_number


print(increment([9,7]))