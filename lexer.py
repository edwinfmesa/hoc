import libs.ply.lex as lex

keywords= {
    'while':'WHILE',
    'if':'IF',
    'else':'ELSE',
    'print':'PRINT',
    # 'read':'READ',
    # 'proc':'PROC',
    'procedure':'PROCEDURE',
    'func':'FUNC',
    'function':'FUNCTION',
    'return':'RETURN',
    'for':'FOR',
    # 'local':'LOCAL',
    # 'begin':'BEGIN',
    # 'end' : 'END'
}

constants = {
    'PI':'PI',
    'PHI':'PHI',
    'GAMMA':'GAMMA',
    'E':'E',
    'DEG':'DEG',
    'PREC':'PREC'
}

bltin = {
    'sin':'SIN',
    'cos':'COS',
    'tan':'TAN',
    'asin':'ASIN',
    'acos':'ACOS',
    'atan':'ATAN',
    'sinh':'SINH',
    'cosh':'COSH',
    'tanh':'TANH',
    'int':'INT',
    'log':'LOG',
    'log10':'LOG10',
    'sqrt':'SQRT',
    'abs':'ABS',
    'erf':'ERF',
    'erfc':'ERFC',

}

tokens = [
   'STRING',
   'COMMENT',
   'FLOAT', 
   # 'NUMBER',
   'VAR',
   # 'FUNCTION',
   #simbolos
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   # --------------
   'MOD',
   'AND',
   'OR',
   'NOT',
   'EQ',
   'LT',
   'LE',
   'GT',
   'GE',
   'ADDEQ',
   'SUBEQ',
   'MULEQ',
   'DIVEQ',
   'MODEQ',
   'ASSIGN',
   'NE',
   'INC',
   'DEC',
   'BLTIN',
   'EXP',
   'LPARENT',
   'RPARENT',
   'LBRACKET',
   'RBRACKET',
   'COMMA',
   'SEMICOLON',
   'NEWLINE',
   'UNARYMINUS'
] 

tokens += keywords.values() + constants.values() + bltin.values()


t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_MOD = r'%'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_EQ = r'=='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='
t_ADDEQ = r'\+='
t_SUBEQ = r'-='
t_MULEQ = r'\*='
t_DIVEQ = r'\/='
t_MODEQ = r'%='
t_ASSIGN = r'='
t_NE = r'!='
t_INC = r'\+\+'
t_DEC = r'\-\-'
# t_DOLLAR = r'\$'
t_EXP = r'\^'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_COMMA = r','
t_SEMICOLON = r';'
t_NEWLINE = r'\n'
t_UNARYMINUS = r'\-'






def t_STRING(t):
    r'\"([^\\^\n] |(\\.))*\"'
    return t

def t_error(t):
    print ("Illegal character ",  t.value[0], "Line ", t.lineno)
    t.lexer.skip(1)
    

def t_FLOAT(t):
    r'[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?'
    t.value = float(t.value)
    return t

# def t_NUMBER(t):
#     r'[0-9]+'
#     t.value = int(t.value)
#     return t

    
# def t_FUNCTION(t):
#     r'[a-zA-Z_][a-zA-Z0-9_]*\('
#     if t.value in keywords:
#       t.type=keywords[t.value]
#     elif  t.value in constants: 
#       t.type=constants[t.value]
#     elif t.value in bltin:
#       t.type=bltin[t.value]
#     return t


def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords:
      t.type=keywords[t.value]
    elif  t.value in constants: 
      t.type=constants[t.value]
    elif t.value in bltin:
      t.type='BLTIN'  #bltin[t.value]
    return t




def t_error_STRING(t):
    r'\".*'
    print ("Error: with string: ", t.value, " Line: ", t.lineno)
    t.lexer.skip(1)

def t_COMMENT(t):
    r'[##].*\n'
    return t

t_ignore = '\t \r'

# lexico = lex.lex()



# test = t1
# print test

# lexico.input(test)

# print "\n--------------------Lexer retorna------------------------\n\n"

# while True:
#    tokenizer = lexico.token()
#    if not tokenizer: break
#    print tokenizer

lexer = lex.lex()

if __name__ == '__main__':
    # Build the lexer
    import sys 
    
    
    
    if len(sys.argv) > 1:
        f = open(sys.argv[1],"r")
        data = f.read()
        f.close()
    else:
        data = ""
        while 1:
            try:
                data += raw_input() + "\n"
            except:
                break
    
    lexer.input(data)
    
    # Tokenize
    while 1:
            tok = lexer.token()
            if not tok: break            # No more input
            print tok
    
      
    
    
    
    
    
    
    
