import libs.ply.yacc as yacc
from lexer import *

def p_program(p):
    "program : list"

# -------------------------------------------------------

def p_list_empty(p):
    "list : empty"
    pass

def p_list_nl(p):
    " list : list NEWLINE "
    pass

def p_list_defn(p):
    "list : list defn NEWLINE"
    pass

def p_list_asgn(p):
    " list : list asgn NEWLINE "
    pass

def p_list_stmt(p):
    "list : list stmt NEWLINE"
    pass

def p_list_expr(p):
    "list : list expr NEWLINE"
    pass

def p_list_error(p):
    "list : list error NEWLINE"
    pass

def p_list_comment(p):
    "list : list COMMENT NEWLINE"
    pass



# ----------------------------------------------------


# ------------------------------------------------------

def p_stmt_expr(p):
    "stmt : expr"
    pass

def p_stmt_return(p):
    "stmt : RETURN"
    pass

def p_stmt_return_expr(p):
    "stmt : RETURN expr "
    pass

def p_stmt_proc(p):
    "stmt : PROCEDURE BEGIN LPARENT arglist RPARENT"
    pass

def p_stmt_print(p):
    "stmt : PRINT prlist"
    pass

def p_stmt_while(p):
    "stmt : WHILE  LPARENT cond RPARENT stmt END "
    pass

def p_stmt_for(p):
    "stmt : FOR LPARENT cond SEMICOLON cond SEMICOLON cond RPARENT stmt END"
    pass

def p_stmt_if(p):
    "stmt : IF LPARENT cond RPARENT stmt END"
    pass

def p_stmt_if_else(p):
    "stmt : IF LPARENT cond RPARENT stmt END ELSE stmt END"
    pass

def p_stmt_braket(p):
    "stmt : LBRACKET stmtlist RBRACKET "
    pass

# -----------------------------------------------------

def p_cond_expr(p):
    "cond : expr "
    pass

# -----------------------------------------------------

def p_stmtlist_empty(p):
    "stmtlist : empty "
    pass

def p_stmlist_newline(p):
    "stmtlist : stmtlist NEWLINE"
    pass

def p_stmtlist_stmt(p):
    "stmtlist : stmtlist stmt "
    pass

# ---------------expr-----------------------------------------

def p_expr_data(p):
    "expr : data"
    pass

def p_expr_unaryop(p):
    "expr : unaryop"
    pass

def p_expr_binaryop(p):
    "expr : binaryop"
    pass

def p_expr_group(p):
    "expr : LPARENT expr RPARENT"
    pass

def p_data_callfunc(p):
    "expr : callfunc"
    pass
# ---------------data----------------------------------------

def p_data_float(p):
    "data : FLOAT"
    pass

def p_data_constant(p):
    "data : CONSTANT"
    pass

def p_data_id(p):
    "data : ID "
    pass

#  -------------unaryop---------------------------------------------


def p_unaryop_munit(p):
    "unaryop : MINUS expr "
    pass

def p_unaryop_inc(p):
    "unaryop : INC ID"
    pass

def p_unaryop_dec(p):
    "unaryop : DEC ID"
    pass

def p_unaryop_inc2(p):
    "unaryop : ID INC"
    pass

def p_unaryop_dec2(p):
    "unaryop : ID DEC"
    pass

# ----------------binaryop--------------------------------------------------

def p_binaryop_asgn(p):
    "binaryop : asgn"
    pass

def p_binaryop_mathop(p):
    "binaryop : mathop"
    pass

def p_binaryop_logicop(p):
    "binaryop : logicop"


# -----------------asgn---------------------------------------------------

def p_asgn_equal(p):
    "asgn : ID ASSIGN expr "
    pass

def p_asgn_addeq(p):
    "asgn : ID ADDEQ expr "
    pass

def p_asgn_subeq(p):
    "asgn : ID SUBEQ expr "
    pass

def p_asgn_muleq(p):
    "asgn : ID MULEQ expr "
    pass

def p_asgn_diveq(p):
    "asgn : ID DIVEQ expr "
    pass

def p_asgn_modeq(p):
    "asgn : ID MODEQ expr "
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

def p_mathop_plus(p):
    'mathop : expr PLUS expr'
    pass

def p_mathop_minus(p):
    'mathop : expr MINUS expr'
    pass
    
def p_mathop_times(p):
    "mathop : expr TIMES expr"
    pass

def p_mathop_divide(p):
    "mathop : expr DIVIDE expr"
    pass

def p_mathop_mod(p):
    "mathop : expr MOD expr"
    pass

# ----------------logicop --------------

def p_logicop_lt(p):
    'logicop : expr LT expr'
    pass

def p_logicop_gt(p):
    'logicop : expr GT expr'
    pass

def p_logicop_le(p):
    'logicop : expr LE expr'
    pass

def p_expr_ge(p):
    'logicop : expr GE expr'
    pass

def p_expr_eq(p):
    'logicop : expr EQ expr'
    pass

def p_expr_ne(p):
    'logicop : expr NE expr'
    pass
    
def p_expr_or(p):
    'logicop : expr OR expr'
    pass

def p_logicop_and(p):
    'logicop : expr AND expr'
    pass

def p_logicop_not(p):
    'logicop : expr NOT expr'
    pass

# ---------------callfunc ---------------------------

def p_callfunc_bltn(p):
    "callfunc : BLTIN LPARENT expr RPARENT"
    pass

def p_callfunc_func(p):
    "callfunc : ID LPARENT expr RPARENT"

# ------------------------------------------------------

def p_prlist_expr(p):
    "prlist : expr"
    pass

def p_prlist_str(p):
    "prlist : STRING"
    pass

def p_prlist_comma_expr(p):
    "prlist : prlist COMMA expr"
    pass

def p_prlist_comma_str(p):
    "prlist : prlist COMMA STRING"
    pass

# ---------------------------------------------------------

def p_defn_func(p):
    "defn : FUNC procname LPARENT formals RPARENT"
    pass

def p_defn_proc(p):
    "defn : PROC procname LPARENT formals RPARENT"
    pass

# -----------------------------------------------------------

def p_formals_var(p):
    "formals : ID"
    pass

def p_formals_comma_var(p):
    "formals : ID COMMA formals"
    pass

# ------------------------------------------------------------

def p_procname_function(p):
    "procname : FUNCTION"
    pass

def p_procname_id(p):
    "procname : ID"
    pass

def p_procname_proc(p):
    "procname : PROCEDURE"
    pass

def p_procname_bltin(p):
    "procname : BLTIN"
    pass

# ------------------------------------------------

def p_arglist_empty(p):
    "arglist : empty"
    pass

def p_arglist_expr(p):
    "arglist : expr"
    pass

def p_arglist_comma_expr(p):
    "arglist : arglist COMMA expr"
    pass

# ----------------------------------------------------

def p_empty(p):
    "empty : "
    pass

# ---------------------------------------------------------

def p_error(p):
    if p:
         print("Syntax error at token", p.type)
         parser.errok()
    else:
         print("Syntax error at EOF")

# -------------------------------------------------------

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)


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
    
    
    
    








