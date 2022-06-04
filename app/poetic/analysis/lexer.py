from poetic.ply import lex


reserved = {
    'If': 'IF',
    'Else': 'ELSE',
    'While': 'WHILE',
    'Until': 'UNTIL',
    'Listen': 'LISTEN',
    'says': 'SAYS',
    'Say': 'SAY',
    'Shout': 'SHOUT',
    'Whisper': 'WHISPER',
    'Scream': 'SCREAM',
    'mysterious': 'MYSTERIOUS',
}

tokens = [
    'COMMENT', # Comments
    'PRONOUN', # Pronouns
    'COMMONVAR', # Common variables
    'ATTR',
    'TRUE',
    'FALSE',
    'NULL',
    # Boolean literals
    'BOOLEAN',
    'BOOLEANMAYBE',
    # Numeric literals
    'NUMBERINT',
    'NUMBERFLOAT',
    'STRINGLITERAL',
    # Assignments
    'PUT', 'LET', 'INTO', 'BE',
    # Increments and decrements
    'BUILD',
    'KNOCK',
    'UP',
    'DOWN',
    # Operations
    'PLUS',
    'MINUS',
    'TIMES',
    'OVER',
    # Poetic tokens
    'NOT',
    'AINT',
    # Comparisons
    'GT',
    'LT',
    'GE',
    'LE',
    # Control flow
    'BREAK',
    'CONTINUE',
    # Functions
    'FOO',
    'AND',
    'RETURN',
    'TAKING',
    'COMMA',
    'ID'
] + list(reserved.values())

t_BOOLEAN = r'\b(boolean)\b'
t_BOOLEANMAYBE = r'\b(maybe)\b'
t_NUMBERINT = r'\d+'
t_NUMBERFLOAT = r'\d+.\d+'
t_STRINGLITERAL = r'\"[^\"]*\"'
t_BUILD = r'\b[Bb]uild\b'
t_KNOCK = r'\b[Kk]nock\b'
t_UP = r'\b(up)\b'
t_NOT = r'\b(not)\b'
t_AINT = r'\b(ain\'t)\b'
t_BREAK = r'\b(break|Break it down)\b'
t_CONTINUE = r'\b(continue|Take it to the top)\b'
t_AND = r'\b(and)\b'
t_TAKING = r'\b(taking)\b'
t_COMMA = r','
t_ignore = ' \t\r'


def t_COMMENT(t):
    r'(\(.*?\))'
    pass


def t_PRONOUN(t):
    r'\b(?i)(it|he|she|him|her|they|them|ze|hir|zie|zir|xe|xem|ve|ver)\b'
    return t


def t_COMMONVAR(t):
    r'\b(?i)(an|the|my|your)\b'
    return t


def t_DOWN(t):
    r'\b(down)\b'
    return t


def t_PLUS(t):
    r'\b(plus|with)\b'
    return t


def t_MINUS(t):
    r'\b(minus|without)\b'
    return t


def t_TIMES(t):
    r'\b(times|of)\b'
    return t


def t_OVER(t):
    r'\b(over|by)\b'
    return t


def t_TRUE(t):
    r'\b(?i)(true|right|yes|ok)\b'
    return t


def t_FALSE(t):
    r'\b(?i)(false|wrong|no|lies)\b'
    return t


def t_NULL(t):
    r'\b(?i)(null|nothing|nowhere|nobody|gone)\b'
    return t


def t_GT(t):
    r'\b(?i)(is)\s(higher|greater|bigger|stronger)\s(than)\b'
    return t


def t_LT(t):
    r'\b(?i)(is)\s(lower|less|smaller|weaker)\s(than)\b'
    return t


def t_GE(t):
    r'\b(?i)(is)\s(as)\s(high|great|big|strong)\s(as)\b'
    return t


def t_LE(t):
    r'\b(?i)(is)\s(as)\s(low|little|small|weak)\s(as)\b'
    return t


def t_ATTR(t):
    r'\b(?i)(is|are|was|where)\b'
    return t


def t_PUT(t):
    r'\b(?i)(put)\b'
    return t


def t_LET(t):
    r'\b(?i)(let)\b'
    return t


def t_INTO(t):
    r'\b(?i)(into|in)\b'
    return t


def t_BE(t):
    r'\b(?i)(be)\b'
    return t


def t_FOO(t):
    r'\b(?i)(takes|wants)\b'
    return t


def t_RETURN(t):
    r'\b(?i)(give\sback|return\sback|return|give|send)\b'
    return t


def t_ID(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value,'ID')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += 1


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    t.value = t.value[0]
    return t


lexer = lex.lex()

def rock_tokens(code):
    tokens = []
    lexer.lineno = 1
    lexer.input(code)
    while True:
        tok = lexer.token()
        if not tok: break
        token = (tok.type, tok.value, tok.lineno, tok.lexpos)
        tokens.append(token)
    return tokens
