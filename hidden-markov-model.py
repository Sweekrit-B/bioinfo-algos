import numpy as np
import random
import pandas as pd
import math

trans_prob_matrix = [[0.8, 0.2], [0.4, 0.6]]
# [n to n, n to c] [c to n, c to c]
emis_prob_matrix = [[0.2, 0.3, 0.3, 0.2], [0.4, 0.2, 0.2, 0.2]]
# [ n for A, C, G, T] [c for A, C, G, T]
nucleotide_matrix = ['A', 'C', 'G', 'T']

#Logarithmic transformation function
def log_transform(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = math.log(matrix[i][j])
    return matrix

new_trans_prob_matrix = log_transform(trans_prob_matrix)
new_emis_prob_matrix = log_transform(emis_prob_matrix)

#num_x = random.randint(20, 50)
x = np.random.choice(['A', 'T', 'G', 'C'], 4)
s1 = 'CGAAAAAAATCG'
for val in x: s1 += val

print(s1)

#setting up the initial array
m = len(s1)
arr = np.zeros((2, m+1))
arr2_n = []
arr2_c = []

arr [0][0] = new_trans_prob_matrix[0][0]
arr [1][0] = new_trans_prob_matrix[0][1]

#determine whether its A, T, G, or C emission probability
def determine_nucleotide(nuc, code):
    nuc_code = nucleotide_matrix.index(nuc)
    if code == 'n': return new_emis_prob_matrix[0][nuc_code]
    if code == 'c': return new_emis_prob_matrix[1][nuc_code]

#first transformation
arr [0][1] = arr[0][0] + determine_nucleotide(s1[0], 'n')
arr [1][1] = arr[0][1] + determine_nucleotide(s1[0], 'c')

#all other transformations
for i in range(2, len(s1)+1):
    arr [0][i] = max(
        arr[0][i-1] + determine_nucleotide(s1[i-1], 'n') + new_trans_prob_matrix[0][0],
        arr[1][i-1] + determine_nucleotide(s1[i-1], 'n') + new_trans_prob_matrix[1][0])
    
    arr2_n.append([float(arr[0][i-1] + determine_nucleotide(s1[i-1], 'n') + new_trans_prob_matrix[0][0]), float(arr[1][i-1] + determine_nucleotide(s1[i-1], 'n') + new_trans_prob_matrix[1][0])])
    
    arr [1][i] = max(
        arr[0][i-1] + determine_nucleotide(s1[i-1], 'c') + new_trans_prob_matrix[0][1],
        arr[1][i-1] + determine_nucleotide(s1[i-1], 'c') + new_trans_prob_matrix[1][1])
    
    arr2_c.append([float(arr[0][i-1] + determine_nucleotide(s1[i-1], 'c') + new_trans_prob_matrix[0][1]), float(arr[1][i-1] + determine_nucleotide(s1[i-1], 'c') + new_trans_prob_matrix[1][1])])

print(arr)

#dynamic programming + recursive backtracking
def backtrack(arr, i):
    nc_seq = ''
    probability_output = arr[0][i] if arr[0][i] >= arr[1][i] else  arr[1][i]
    current_state = 'N' if arr[0][i] >= arr[1][i] else 'C' 
    nc_seq += current_state

    while i > 1:
        if current_state == 'N':
            from_N_to_N = arr[0][i-1] + determine_nucleotide(s1[i-1], 'n') + new_trans_prob_matrix[0][0]
            from_C_to_N = arr[1][i-1] + determine_nucleotide(s1[i-1], 'n') + new_trans_prob_matrix[1][0]
            
            if arr[0][i] == from_N_to_N:
                nc_seq += 'N'
                current_score = arr[0][i-1]
                current_state = 'N'
                i -= 1
            elif arr[0][i] == from_C_to_N:
                nc_seq += 'C'
                current_score = arr[1][i-1]
                current_state = 'C'
                i -= 1
        
        if current_state == 'C':
            from_N_to_C =  arr[0][i-1] + determine_nucleotide(s1[i-1], 'c') + new_trans_prob_matrix[0][1]
            from_C_to_C = arr[1][i-1] + determine_nucleotide(s1[i-1], 'c') + new_trans_prob_matrix[1][1]
            
            if arr[1][i] == from_N_to_C:
                nc_seq += 'N'
                current_score = arr[0][i-1]
                i -= 1
            if arr[1][i] == from_C_to_C:
                nc_seq += 'C'
                current_score = arr[1][i-1]
                i -= 1

    return [nc_seq[::-1], probability_output]

print(s1)
for output in backtrack(arr, len(s1)):
    print(output)