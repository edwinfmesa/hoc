import libs.ply.lex as lex

keywords= {
    'while':'WHILE',
    'if':'IF',
    'else':'ELSE',
    'print':'PRINT',
    'read':'READ',
    'proc':'PROC',
    'procedure':'PROCEDURE',
    'func':'FUNC',
    'function':'FUNCTION',
    'return':'RETURN',
    'for':'FOR',
    'local':'LOCAL',
    'begin':'BEGIN',
    'end' : 'END'
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
    'sin':'BLTIN',
    'cos':'BLTIN',
    'tan':'BLTIN',
    'asin':'BLTIN',
    'acos':'BLTIN',
    'atan':'BLTIN',
    'sinh':'BLTIN',
    'cosh':'BLTIN',
    'tanh':'BLTIN',
    'int':'BLTIN',
    'log':'BLTIN',
    'log10':'BLTIN',
    'sqrt':'BLTIN',
    'abs':'BLTIN',
    'erf':'BLTIN',
    'erfc':'BLTIN',

}

tokens = [
   'STRING',
   'COMMENT',
   'FLOAT', 
   'NUMBER',
   'ID',
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
   'DOLLAR',
   'EXP',
   'LPARENT',
   'RPARENT',
   'LBRACKET',
   'RBRACKET',
   'COMMA',
   'SEMICOLON',
   'NEWLINE'
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
t_DOLLAR = r'\$'
t_EXP = r'\^'
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_COMMA = r','
t_SEMICOLON = r';'
t_NEWLINE = r'\n'






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

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

    
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value in keywords:
      t.type=keywords[t.value]
    elif  t.value in constants: 
      t.type=constants[t.value]
    elif t.value in bltin:
      t.type='BLTIN'
    return t

def t_error_STRING(t):
    r'\".*'
    print ("Error: with string: ", t.value, " Line: ", t.lineno)
    t.lexer.skip(1)

def t_COMMENT(t):
    r'[##].*'
    return t

t_ignore = '\t '

# lexico = lex.lex()

# t1="""
# 3+4%
# 1&&3
# 2 ||3
# 1!==3<
# 4>1
# 2<=2
# 9>=10
# 1++(3)
# 1$2
# """

# t2="""

# if
# 2+2
# i=1
# if
# pi
# PI
# sin 
# cos(0)
# 5.0
# 3E
# """

# t3="""
# 4.5
# 3
# 565.999
# -34
# -344.44
# 4E
# 5E1
# 5E6
# 6E-5
# -3E-4
# """

# t4="""
# 3+4-8+2/4*8
# 4+1+2*PHI
# print (7-8-1)+E
# tan(PI/3)+cos(2*pi)
# """

# t5="""
# while (read(x)) {
#      print "Prueba de modulo ", x%40000
# } 
# ## esto es un comentario en hoc
# hola
# "esto es un error 
# @
# """

# t6='''
# proc squares(){ 
#     local i, j, k 
#     for (i=1; i <= $1; i=i+1){ 
#         print i*i 
#     }
# } 
# '''

# t7="""
# func reciduous(){
#     if ($1 ==$2) {
#        return 1
#     } else {
#       return $1/$2
#     } 
# } 
# """
# t8="""
# func cuadrado(){
#     if ($1 ==0) {
#        return 1
#     } else {
#       return $1*$1
#     } 
# } 
# """
# t9="""
# func factorial(){
#     if ($1 ==0) {
#        return 1
#     } else {
#         while ($1 >0){
#             $2 += $1
#         }
#         $1= $1-1
#         return $2
#     } 
# } 
# """
# t10="""
# func igual(){
#     if ($1 ==$2) {
#         return 1
#     } else {
#         return 0
#     } 
# } 
# igual(3,3)
# """

# test = t1
# print test

# lexico.input(test)

# print "\n--------------------Lexer retorna------------------------\n\n"

# while True:
#    tokenizer = lexico.token()
#    if not tokenizer: break
#    print tokenizer

    

if __name__ == '__main__':
    # Build the lexer
    import sys 
    
    lex = lex.lex()
    
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
    
    lex.input(data)
    
    # Tokenize
    while 1:
            tok = lex.token()
            if not tok: break            # No more input
            print tok
    
      
    
    
    
    
    
    
    
