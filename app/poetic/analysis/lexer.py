from poetic.ply import lex


tokens = [
    'COMMENT',
    'CMVAR','PRONOUN',
    'TRUE','FALSE','NULL',
    'ATTR',
    'INT','FLOAT',
    'LITERALSTR',
    'PUT','LET','IN','BE',
    'BUILD','KNOCK',
    'UP','DOWN',
    'PLUS','MINUS','MULT','DIV',
    'IF','GT','LT','GE','LE',
    'LOGICAL',
    'LISTEN','SAY',
    'LOOP','BREAK','CONTINUE',
    'FOO','CALL','SEND',
    'AND',
    'COMMA',
    'PPVAR',
    'ID',
    'END'
]

def t_COMMENT(t):
    r'(\(.*?\))'
    pass

t_CMVAR = r'\b(?i:an|the|my|your)\b'
t_PRONOUN = r'\b(?i:it|he|she|him|her|they|them|ze|hir|zie|zir|xe|xem|ve|ver)\b'

t_ATTR = r'\b(?i:is|are|was|where)\b'

# Constants
t_TRUE = r'\b(?i:maybe|true|right|yes|ok)\b'
t_FALSE = r'\b(?i:definitely\smaybe|false|wrong|no|lies)\b'
t_NULL = r'\b(?i:null|nothing|nowhere|nobody|gone)\b'

t_INT = r'\d+'
t_FLOAT = r'\d+.\d+'

def t_LITERALSTR(t):
    r'\"(.*?)\"'
    t.value = t.value[1:-1]
    return t

# Assignments
t_PUT = r'\b(?i:put)\b'
t_LET = r'\b(?i:let)\b'
t_IN  = r'\b(?i:into|in)\b'
t_BE  = r'\b(?i:be)\b'

# Increment and Decrement
t_BUILD = r'\b(?i:build)\b'
t_KNOCK = r'\b(?i:knock)\b'
t_UP    = r'\b(?i:up)\b'
t_DOWN  = r'\b(?i:down)\b'

# Operators
t_PLUS  = r'\b(?i:plus|with)\b'
t_MINUS = r'\b(?i:minus|without)\b'
t_MULT  = r'\b(?i:times|of)\b'
t_DIV   = r'\b(?i:over|by)\b'

# Comparisons
t_IF = r'\b(?i:if)\b'
t_GT = r'\b(?i:is)\s(?i:higher|greater|bigger|stronger)\s(?i:than)\b'
t_LT = r'\b(?i:is)\s(?i:lower|less|smaller|weaker)\s(?i:than)\b'
t_GE = r'\b(?i:is)\s(?i:as)\s(?i:high|great|big|strong)\s(?i:as)\b'
t_LE = r'\b(?i:is)\s(?i:as)\s(?i:low|little|small|weak)\s(?i:as)\b'

# Logical Operations
t_LOGICAL = r'\b(?i:and|or|nor|not)\b'

# Input/Output
t_LISTEN = r'\b(?i:listen\sto|listen)\b'
t_SAY = r'\b(?i:shout|whisper|scream|say)\b'

# Loops
t_LOOP     = r'\b(?i:while|until)\b'
t_BREAK    = r'\b(?i:break\sit\sdown|break)\b'
t_CONTINUE = r'\b(?i:take\sit\sto\sthe\stop|continue)\b'

# Functions
t_FOO  = r'\b(?i:takes|wants)\b'
t_CALL = r'\b(?i:taking)\b'
t_SEND = r'\b(?i:give\sback|return\sback|return|give|send)\b'

t_COMMA = r','
t_PPVAR = r'[A-Z][a-z]*'
t_ID = r'[a-z]+'


def t_END(t):
    r'(\n{2})'
    t.value = 'Blank Line'
    t.lexer.lineno += 2
    return t


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1


t_ignore = ' \t\r'


def t_error(t):
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
        if not tok:
            tokens.append(('EOI','The End',0,0))
            break
        token = (tok.type, tok.value, tok.lineno, tok.lexpos)
        tokens.append(token)
    return tokens
