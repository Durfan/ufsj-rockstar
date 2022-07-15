from poetic.ply import yacc
from poetic.analysis.lexer import tokens


results = []


def p_statement(p):
    '''statement : assignment
                 | CONTINUE
                 | function
                 | LOOP conditional COMMA
                 | SEND expression
                 | IF conditional
                 | IF identifier CALL args
                 | SAY expression'''

    if (p[1] == 'Give back'):
        p[0] = f'jr {p[2]}'
    elif (p[1] == 'Say'):
        p[0] = (f'li $v0, 4', f'la $a0, {p[2]}', 'syscall')
    elif (p[1] == 'Shout'):
        p[0] = (f'li $v0, 4', f'la $a0, {p[2]}', 'syscall')
    elif (p[1] == 'While'):
        p[0] = (f'Loop:', f'{p[2]}')
    elif (len(p) == 2):
        p[0] = p[1]
    elif (len(p) == 3):
        p[0] = (p[1], p[2])
    elif (len(p) > 3):
        p[0] = (p[1], p[2])

    global results
    results.append(f'{p[0]}')


def p_assignment(p):
    '''assignment : identifier ATTR expression
                  | BUILD identifier UP
                  | KNOCK identifier DOWN
                  | PUT expression IN identifier'''

    if (p[1] == 'Put'):
        p[0] = (f'{p[2]}', f'sw {p[4]}')
    elif (p[1] == 'Build'):
        p[0] = f'add {p[2]}, {p[2]}, 1'
    elif (p[1] == 'Knock'):
        p[0] = f'sub {p[2]}, {p[2]}, 1'
    elif (p[2] == 'is' or 'are' or 'was' or 'where'):
        p[0] = f'add {p[1]}, {p[3]}'
        


def p_function(p):
    '''function : identifier FOO args'''

    p[0] = (f'{p[1]}:', f'{p[3]}')


def p_args(p):
    '''args : identifier LOGICAL args
            | identifier'''

    if (len(p) == 4):
        p[0] = (f'lw {p[1]}', f'{p[3]}')
    else:
        p[0] = f'lw {p[1]}'


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIV expression'''

    if (p[2] == 'plus'):
        p[0] = f'add {p[1]}, {p[1]}, {p[3]}'
    elif (p[2] == 'with'):
        p[0] = f'add {p[1]}, {p[1]}, {p[3]}'
    elif (p[2] == 'without'):
        p[0] = f'sub {p[1]}, {p[1]}, {p[3]}'
    elif (p[2] == 'minus'):
        p[0] = f'sub {p[1]}, {p[1]}, {p[3]}'
    elif (p[2] == 'of'):
        p[0] = f'mult {p[1]}, {p[3]}'
    elif (p[2] == 'times'):
        p[0] = f'mult {p[1]}, {p[3]}'
    elif (p[2] == 'over'):
        p[0] = f'div {p[1]}, {p[3]}'
    elif (p[2] == 'by'):
        p[0] = f'div {p[1]}, {p[3]}'


def p_conditional(p):
    '''conditional : expression GT expression
                   | expression LT expression
                   | expression ATTR expression
                   | expression GE expression
                   | expression LE expression'''

    if (p[2] == 'is as high as'):
        p[0] = f'bge {p[1]}, {p[3]}, L2'
    elif (p[2] == 'is as low as'):
        p[0] = f'ble {p[1]}, {p[3]}, L2'
    elif (p[2] == 'is lower as'):
        p[0] = f'blt {p[1]}, {p[3]}, L2'
    elif (p[2] == 'is higher as'):
        p[0] = f'bgt {p[1]}, {p[3]}, L2'
    elif (p[2] == 'is'):
        p[0] = f'beq {p[1]}, {p[3]}, L2'

def p_expression_identifier(p):
    '''expression : identifier
                  | literal'''
    p[0] = p[1]


def p_identifier(p):
    '''identifier : PPVAR
                  | cmvar
                  | ID
                  | PRONOUN'''

    p[0] = p[1]


def p_cmvar(p):
    '''cmvar : CMVAR ID'''

    p[0] = f'${p[1]}{p[2]}'


def p_literal(p):
    '''literal : LITERALNUM
               | LITERALSTR
               | TRUE
               | FALSE
               | NULL
               | poetic'''

    p[0] = p[1]


def p_poetic(p):
    '''poetic : POETIC'''

    number = ""
    for word in p[1].split():
        number += str(len(word) % 10)
    p[0] = int(number)


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    global results
    if p:
        results.append(('error', f'BONO? {p}'))
    else:
        results.append(('error', 'WTF?!'))
    parser.restart()


parser = yacc.yacc()


def syntactic_ballad(code):
    global results
    results = []
    code = code.split('\n')
    code = [x for x in code if x]
    for line in code:
        parser.parse(line)
    return results
