import libs.ply.yacc as yacc
from lexer import *
from hocast import *
import inspect 

cont=0

def get_p(p):
    try:
        a = ' ---------- TYPE: ' + p.type
    except:
        try:
            a = ' ---------- EXC: ' + ' '.join(str(x) for x in p[1:]) 
        except:
            a =  p
    return a


    
# -------------------------------------------------------------------------
# reglas de produccion     
    
def p_program(p):
    "program : empty"
    p[0] = ProgList([p[1]])        
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_program(p):
    "program : stmt NEWLINE"
    p[0] = ProgList([p[1]])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
def p_program2(p):
    "program : program stmt NEWLINE"
    p[1].append(p[2])
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1

def p_factor_float(p):
    "factor : FLOAT"
    p[0] = Literal(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
def p_factor_var(p):
    "factor : VAR"
    p[0] = Location(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_factor_uminus(p):
    "factor : '-' factor"
    p[0] = UnaryOp('-',p[2])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_factor_group(p):
    "factor : '(' factor ')' "
    p[0] = p[2]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_stmt_asign(p):
    "stmt : VAR '=' expr"
    p[0] = BinaryOP('=',Location(p[1]), p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_stmt_expr(p):
    "stmt : expr"
    p[0] = p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_expr_plus(p):
    "expr : expr PLUS term "
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_expr_minus(p):
    "expr : expr '-' term "
    p[0] = BinaryOp('-', p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_expr_term(p):
    "expr : term"
    p[0] = p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_term_mult(p):
    "term : term '*' factor "
    p[0] = BinOp('*', p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_term_div(p):
    "term : term '/' factor "
    p[0] = BinOp('/', p[1], p[3]) 
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_term_factor(p):
    "term : factor"
    p[0] = p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_empty(p):
    "empty : "
    p[0] = ""
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    

def p_error(p):
    'error : error'
    global cont
    print cont, inspect.stack()[0][3], 'ERROR', get_p(p)
    cont = cont + 1
    print p
    if p:
         print("Syntax error at token", p.type)
         parser.errok()
    else:
         print("Syntax error at EOF")
    
    
parser = yacc.yacc()

if __name__ == '__main__':
    
    import sys 
    cont=0

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
    
    # resp = parser.parse(data+"\n")
    print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    root = yacc.parse(data+"\n")
    print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    print root.pprint()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    