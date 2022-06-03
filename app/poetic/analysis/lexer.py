import poetic.ply as lex


tokens = (
    'CommonVariable',
    'Pronoun',
    'Mysterious',
    'Null',
    'Boolean',
    'BooleanTrue',
    'BooleanFalse',
    'BooleanMaybe',
    'NumberInt',
    'NumberFloat',
    'StringLiteral',
    'Put',
    'Into',
    'Build',
    'Knock',
    'Up',
    'TokDown',
    'Plus',
    'Minus',
    'Times',
    'Over',
    'Is',
    'Says',
    'Not',
    'Aint',
 )


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)