import libs.ply.yacc as yacc
from lexer import *
from hocast import *
import inspect
# from visitor import *

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

# def p_program(p):
#     "program : list"
#     # print "AQUI!----",p[0],"-",p[1]
#     p[0] = Program(p[1])
#     global cont
#     print cont, inspect.stack()[0][3] + get_p(p)
#     cont = cont + 1
    
# -------------------------------------------------------

def p_list_empty(p):
    "list : empty"
    p[0]=ProgList([p[1]])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_list_nl(p):
    " list : list  newline "
    p[1].append(p[2])
    p[0]= p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    
    cont = cont + 1
        

def p_list_defn(p):
    "list : list defn newline"
    # print "AQUI!----",p[0],"-",p[1],"-",p[2],"-",p[3]
    p[1].append(p[2])
    p[0]= p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_list_asgn(p):
    " list : list asgn newline "
    p[1].append(p[2])
    p[0]= p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
def p_list_stmt(p):
    "list : list stmt newline "
    p[1].append(p[2])
    p[0]= p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
    
def p_list_expr(p):
    "list : list expr newline"
    p[1].append(p[2])
    p[0]= p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_list_error(p):
    "list : list error newline"
    p[1].append(p[2])
    p[0]= p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_list_comment(p):
    "list : list COMMENT newline"
    p[1].append(p[2])
    p[0]= p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        



# --------------------------asgn--------------------------

def p_asgn_equal(p):
    "asgn : VAR ASSIGN expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_asgn_addeq(p):
    "asgn : VAR ADDEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_asgn_subeq(p):
    "asgn : VAR SUBEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_asgn_muleq(p):
    "asgn : VAR MULEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_asgn_diveq(p):
    "asgn : VAR DIVEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_asgn_modeq(p):
    "asgn : VAR MODEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    

# ------------------------------------------------------

def p_stmt_expr(p):
    "stmt : expr"
    p[0] = Statement(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    

def p_stmt_return(p):
    "stmt : RETURN"
    p[0] = Statement(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_stmt_return_expr(p):
    "stmt : RETURN  expr "
    p[0]=Statement(ReturnValue(P[1],P[2]))
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

# def p_stmt_proc(p): # COmentado por conflicto
#     "stmt : callproc "
#     p[0]=p[1] 
    

def p_stmt_print(p):
    "stmt : PRINT prlist"
    p[0]=Statement(PrintValue(P[1],P[2]))
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_stmt_while(p):
    "stmt : WHILE  LPARENT cond RPARENT stmt"
    p[0]=Statement(p[1]) # Pendiente
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_stmt_for(p):
    "stmt : FOR LPARENT cond SEMICOLON cond SEMICOLON cond RPARENT stmt"
    p[0]=Statement(p[1]) # Pendiente
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_stmt_if(p):
    "stmt : IF LPARENT cond RPARENT stmt"
    p[0]=Statement(p[1]) # Pendiente
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_stmt_if_else(p):
    "stmt : IF LPARENT cond RPARENT stmt  ELSE stmt "
    p[0]=Statement(p[1]) # Pendiente
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_stmt_braket(p):
    "stmt : LBRACKET stmtlist RBRACKET "
    p[0]=Statement(p[1]) # Pendiente
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

# -----------------------------------------------------

def p_cond_expr(p):
    "cond : expr "
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
# -----------------------------------------------------

def p_stmtlist_empty(p):
    "stmtlist : empty "
    p[0]=StatementsList([Empty()])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_stmlist_newline(p):
    "stmtlist : stmtlist newline"
    p[1].append(p[2])
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
def p_stmtlist_stmt(p):
    "stmtlist : stmtlist stmt "
    p[1].append(p[2])
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
# ---------------expr-----------------------------------------

def p_expr_data(p):
    "expr : data"
    p[0]=Expression(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
def p_expr_asgn(p):
    "expr : asgn"
    p[0]=Expression(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_expr_unaryop(p):
    "expr : unaryop"
    p[0]=Expression(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_expr_binaryop(p):
    "expr : binaryop"
    p[0]=Expression(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_expr_group(p):
    "expr : LPARENT expr RPARENT"
    p[0]=Expression(GroupParent(P[1],p[2],p[3]))
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_data_callfunc(p):
    "expr : callfunc"
    p[0]=Expression(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
# ---------------data----------------------------------------

def p_data_float(p):
    "data : FLOAT"
    p[0]=Literal(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        # print "FLoat", p[0],p[1]
    

def p_data_constant(p):
    "data : constant"
    p[0]=Literal(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_data_VAR(p):
    "data : VAR "
    p[0]=StoreVar(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    

# ------------------ VARiable -------------------------

# def p_id_VAR(p):
#     "VAR : VAR"
#     p[0] = p[1]
#     global cont
#     print cont, inspect.stack()[0][3] + get_p(p)
#     cont = cont + 1
    

#  -------------unaryop---------------------------------------------


def p_unaryop_munit(p):
    "unaryop : UNARYMINUS expr "
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    


def p_unaryop_inc(p):
    "unaryop : INC VAR"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_unaryop_dec(p):
    "unaryop : DEC VAR"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_unaryop_inc2(p):
    "unaryop : VAR INC"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_unaryop_dec2(p):
    "unaryop : VAR DEC"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
def p_not_expr(p):
    "unaryop : NOT  expr"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

# ----------------binaryop--------------------------------------------------


def p_binaryop_mathop(p):
    "binaryop : mathop"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_binaryop_logicop(p):
    "binaryop : logicop"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    



# -----------------mathop------------------------------------


# def p_expr_function(p):
#     "expr : FUNCTION BEGIN"
#     



# def p_expr_bltin(p):
#     "expr : BLTIN LPARENT expr RPARENT"
#     


def p_mathop_exp(p):
    'mathop : expr EXP expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1

    
def p_mathop_plus(p):
    'mathop : expr PLUS expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_mathop_minus(p):
    'mathop : expr MINUS expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
    
def p_mathop_times(p):
    "mathop : expr TIMES expr"
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_mathop_divide(p):
    "mathop : expr DIVIDE expr"
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_mathop_mod(p):
    "mathop : expr MOD expr"
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

# ----------------logicop --------------

def p_logicop_lt(p):
    'logicop : expr LT expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_logicop_gt(p):
    'logicop : expr GT expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_logicop_le(p):
    'logicop : expr LE expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_logicop_ge(p):
    'logicop : expr GE expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_logicop_eq(p):
    'logicop : expr EQ expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_logicop_ne(p):
    'logicop : expr NE expr '
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
    
def p_logicop_or(p):
    'logicop : expr OR expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_logicop_and(p):
    'logicop : expr AND expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
    

# ---------------callfunc ---------------------------

def p_callfunc_bltn(p):
    "callfunc : bltin LPARENT arglist RPARENT"
    p[0]=Calls(p[1],p[3])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

# def p_callproc(p): comentado por conflicto
#     "callproc : procname LPARENT arglist RPARENT"
#     p[0]=p[1]

def p_callfunc(p):
    "callfunc : FUNCTION arglist RPARENT"
    p[0]=Calls(p[1],p[2])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
# -----------------procname --------------------------

# def p_procname_id(p): #comentado por conflicto
#     "procname : ID"
#     p[0]=p[1]

# def p_funcname_id(p): 
#     "funcname : ID"
#     p[0]=p[1]
#     global cont
#     print cont, inspect.stack()[0][3] + get_p(p)
#     cont = cont + 1
    

# ------------------------------------------------------

def p_prlist_expr(p):
    "prlist : expr"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_prlist_str(p):
    "prlist : STRING"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_prlist_comma_expr(p):
    "prlist : prlist COMMA expr"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_prlist_comma_str(p):
    "prlist : prlist COMMA STRING"
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

# -----------------------def func----------------------------------

def p_defn_func(p):
    "defn : FUNC FUNCTION formals RPARENT stmt"
    p[0]=[p[1]]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

# def p_defn_proc(p): # conflicto con procedimientos
#     "defn : PROC procname LPARENT formals RPARENT stmt"
#     p[0]=p[1]
    

# ------------------------formals-----------------------------------

def p_formals_empty(p):
    "formals : empty"
    p[0]=FormalsList([p[1]])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    
def p_formals_VAR(p):
    "formals : VAR"
    p[0]=FormalsList([p[1]])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_formals_comma_VAR(p):
    "formals : formals COMMA VAR"
    p[1].append(p[3])
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

# --------------------arglist----------------------------

def p_arglist_empty(p):
    "arglist : empty"
    p[0]=ArgList([p[1]])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_arglist_expr(p):
    "arglist : expr"
    p[0]=ArgList([p[1]])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

def p_arglist_comma_expr(p):
    "arglist : arglist COMMA expr"
    p[1].append(p[3])
    p[0]=p[1]
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        

# ----------------------------------------------------

def p_empty(p):
    "empty : "
    p[0]=Empty()
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
def p_newline(p):
    "newline : NEWLINE"
    p[0]=Literal(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1


# -----------------bltin--------------------------------------

def p_bltin(p):
    """
    bltin : SIN 
        | COS 
        | TAN 
        | ASIN 
        | ACOS 
        | ATAN 
        | SINH 
        | COSH 
        | TANH 
        | INT 
        | LOG 
        | LOG10 
        | SQRT 
        | ABS 
        | ERF 
        | ERFC
    """
    p[0] = Literal(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
    

# ------------------- constants ---------------------------------

def p_constant(p):
    """
    constant : PI
        | PHI
        | GAMMA
        | E
        | DEG
        | PREC
    """
    p[0] = Literal(p[1])
    global cont
    print cont, inspect.stack()[0][3] + get_p(p)
    cont = cont + 1
        
# ----------------------------Error-----------------------------

def p_error(p):
    'error : error'
    global cont
    print cont, inspect.stack()[0][3], "ERROR", get_p(p)
    cont = cont + 1
    print p
    if p:
         print("Syntax error at token", p.type)
         parser.errok()
    else:
         print("Syntax error at EOF")


# --------------------------------------------------------------

precedence = (
    ('right', 'ASSIGN', 'ADDEQ', 'SUBEQ', 'MULEQ', 'DIVEQ', 'MODEQ'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'GT','GE','LT','LE','EQ','NE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE','MOD'),
    ('left', 'UNARYMINUS','NOT','INC','DEC'),
    ('left', 'EXP'),
    ('left','VAR'),
    ('left', 'NEWLINE'),
    ('left','PI','PHI','GAMMA','E','DEG','PREC'),
    ('left', 'SIN', 'COS', 'TAN', 'ASIN', 'ACOS', 'ATAN', 'SINH', 'COSH', 'TANH' , 'INT', 'LOG', 'LOG10',  'SQRT', 'ABS', 'ERF', 'ERFC'),
    ('left','FLOAT'),
    # ('right','LPARENT'),

)

# ----------------------------------------------

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
    root = yacc.parse(data+ "\n")
    print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    print root.pprint()
    print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    print DotVisitor(root)
