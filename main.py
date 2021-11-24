from cyk_parser import cyk_parser
# import argparse
from cnf_to_dict import cnf_file_to_dict
from lexer import *

rules = [
(r'\n', 'NEWLINE'),
('\\n', 'NEWLINE'),
(r'False', 'FALSE'),
(r'None', 'NONE'),
(r'True', 'TRUE'),
(r'and', 'AND'),
(r'as', 'AS'),
(r'break', 'BREAK'),
(r'class', 'CLASS'),
(r'continue', 'CONTINUE'),
(r'def', 'DEF'),
(r'elif', 'ELIF'),
(r'else', 'ELSE'),
(r'for', 'FOR'),
(r'from', 'FROM'),
(r'if', 'IF'),
(r'import', 'IMPORT'),
(r'in$', 'IN'),
(r'is$', 'IS'),
(r'not', 'NOT'),
(r'or', 'OR'),
(r'pass', 'PASS'),
(r'raise', 'RAISE'),
(r'return', 'RETURN'),
(r'while', 'WHILE'),
(r'with', 'WITH'),
(r'is$', 'COMPARE'),
(r'not', 'COMPARE'),
('\d+', 'NUMBER'),
('[a-zA-Z_]\w*', 'VARIABEL'),
# COMPARISON
(r'==|!=|>=|<=|>|<|in|not in|is|is not', 'COMPARISON'),
# ASSIGNMENT
('=', 'ASSIGNMENT'),
(r'\/\/=|\*\*=|\+=|\-=|\*=|\/=|\%=', 'ASSIGNMENT'),
# ARITMATIKA
(r'[+]|[-]|[*]|[/]|[%]|\/\/|\*\*', 'ARITMATIKA'),
# TANDA BACA
('[:]', 'COLON'),
('[.]', 'DOT'),
(',', 'COMMA'),
# KURUNG COMMENT
('[(]', 'KURUNG_BUKA'),
('[)]', 'KURUNG_TUTUP'),
('\[', 'KURUNG_SIKU_BUKA'),
('\]', 'KURUNG_SIKU_TUTUP'),
('[#]', 'COMMENT'),
('\'\'\'', 'COMMENT_MULTILINE'),
('\'', 'QUOTE'),
('"', 'DQUOTE')
]

lx = Lexer(rules, skip_whitespace=True)
filename = input('Masukkan nama file: ')

ipt = read_files_input(filename)
lx.input(ipt)

output = ''
try:
    for tok in lx.tokens():
        if tok == '':
            output = output
        else:
            output += "'" + str(tok) + "'" + ' '
        #print(tok)
except LexerError as err:
    # print('LexerError at position %s' % err.pos)
    pass

output = output.split("'NEWLINE'")
CNF = cnf_file_to_dict("grammars/cnf.txt")
# pprint(CNF)
i = 1
for x in output:
    x = x.strip().split(' ')
    print(x)
    hasil_cyk = cyk_parser(x, CNF)
    print(hasil_cyk[0])
    if (hasil_cyk[0] == False):
        print("Error in line {}".format(i))
    i += 1