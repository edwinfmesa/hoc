import ply.lex as lex

keywords= {
    'while':'WHILE',
    'if':'IF',
    'else':'ELSE',
    'print':'PRINT',
    'read':'READ',
    'proc':'PROC',
    'procedure':'PROCEDURE',
    'fun':'FUN',
    'function':'FUNCTION',
    'return':'RETURN',
    'for':'FOR',
    'local':'LOCAL'
}

constants = {
    'PI':'PI',
    'PHI':'PHI',
    'GAMMA':'GAMMA',
    'E':'E',
    'DEG':'DEG',
    'PREC':'PREC'
}

bltn = {
    'sin':'SIN',
    'cos':'COS',
    'tan':'TAN',
    'asin':'ASIN',
    'acos':'ACOS',
    'atan':'ATAN',
    'sinh':'SINH',
    'cosh':'COSH',
    'tanh':'TANH',
    'exp':'EXP',
    'int':'INT',
    'log':'LOG',
    'log10':'LOG10',
    'sqrt':'SQRT',
    'abs':'ABS',
    'erf':'ERF',
    'erfc':'ERFC',

}

tokens = [
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
   

] 

tokens += keywords.values() + constants.values() + bltn.values()


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

t_ignore = '\t\n\" "'
# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

def t_FLOAT(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t



# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)
    
def t_ID(t):
   r'[a-zA-Z_][a-zA-Z0-9_]*'
   if t.value in keywords:
      t.type=keywords[t.value]
   elif  t.value in constants: 
      t.type=constants[t.value]
   elif t.value in bltn:
      t.type=bltn[t.value]
   return t

    

lexico = lex.lex()

t1="""
3+4%
1&&3
2 ||3
1!==3<
4>1
2<=2
9>=10
1++(3)
1$2
"""

t2="""

if
2+2
i=1
if
pi
PI
sin 
cos(0)
5.0
3E
"""

s = t2
print s

lexico.input(s)
print "\n--------------------Lexer retorna------------------------\n\n"
# try:
while True:
   tokenizer = lexico.token()
   if not tokenizer: break
   print tokenizer
# except:
#     print "Unknown ERROR"
# print("\n Please press any key... ")
# wait()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    