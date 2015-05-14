import libs.ply.yacc as yacc
from lexer import *
from hocast import *

def p_program(p):
    "program : list"
    p[0] = p[1]

# -------------------------------------------------------

def p_list_empty(p):
    "list : empty"
    p[0]=p[1]
    pass

def p_list_nl(p):
    " list : list  NEWLINE "
    p[0]=p[1]
    pass

def p_list_defn(p):
    "list : list defn NEWLINE"
    p[0]=p[1]
    pass

# def p_list_asgn(p):
#     " list : list asgn NEWLINE "
    # pass

def p_list_stmt(p):
    "list : list stmt NEWLINE "
    p[0]=p[1]

    pass

def p_list_expr(p):
    "list : list expr NEWLINE"
    p[0] = p[2]
    pass

def p_list_error(p):
    "list : list error NEWLINE"
    p[0]=p[1]
    pass

def p_list_comment(p):
    "list : list COMMENT NEWLINE"
    p[0]=p[1]
    pass



# ----------------------------------------------------


# ------------------------------------------------------

# def p_stmt_expr(p):
#     "stmt : expr"
#     pass

def p_stmt_return(p):
    "stmt : RETURN"
    p[0]=p[1]
    pass

def p_stmt_return_expr(p):
    "stmt : RETURN expr "
    p[0]=p[1]
    pass

def p_stmt_proc(p):
    "stmt : PROCEDURE BEGIN LPARENT arglist RPARENT"
    p[0]=p[1]
    pass

def p_stmt_print(p):
    "stmt : PRINT prlist"
    p[0]=p[1]
    pass

def p_stmt_while(p):
    "stmt : WHILE  LPARENT cond RPARENT stmt END "
    p[0]=p[1]
    pass

def p_stmt_for(p):
    "stmt : FOR LPARENT cond SEMICOLON cond SEMICOLON cond RPARENT stmt END"
    p[0]=p[1]
    pass

def p_stmt_if(p):
    "stmt : IF LPARENT cond RPARENT stmt END"
    p[0]=p[1]
    pass

def p_stmt_if_else(p):
    "stmt : IF LPARENT cond RPARENT stmt END ELSE stmt END"
    p[0]=p[1]
    pass

def p_stmt_braket(p):
    "stmt : LBRACKET stmtlist RBRACKET "
    p[0]=p[1]
    pass

# -----------------------------------------------------

def p_cond_expr(p):
    "cond : expr "
    p[0]=p[1]
    pass

# -----------------------------------------------------

def p_stmtlist_empty(p):
    "stmtlist : empty "
    p[0]=p[1]
    pass

def p_stmlist_newline(p):
    "stmtlist : stmtlist NEWLINE"
    p[0]=p[1]
    pass

def p_stmtlist_stmt(p):
    "stmtlist : stmtlist stmt "
    p[0]=p[1]
    pass

# ---------------expr-----------------------------------------

def p_expr_data(p):
    "expr : data"
    p[0]=p[1]
    pass

def p_expr_unaryop(p):
    "expr : unaryop"
    p[0]=p[1]
    pass

def p_expr_binaryop(p):
    "expr : binaryop"
    p[0]=p[1]
    pass

def p_expr_group(p):
    "expr : LPARENT expr RPARENT"
    p[0]=p[1]
    pass

def p_data_callfunc(p):
    "expr : callfunc"
    p[0]=p[1]
    pass
# ---------------data----------------------------------------

def p_data_float(p):
    "data : FLOAT"
    p[0]=p[1]
    # print "FLoat", p[0],p[1]
    pass

def p_data_constant(p):
    "data : constant"
    p[0]=p[1]
    pass

def p_data_id(p):
    "data : ID "
    p[0]=p[1]
    pass

#  -------------unaryop---------------------------------------------


def p_unaryop_munit(p):
    "unaryop : UNARYMINUS expr "
    p[0]=p[1]
    pass

def p_unaryop_inc(p):
    "unaryop : INC ID"
    p[0]=p[1]
    pass

def p_unaryop_dec(p):
    "unaryop : DEC ID"
    p[0]=p[1]
    pass

def p_unaryop_inc2(p):
    "unaryop : ID INC"
    p[0]=p[1]
    pass

def p_unaryop_dec2(p):
    "unaryop : ID DEC"
    p[0]=p[1]
    pass

# ----------------binaryop--------------------------------------------------

def p_binaryop_asgn(p):
    "binaryop : asgn"
    p[0]=p[1]
    pass

def p_binaryop_mathop(p):
    "binaryop : mathop"
    p[0]=p[1]
    pass

def p_binaryop_logicop(p):
    "binaryop : logicop"
    p[0]=p[1]


# -----------------asgn---------------------------------------------------

def p_asgn_equal(p):
    "asgn : ID ASSIGN expr "
    p[0]=p[1]
    pass

def p_asgn_addeq(p):
    "asgn : ID ADDEQ expr "
    p[0]=p[1]
    pass

def p_asgn_subeq(p):
    "asgn : ID SUBEQ expr "
    p[0]=p[1]
    pass

def p_asgn_muleq(p):
    "asgn : ID MULEQ expr "
    p[0]=p[1]
    pass

def p_asgn_diveq(p):
    "asgn : ID DIVEQ expr "
    p[0]=p[1]
    pass

def p_asgn_modeq(p):
    "asgn : ID MODEQ expr "
    p[0]=p[1]
    pass


# -----------------mathop------------------------------------


# def p_expr_function(p):
#     "expr : FUNCTION BEGIN"
#     pass



# def p_expr_bltin(p):
#     "expr : BLTIN LPARENT expr RPARENT"
#     pass

# def p_expr_parent(p):
#     "expr : LPARENT expr RPARENT"
#     pass

def p_mathop_exp(p):
    'mathop : expr EXP expr'
    p[0]=p[1]

def p_mathop_plus(p):
    'mathop : expr PLUS expr'
    p[0]=p[1]+p[3]
    pass

def p_mathop_minus(p):
    'mathop : expr MINUS expr'
    p[0]=p[1] - p[3]
    pass
    
def p_mathop_times(p):
    "mathop : expr TIMES expr"
    p[0]=p[1] * p[3]
    pass

def p_mathop_divide(p):
    "mathop : expr DIVIDE expr"
    p[0]=p[1]
    pass

def p_mathop_mod(p):
    "mathop : expr MOD expr"
    p[0]=p[1]
    pass

# ----------------logicop --------------

def p_logicop_lt(p):
    'logicop : expr LT expr'
    p[0]=p[1]
    pass

def p_logicop_gt(p):
    'logicop : expr GT expr'
    p[0]=p[1]
    pass

def p_logicop_le(p):
    'logicop : expr LE expr'
    p[0]=p[1]
    pass

def p_expr_ge(p):
    'logicop : expr GE expr'
    p[0]=p[1]
    pass

def p_expr_eq(p):
    'logicop : expr EQ expr'
    p[0]=p[1]
    pass

def p_expr_ne(p):
    'logicop : expr NE expr '
    p[0]=p[1]
    pass
    
def p_expr_or(p):
    'logicop : expr OR expr'
    p[0]=p[1]
    pass

def p_logicop_and(p):
    'logicop : expr AND expr'
    p[0]=p[1]
    pass

def p_logicop_not(p):
    'logicop : expr NOT expr'
    p[0]=p[1]
    pass

# ---------------callfunc ---------------------------

def p_callfunc_bltn(p):
    "callfunc : bltin LPARENT expr RPARENT"
    p[0]=p[1]
    pass

def p_callfunc_func(p):
    "callfunc : ID LPARENT expr RPARENT"
    p[0]=p[1]

# ------------------------------------------------------

def p_prlist_expr(p):
    "prlist : expr"
    p[0]=p[1]
    pass

def p_prlist_str(p):
    "prlist : STRING"
    p[0]=p[1]
    pass

def p_prlist_comma_expr(p):
    "prlist : prlist COMMA expr"
    p[0]=p[1]
    pass

def p_prlist_comma_str(p):
    "prlist : prlist COMMA STRING"
    p[0]=p[1]
    pass

# ---------------------------------------------------------

def p_defn_func(p):
    "defn : FUNC procname LPARENT formals RPARENT"
    p[0]=p[1]
    pass

def p_defn_proc(p):
    "defn : PROC procname LPARENT formals RPARENT"
    p[0]=p[1]
    pass

# -----------------------------------------------------------

def p_formals_var(p):
    "formals : ID"
    p[0]=p[1]
    pass

def p_formals_comma_var(p):
    "formals : ID COMMA formals"
    p[0]=p[1]
    pass

# ------------------------------------------------------------

def p_procname_function(p):
    "procname : FUNCTION"
    p[0]=p[1]
    pass

def p_procname_id(p):
    "procname : ID"
    p[0]=p[1]
    pass

def p_procname_proc(p):
    "procname : PROCEDURE"
    p[0]=p[1]
    pass

def p_procname_bltin(p):
    "procname : bltin"
    p[0]=p[1]
    pass

# ------------------------------------------------

def p_arglist_empty(p):
    "arglist : empty"
    p[0]=p[1]
    pass

def p_arglist_expr(p):
    "arglist : expr"
    p[0]=p[1]
    pass

def p_arglist_comma_expr(p):
    "arglist : arglist COMMA expr"
    p[0]=p[1]
    pass

# ----------------------------------------------------

def p_empty(p):
    "empty : "
    p[0]=""
    pass

# ---------------------------------------------------------

def p_error(p):
    'error : error'
    # p[0]=p[1]
    print p
    if p:
         print("Syntax error at token", p.type)
         parser.errok()
    else:
         print("Syntax error at EOF")

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
    pass


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
    p[0] = p[1]
    pass


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
    

)

# ----------------------------------------------


# Build the parser
parser = yacc.yacc()

# while True:
#     try:
#         s = raw_input('calc > ')
#         print "Resultado para: ", s
#     except EOFError:
#         break
#     print s 
#     if not s: continue
#     # result = parser.parse(s)
#     result = parser.parse(s)
#     print(result)

t = "5+4*7 \n"
print "RES", parser.parse(t)


 


# parser = yacc.yacc()

# if __name__ == '__main__':
#     # Build the lexer
#     import sys 
    
    
    
#     if len(sys.argv) > 1:
#         f = open(sys.argv[1],"r")
#         data = f.read()
#         f.close()
        
#     else:
#         data = ""
#         while 1:
#             try:
#                 data += raw_input() + "\n"
#             except:
#                 break
    
#     # lex.input(data)
#     lexer.input(data)
#     result = parser.parse(data,lexer=lexer)
#     print result
#     # # Tokenize
#     # while 1:
#     #         tok = lex.token()
#     #         if not tok: break            # No more input
#     #         print tok
    
      
    
    
    
# # parser = yacc.yacc(debug=debug)

# # with open('first.test') as f:
# #     data = f.read()
# #     lexer.input(data)
# #     parsed = parser.parse(data, lexer=lexer)
    
# #     i = Interpeter(parsed)
# #     i.interpet()

#     #for tok in lexer:
#         #print tok
    
    
    
    








