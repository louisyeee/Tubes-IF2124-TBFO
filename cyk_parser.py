import numpy as np
from tabulate import tabulate

'''
Asumsi:
- Text dalam bentuk array
- CNF dalam bentuk dictionary
'''

def beautiful_print(matrix):
    headers = [f'col{i}' for i in range(len(matrix))]

    table = tabulate(matrix, headers, tablefmt="fancy_grid")

    print(table)

def is_product(CNF, parent,  input1, input2 = None):
    if (input2 == None):
        return CNF[parent] == input1 
    else:
        return CNF[parent] == (input1, input2)

def nearest_non_terminal(CNF, input1, input2 = None):
    if (input2 == None):
        product = input1
    else:
        product = "{} {}".format(input1, input2)
        
    for key, value in CNF.items():
            if (product in value):
                return key     
    return None

def fill_diagonal_matrix_with_nearest_non_terminal(CNF, matrix, text):
    for i in range(len(matrix)):
        if (matrix[i][i] == 'NULL'):
            matrix[i][i] = nearest_non_terminal(CNF, text[i])

def is_grammar_fulfilled_in_cyk_matrix(start_state, cyk_matrix):
    return cyk_matrix[0][len(cyk_matrix)-1] == start_state


def process_diagonal_matrix(CNF, matrix, diagonalKe):
    diagonal_length = len(matrix) - diagonalKe
    pointer = 0
    # baris -> i + diagonalKe
    while (pointer < diagonal_length):
        if (pointer+1 < len(matrix) and pointer+diagonalKe+1 < len(matrix)):
            replacement = nearest_non_terminal(CNF, matrix[pointer][pointer+diagonalKe], matrix[pointer+1][pointer+diagonalKe+1])
        if (replacement != None):
            matrix[pointer][pointer+diagonalKe+1] = replacement
            pointer += 2
        elif (pointer+1 < len(matrix) and pointer+diagonalKe+1 < len(matrix)):
            matrix[pointer][pointer+diagonalKe+1] = matrix[pointer][pointer+diagonalKe]
            pointer += 1
        elif (pointer+1 == len(matrix) or pointer+diagonalKe+1 == len(matrix)):
            matrix[pointer-1][pointer+diagonalKe] = matrix[pointer][pointer+diagonalKe]
            pointer += 1
        else:    
            pointer += 1

def cyk_parse(text,CNF):
    # PRODUKSI MATRIKS
    word_length = len(text)
    cyk_matrix = np.full((word_length, word_length), 'NULL')
    # ROW DIMULAI DARI 0 sampai len(text) - 1
    # COL DIMULAI DARI 1 sampai len(text)
    # CNF DALAM BENTUK DICTIONARY
    
    # ISI MATRIX INISIALISASI
    fill_diagonal_matrix_with_nearest_non_terminal(CNF, cyk_matrix, text)

    # ITERASI DIAGONAL SAMPAI ATAS
    for diagonalKe in range(word_length-1):
        process_diagonal_matrix(CNF, cyk_matrix, diagonalKe)
    beautiful_print(cyk_matrix)
    return is_grammar_fulfilled_in_cyk_matrix('S', cyk_matrix)

# TEST
CNF = {
    'S': ('NP VP'),
    'NP': ('Det N', 'N'),
    'VP': ('V NP'),
    'Det': ('the','a'),
    'N': ('cat'),
    'V': ('chased')
}

text = ['the', 'cat', 'chased', 'a', 'cat']

print(cyk_parse(text, CNF))

