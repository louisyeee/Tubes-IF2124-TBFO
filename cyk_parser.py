import numpy as np


'''
Asumsi:
- Text dalam bentuk array
- CNF dalam bentuk dictionary
'''



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
            if (value == product):
                return key     
    return None

def fill_diagonal_matrix_with_nearest_non_terminal(CNF, matrix, text):
    for i in len(matrix):
        if (matrix[i][i] == 0):
            matrix[i][i] = nearest_non_terminal(CNF, text[i])

def is_grammar_fulfilled_in_cyk_matrix(start_state, cyk_matrix):
    return cyk_matrix[0][len(cyk_matrix)-1] == start_state


def process_diagonal_matrix(CNF, matrix, diagonalKe):
    diagonal_length = len(matrix) - diagonalKe
    pointer = 0
    # baris -> i + diagonalKe
    while (pointer < diagonal_length):
        replacement = nearest_non_terminal(CNF, matrix[pointer][pointer+diagonalKe], matrix[pointer+1][pointer+diagonalKe+1])
        if (replacement != None):
            matrix[pointer][pointer+diagonalKe+1] = replacement
            pointer += 2
        else:
            pointer += 1
def cyk_parse(text,CNF):
    # PRODUKSI MATRIKS
    word_length = len(text)
    cyk_matrix = np.zeros(word_length, word_length)
    # ROW DIMULAI DARI 0 sampai len(text) - 1
    # COL DIMULAI DARI 1 sampai len(text)
    # CNF DALAM BENTUK DICTIONARY
    
    # ISI MATRIX INISIALISASI
    fill_diagonal_matrix_with_nearest_non_terminal(CNF, cyk_matrix, text)

    # ITERASI DIAGONAL SAMPAI ATAS
    for diagonalKe in range(word_length-1):
        process_diagonal_matrix(CNF, cyk_matrix, diagonalKe)

    return is_grammar_fulfilled_in_cyk_matrix('START', cyk_matrix)        

