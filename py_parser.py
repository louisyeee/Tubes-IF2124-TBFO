import re
key = rules = [
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
]
def python_to_symbol(file, rules=None):
    f = open(file, "r")
    text =f.read()
    text = re.sub(' {2,}', ' ', text)
    text = text.rstrip("\n")
    text_lines = text.split('\n')
    hasil = []
    for line in text_lines:
        for word in line.lstrip().split(' '):

            for y in rules:
                if re.match(y[0], word):
                    hasil.append(y[1])
        hasil.append('NEWLINE')
    print(hasil)
    # hasil = []
    # for x in text:
    #     for y in rules:
    #         if re.match(y[0], x):
    #             hasil.append(y[1])
    # print(hasil)

python_to_symbol("test.py",rules)

