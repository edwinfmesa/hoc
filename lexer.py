import ply.lex as lex

# keywords= {
# 	'while':'WHILE',
# 	'if':'IF',
# 	'else':'ELSE',
# 	'print':'PRINT',
# 	'read':'READ',
# 	'proc':'PROC',
# 	'procedure':'PROCEDURE',
# 	'fun':'FUN',
# 	'function':'FUNCTION',
# 	'return':'RETURN',
# 	'for':'FOR',
# 	'local':'LOCAL'
# }

# constants = {
# 	'PI':'PI',
# 	'PHI':'PHI',
# 	'GAMMA':'GAMMA',
# 	'E':'E',
# 	'DEG':'DEG',
# 	'PREC':'PREC'
# }

# bltn = {
# 	'sin':'SIN',
# 	'cos':'COS',
# 	'tan':'TAN',
# 	'asin':'ASIN',
# 	'acos':'ACOS',
# 	'atan':'ATAN',
# 	'sinh':'SINH',
# 	'cosh':'COSH',
# 	'tanh':'TANH',
# 	'exp':'EXP',
# 	'int':'INT',
# 	'log':'LOG',
# 	'log10':'LOG10',
# 	'sqrt':'SQRT',
# 	'abs':'ABS',
# 	'erf':'ERF',
# 	'erfc':'ERFC',

# }

tokens = [
   # 'NUMBER',
   # 'ID',
   #simbolos
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   # --------------
   # 'MOD',
   # 'AND',
   # 'OR',
   # 'NOT',
   # 'EQ',
   # 'LT',
   # 'LE',
   # 'GT',
   # 'GE',
   # 'ADDEQ',
   # 'SUBEQ',
   # 'MULEQ',
   # 'DIVEQ',
   # 'MODEQ',
   # 'ASSIGN',
   # 'NE',
   # 'INC',
   # 'DEC',
   # 'DOLLAR',
   # 'EXP',
   # 'LPARENT',
   # 'RPARENT',
   

]
#+ list(keywords.values())+ list(constants.values())+ list(bltn.values())


t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
# t_MOD = r'%'
# t_AND = r'&&'
# t_OR = r'\|\|'
# t_NOT = r'!'
# t_EQ = r'=='
# t_LT = r'<'
# t_LE = r'<='
# t_GT = r'>'
# t_GE = r'>='
# t_ADDEQ = r'\+='
# t_SUBEQ = r'-='
# t_MULEQ = r'\*='
# t_DIVEQ = r'\/='
# t_MODEQ = r'%='
# t_ASSIGN = r'='
# t_NE = r'!='
# t_INC = r'\+\+'
# t_DEC = r'\-\-'
# t_DOLLAR = r'\$'
# t_EXP = r'\^'
# t_LPARENT = r'\('
# t_RPARENT = r'\)'

t_ignore = '\t'

# def t_NUMBER(t):
# 	r'[0-9]+'
# 	t.value = int(t.value)
# 	return t

# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)
	
# def t_ID(t):
# 	r'[a-zA-Z_][a-zA-Z0-9_]*'
# 	# if t.value in keywords.value() or t.value in constants.value() or t.value in bltn.value():
# 	# 	t.value=t.type
# 	return t

	

lexico = lex.lex()

t1="""
3+4
"""

s = t1
print s

lexico.input(s)
print "\n\n --------------------RETURN------------------------\n\n"
# try:
while True:
    tokenizer = lexico.token()
    if not tokenizer: break
    print tokenizer
# except:
#     print "Unknown ERROR"
# print("\n Please press any key... ")
# wait()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	