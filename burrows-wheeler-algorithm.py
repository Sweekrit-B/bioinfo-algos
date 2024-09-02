import numpy as np
import random as random

num_x = random.randint(1, 50)
num_start = random.randint(1, num_x//2)
num_end = random.randint(num_start+1, num_x)

x_str_2 = ""
x_random = np.random.choice(['A', 'T', 'G', 'C'], num_x).tolist()
for i in x_random:
    x_str_2 += i

x_str_2 += "$"
x_2 = list(x_str_2)

"""['C', 'G', 'A', 'C', 'C', 'C', 'C', 'A', 'G', 'C', 'C', 'G', 'G', 'T', '$']"""

"""y_str_2 = "ACCCCAG" """
y_str_2 = ""
y_2 = list(y_str_2)

y_random = x_random[num_start:num_end]
for i in y_random:
    y_str_2 += i

y_2 = list(y_str_2)

"""
x_str = "ACTACGG"
x_str += "$"
x = list(x_str)

y_str = "TACG"
y = list(y_str)
"""

current_list = x_2
arr = []

'''
T A C G
G T A C
C G T A
A C G T

'''

def cycle(current_list):
    for i in range(len(current_list)):
        end_nuc = current_list.pop()
        current_list.insert(0, end_nuc)
        arr.append(current_list.copy())

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    sorted_left = mergeSort(left_half)
    sorted_right = mergeSort(right_half)

    return merge(sorted_left, sorted_right)

def merge(left, right):
    final_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final_arr.append(left[i])
            i += 1
        else:
            final_arr.append(right[j])
            j += 1
    
    final_arr.extend(left[i:])
    final_arr.extend(right[j:])

    return(final_arr)

def first_column(arr):
    firsts_list = []
    for item in arr:
        firsts_list.append(item[0])
    return firsts_list

def last_column(arr):
    lasts_list = []
    for item in arr:
        lasts_list.append(item[-1])
    return lasts_list

def determine_order_arr(arr, first, last):
    true_line = arr[0]
    print("The true line is as follows: ")
    print(true_line)

    used_indices = []

    a_list_first = []
    t_list_first = []
    c_list_first = []
    g_list_first = []

    for i in range(0, len(first)):
        if first[i] == 'A':
            a_list_first.append(i)
        elif first[i] == 'T':
            t_list_first.append(i)
        elif first[i] == 'G':
            g_list_first.append(i)
        elif first[i] == 'C':
            c_list_first.append(i)
    
    a_list_last = []
    t_list_last = []
    c_list_last = []
    g_list_last = []

    for i in range(0, len(last)):
        if last[i] == 'A':
            a_list_last.append(i)
        elif last[i] == 'T':
            t_list_last.append(i)
        elif last[i] == 'G':
            g_list_last.append(i)
        elif last[i] == 'C':
            c_list_last.append(i)

    print(a_list_first)
    print(a_list_last)
    print(t_list_first)
    print(t_list_last)
    print(c_list_first)
    print(c_list_last)
    print(g_list_first)
    print(g_list_last)

    start_letter = arr[0][-1]
    print("The starting nucleotide is: " + start_letter)
    print("Our first line is:")
    print(first)
    print("Our last line is:")
    print(last)

    current_letter = start_letter
    current_index = last.index(current_letter)

    order_list = np.empty(len(true_line)).tolist()
    for index in range(len(order_list)):
        order_list[index] = 0

    i = 1
    while i < len(true_line):
        print("Our i value is: " + str(i))
        if current_letter == "A":
            secondary_index = a_list_last.index(current_index)
            order_list[current_index] = i
            current_index = a_list_first[secondary_index]
            current_letter = last[current_index]
            i += 1
        elif current_letter == "T":
            secondary_index = t_list_last.index(current_index)
            order_list[current_index] = i
            current_index = t_list_first[secondary_index]
            current_letter = last[current_index]
            i += 1
        elif current_letter == "C":
            secondary_index = c_list_last.index(current_index)
            order_list[current_index] = i
            current_index = c_list_first[secondary_index]
            current_letter = last[current_index]
            i += 1
        elif current_letter == "G":
            secondary_index = g_list_last.index(current_index)
            order_list[current_index] = i
            current_index = g_list_first[secondary_index]
            current_letter = last[current_index]
            i += 1
        else:
            order_list[current_index] = i
            break
    
    for i in range(0, len(order_list)):
        if order_list[i] == 0:
            order_list[i] = len(last)

    return order_list    

"""def determine_order(arr, first, last):
    true_line = arr[0]
    print("The true line is as follows: ")
    print(true_line)

    start_letter = arr[0][-1]
    print("The starting nucleotide is: " + start_letter)
    print("Our first line is:")
    print(first)
    print("Our last line is:")
    print(last)

    current_letter = start_letter
    order_list = np.empty(len(true_line)).tolist()
    for index in range(len(order_list)):
        order_list[index] = 0

    i = 1
    while i  < len(true_line):
        print("Our i value is " + str(i))

        current_index = last.index(current_letter)
        print("The first seen index for " + current_letter + " is " + str(current_index))
        print('\n')
        order_list[current_index] = i
        print("Therefore, in index " + str(current_index) + " of order_list, the i value is " + str(i))
        print("This is what order list looks like now: ")
        print(order_list)
        print('\n')
        last[current_index] = ""
        print("Now, we will replace the current_index in last with a blank.")
        print("This is what last looks like now: ")
        print(last)
        print('\n')
        
        current_index = first.index(current_letter)
        print("Now, we set the current index to be the first index of the nucleotide " + current_letter + " in first, which is " + str(current_index))
        current_letter = last[current_index]
        print("This means that the current letter we are dealing with is " + current_letter)
        first[current_index] = ""
        print("Now, we will replace the current_index in first with a blank.")
        print("This is what we see now: ")
        print(first)
        print(last)
        print(order_list)
        print('\n')

        i += 1
    
    return order_list"""

def find_read(read, last, order):
    og_read = read
    read = read[::-1] + "$"
    current_nuc = read[0]
    
    print(last)
    print(order)
    print(read)

    possible_starts = []

    for i in range(len(last)):
        if current_nuc == last[i]:
            possible_starts.append(i)

    print(possible_starts)
    stored_start = 0
    j = 0

    for i in possible_starts:
        print("Starting with possible_starts value:   " + str(i))
        current_point_in_last = i
        current_value_in_order = order[current_point_in_last]
        stored_start = current_value_in_order
        print("Our stored start for this iteration is:   " + str(stored_start))

        while j <= len(last):
            if last[current_point_in_last] == current_nuc:

                print("\n" + str(last[current_point_in_last]) + " at index " + str(current_point_in_last) + " is equal to " + str(read[j]) + " at index " + str(j) + " of the read")
                print("Current value in order is:   " + str(current_value_in_order))
                
                j += 1
                current_nuc = read[j]
                current_value_in_order += 1
                current_point_in_last = order.index(current_value_in_order)

                print("\nFor the next step, the value of j is:   " + str(j))
                print("The next step has a current_nuc of:   " + current_nuc)
                print("The next value in order that we are dealing with is:   " + str(current_value_in_order))
                print("This means that in the list last, we are dealing with index:   " + str(current_point_in_last) + "  with value  " + last[current_point_in_last])
                print("Our stored start value is: " + str(stored_start))

                if j == len(og_read):
                    start_point = len(last) - stored_start - len(og_read)
                    end_point = len(last) - stored_start - 1
                    return [start_point, end_point]

            else:
                print("\n" + str(last[current_point_in_last]) + " at index " + str(current_point_in_last) + " is NOT equal to " + str(read[j]) + " at index " + str(j) + " of the read")
                current_nuc = read[0]
                j = 0
                break
        
    return "There is no match!"  


    """for i in possible_starts:
        print("Starting, with possible_starts value being " + str(i))
        current_point_in_last = i
        current_value_in_order = order[i]
        stored_start = order[i]

        while j <= len(last):
            if last[current_point_in_last] == current_nuc:
                print(str(last[current_point_in_last]) + " at index " + str(current_point_in_last) + " is equal to " + str(read[j]) + " at index " + str(j) + " of the read")
                j += 1
                current_nuc = read[j]
                current_value_in_order += 1
                print("Current value in order is " + str(current_value_in_order))
                current_point_in_last = order.index(current_value_in_order)
                print("Current value of j is " + str(j))
                if j == len(og_read):
                    return stored_start
            else:
                print(str(last[current_point_in_last]) + " at index " + str(current_point_in_last) + " is NOT equal to " + str(read[j]) + " at index " + str(j) + " of the read")
                current_nuc = read[0]
                j = 0
                break
        
    return "There is no match!" """  

print(x_2)
print(y_2)
print("\n")

cycle(current_list)
sort_arr = mergeSort(arr)
for item in sort_arr:
    print(item)

print("\n")

first = first_column(sort_arr)
last = last_column(sort_arr)
order = determine_order_arr(sort_arr, first_column(sort_arr), last_column(sort_arr))
print("\n\n")
print(x_2)
print(find_read(y_str_2, last, order))