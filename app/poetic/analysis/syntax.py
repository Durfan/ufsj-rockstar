import re
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

    if (len(p) == 2):
        p[0] = p[1]
    elif (len(p) == 3):
        p[0] = (p[1], p[2])
    elif (len(p) > 3):
        p[0] = (p[1], p[2])

    global results
    results.append(f'statement: {p[0]}')


def p_assignment(p):
    '''assignment : identifier ATTR expression
                  | BUILD identifier UP
                  | KNOCK identifier DOWN
                  | PUT expression IN identifier'''

    if (len(p) == 4):
        p[0] = ('Assign', p[1], p[3])
    else:
        p[0] = ('Assign', p[2], p[3])


def p_function(p):
    '''function : identifier FOO args'''

    p[0] = ('FOO', p[1])


def p_args(p):
    '''args : identifier LOGICAL args
            | identifier'''
    
    if (len(p) == 4):
        p[0] = ('args', p[1], p[3])
    else:
        p[0] = p[1]


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULT expression
                  | expression DIV expression'''

    p[0] = p[2]


def p_conditional(p):
    '''conditional : expression GT expression
                   | expression LT expression
                   | expression ATTR expression
                   | expression GE expression
                   | expression LE expression'''

    p[0] = ('conditional', p[2])


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

    p[0] = ('common', p[1] + '_' + p[2])


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
    p[0] = number


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    global results
    results.append(f'BONO? {p}')
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
