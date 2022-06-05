
tk_EOI, tk_Mul, tk_Div, tk_Mod, tk_Add, tk_Sub, tk_Negate, tk_Not, tk_Lss, tk_Leq, tk_Gtr, \
tk_Geq, tk_Eql, tk_Neq, tk_Assign, tk_And, tk_Or, tk_If, tk_Else, tk_While, tk_Print,      \
tk_Putc, tk_Lparen, tk_Rparen, tk_Lbrace, tk_Rbrace, tk_Semi, tk_Comma, tk_Ident,          \
tk_Integer, tk_String = range(31)

nd_Ident, nd_String, nd_Integer, nd_Sequence, nd_If, nd_Prtc, nd_Prts, nd_Prti, nd_While, \
nd_Assign, nd_Negate, nd_Not, nd_Mul, nd_Div, nd_Mod, nd_Add, nd_Sub, nd_Lss, nd_Leq,     \
nd_Gtr, nd_Geq, nd_Eql, nd_Neq, nd_And, nd_Or = range(25)

all_syms = {
    'End_of_input'   : 'tk_EOI',
    'Op_multiply'    : 'tk_Mul',
    'Op_divide'      : 'tk_Div',
    'Op_mod'         : 'tk_Mod',
    'Op_add'         : 'tk_Add',
    'Op_subtract'    : 'tk_Sub',
    'Op_negate'      : 'tk_Negate',
    'Op_not'         : 'tk_Not',
    'Op_less'        : 'tk_Lss',
    'Op_lessequal'   : 'tk_Leq',
    'Op_greater'     : 'tk_Gtr',
    'Op_greaterequal': 'tk_Geq',
    'Op_equal'       : 'tk_Eql',
    'Op_notequal'    : 'tk_Neq',
    'Op_assign'      : 'tk_Assign',
    'Op_and'         : 'tk_And',
    'Op_or'          : 'tk_Or',
    'Keyword_if'     : 'tk_If',
    'Keyword_else'   : 'tk_Else',
    'Keyword_while'  : 'tk_While',
    'Keyword_print'  : 'tk_Print',
    'Keyword_putc'   : 'tk_Putc',
    'LeftParen'      : 'tk_Lparen',
    'RightParen'     : 'tk_Rparen',
    'LeftBrace'      : 'tk_Lbrace',
    'RightBrace'     : 'tk_Rbrace',
    'Semicolon'      : 'tk_Semi',
    'Comma'          : 'tk_Comma',
    'Identifier'     : 'tk_Ident',
    'Integer'        : 'tk_Integer',
    'String'         : 'tk_String'
}

TK_NAME         = 0
TK_RIGHT_ASSOC  = 1
TK_IS_BINARY    = 2
TK_IS_UNARY     = 3
TK_PRECEDENCE   = 4
TK_NODE         = 5

input_tks  = None
err_line   = None
err_col    = None
tok        = None
tok_text   = None


class Node:
    def __init__(self, node_type, left = None, right = None, value = None):
        self.node_type  = node_type
        self.left  = left
        self.right = right
        self.value = value


def error(msg):
    print("(%d, %d) %s" % (int(err_line), int(err_col), msg))


def gettok():
    global err_line, err_col, tok, tok_text, tok_other
    line = input_file.readline()
 
    line_list = shlex.split(line, False, False)
    # line col Ident var_name
    # 0    1   2     3
 
    err_line = line_list[0]
    err_col  = line_list[1]
    tok_text = line_list[2]
 
    tok = all_syms.get(tok_text)
    if tok == None:
        error("Unknown token %s" % (tok_text))
 
    tok_other = None
    if tok in [tk_Integer, tk_Ident, tk_String]:
        tok_other = line_list[3]

 
def make_node(oper, left, right = None):
    return Node(oper, left, right)


def parse(tokens):
    t = None
    gettok()
    while True:
        t = make_node(nd_Sequence, t, stmt())
        if tok == tk_EOI or t == None:
            break
    return t
