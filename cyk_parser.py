import numpy as np


def nearest_non_terminal(CNF, input1, input2 = None):
    hasil = []
    if (input2 == None):
        for x in input1:
            for key, value in CNF.items():
                if (x in value):
                    hasil.append(key)
    else:
        for x in input1:
            for y in input2:
                product = "{} {}".format(x, y)
                for key, value in CNF.items():
                    # print(product, value)
                    if (product in value):
                        hasil.append(key)     # hasil = ['S', 'NP', 'VP', 'V', 'N', 'P']
    return hasil

def fill_diagonal_matrix_with_nearest_non_terminal(CNF, matrix, text):
    for i in range(len(matrix)):
        if (matrix[i][i] == 'NULL'):
            matrix[i][i] = nearest_non_terminal(CNF, [text[i]])

def is_grammar_fulfilled_in_cyk_matrix(start_state, cyk_matrix, CNF = None):
    left = find_rightmost_left_of_unused_symbol(cyk_matrix, 0, len(cyk_matrix)-1)
    down = find_topmost_down_of_unused_symbol(cyk_matrix, 0, len(cyk_matrix)-1)

    if (left != None and down != None):
        if start_state in nearest_non_terminal(CNF, left, down):
            return True
    return False



def process_diagonal_matix_from_right_to_left(CNF, matrix, diagonalKe):
    #handling diagonal pertama

    #handling diagonal rekurens
    diagonal_length = len(matrix) - diagonalKe
    pointer = diagonal_length - 1
    while (pointer > -1):
        if is_unused(matrix,pointer, pointer+diagonalKe):
            here = matrix[pointer][pointer+diagonalKe]
            left = find_rightmost_left_of_unused_symbol(matrix, pointer, pointer+diagonalKe)
            down = find_topmost_down_of_unused_symbol(matrix, pointer, pointer+diagonalKe)
            if (left != None and down != None):
                replacement = nearest_non_terminal(CNF, left, down)
                if replacement == []: #kalau gaada
                    matrix[pointer][pointer+diagonalKe] = 'NULL'
                else:
                    matrix[pointer][pointer+diagonalKe] = replacement
            pointer -= 1

def find_rightmost_left_of_unused_symbol(matrix, row, col):
    for i in range(col, -1, -1):
        if (matrix[row][i] != 'NULL'):
            if (is_unused(matrix, row, i)):
                return matrix[row][i]
    return None

def find_topmost_down_of_unused_symbol(matrix, row, col):
    for i in range(row, len(matrix)):
        if (matrix[i][col] != 'NULL'):
            if (is_unused(matrix, i, col)):
                return matrix[i][col]
    return None

def is_unused(matrix, row, col):
    if (col < len(matrix) - 1 and row > 0):
        return matrix[row-1][col] == 'NULL' and matrix[row][col+1] == 'NULL'
    elif (col < len(matrix) - 1):
        return matrix[row][col+1] == 'NULL'
    elif (row > 0):
        return matrix[row-1][col] == 'NULL'
    else:
        return True

def cyk_parser(text,CNF):
    # PRODUKSI MATRIKS
    word_length = len(text)
    cyk_matrix = np.full((word_length, word_length), 'NULL',dtype=object)
    # ROW DIMULAI DARI 0 sampai len(text) - 1
    # COL DIMULAI DARI 1 sampai len(text)
    # CNF DALAM BENTUK DICTIONARY
    
    # ISI MATRIX INISIALISASI
    fill_diagonal_matrix_with_nearest_non_terminal(CNF, cyk_matrix, text)

    # ITERASI DIAGONAL SAMPAI ATAS
    for diagonalKe in range(1, word_length-1):
        process_diagonal_matix_from_right_to_left(CNF, cyk_matrix, diagonalKe)
    
    return [is_grammar_fulfilled_in_cyk_matrix('START', cyk_matrix, CNF = CNF), cyk_matrix]



