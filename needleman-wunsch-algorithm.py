#Needleman-Wunsch Algorithm

'''
Structure of dynamic programming algorithm:
1) Matrix creation of m*n, where m and n are the sizes of the S1 and S2 sequences respectively
2) To fill each row of the matrix, use the squares around it
3) Backtrack from the optimal solution (which is the last cell in the matrix)

'''

import numpy as np
import random

gap_penalty = -1
match_score = 1
mismatch_penalty = -1
extension_penalty = -0.5

num_x = random.randint(1, 50)
num_y = random.randint(1, 50)

x = np.random.choice(['A', 'T', 'G', 'C'], num_x)
y = np.random.choice(['A', 'T', 'G', 'C'], num_y)

s1, s2 = "", ""

for val in x:
    s1 += val
for val in y:
    s2 += val

print("\n")
print(s1)
print(s2)

#setting up the initial array
m, n = len(s1), len(s2)
arr = np.zeros((m+1, n+1))

#print(arr)

#we use a numpy array of 1 greater so that we can fit all values. Otherwise, the last or first value gets cut off.
for i in range(1, m+1):
    arr[i][0] = gap_penalty*i
for j in range(1, n+1):
    arr[0][j] = gap_penalty*j

#creating the rest of the array
old_gap_x = False
old_gap_y = False

for i in range(1, m+1):
    for j in range(1, n+1):
        match = arr[i-1][j-1] + (match_score if s1[i-1] == s2[j-1] else mismatch_penalty)
        xi_gap = arr[i-1][j] + (gap_penalty if old_gap_x else extension_penalty)
        yi_gap = arr[i][j-1] + (gap_penalty if old_gap_y else extension_penalty)

        arr[i][j] = max(match, xi_gap, yi_gap)

        if arr[i][j] == xi_gap:
            old_gap_x = True
        else:
            old_gap_x = False
        if arr[i][j] == yi_gap:
            old_gap_y = True
        else:
            old_gap_y = False

#print(arr)

#backtracking from the final solution (recursion)
i, j = m, n
ns1, ns2 = "", ""
final = []
def addNextValue(arr, i, j, ns1, ns2):
    current_score = arr[i][j]
    if current_score == arr[i-1][j-1] + (match_score if s1[i-1] == s2[j-1] else mismatch_penalty):
        ns1 += s1[i-1]
        ns2 += s2[j-1]
        '''print("Match!")
        print(f"Coordinate ({i}, {j}), Value: {current_score}")
        print(f'OG 1: {s1[::-1]}, OG 2: {s2[::-1]}')
        print(f'ST 1: {ns1}, ST 2: {ns2}, \n')'''
        final.append([ns1, ns2])
        addNextValue(arr, i-1, j-1, ns1, ns2)
    elif current_score == arr[i][j-1] + gap_penalty or current_score == (arr[i][j-1] + extension_penalty):
        ns1 += "-"
        ns2 += s2[j-1]
        '''print("Skip first string value!")
        print(f'OG 1: {s1[::-1]}, OG 2: {s2[::-1]}')
        print(f'ST 1: {ns1}, ST 2: {ns2}, \n')'''
        final.append([ns1, ns2])
        addNextValue(arr, i, j-1, ns1, ns2)
    elif current_score == arr[i-1][j] + gap_penalty or current_score == (arr[i-1][j] + extension_penalty):
        ns1 += s1[i-1]
        ns2 += "-"
        '''print("Skip second string value!")
        print(f'OG 1: {s1[::-1]}, OG 2: {s2[::-1]}')
        print(f'ST 1: {ns1}, ST 2: {ns2}, \n')'''
        final.append([ns1, ns2])
        addNextValue(arr, i-1, j, ns1, ns2)

addNextValue(arr, i, j, ns1, ns2)
print("\n")
for sequence in final[-1]:
    print(sequence[::-1])
print(f"Final similarity score: {arr[m][n]} \n")

#while loop (non-recursion backtracking)
'''
while i > 0 and j > 0:
    current_score = arr[i][j]
    print(f"Cell ({i}, {j}), Current score: {current_score}")
    if current_score == arr[i-1][j-1] + (match_score if s1[i-1] == s2[j-1] else mismatch_penalty):
        #you use the i-1 value of the string because thats what corresponds to the i value of the matrix (because the matrix is +1 on both axes)
        ns1 += s1[i-1]
        ns2 += s2[j-1]
        i -= 1
        j -= 1
        print("Match!")
        print(f'OG 1: {s1[::-1]}, OG 2: {s2[::-1]}')
        print(f'ST 1: {ns1}, ST 2: {ns2}, \n')
    elif current_score == arr[i][j-1] + gap_penalty:
        ns1 += "-"
        ns2 += s2[j-1]
        j -= 1
        print("Skip first string value!")
        print(f'OG 1: {s1[::-1]}, OG 2: {s2[::-1]}')
        print(f'ST 1: {ns1}, ST 2: {ns2}, \n')
    elif current_score == arr[i-1][j] + gap_penalty:
        ns1 += s1[i-1]
        ns2 += "-"
        i -= 1
        print("Skip second string value!")
        print(f'OG 1: {s1[::-1]}, OG 2: {s2[::-1]}')
        print(f'ST 1: {ns1}, ST 2: {ns2}, \n')
'''