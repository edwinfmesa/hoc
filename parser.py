import libs.ply.yacc as yacc
from lexer import *

# -------------------------------------------------------

def p_list_empty(p):
    "list : "

def p_list_nl(p):
    " list : list \n "

def p_list_defn(p):
    "list : list defn \n"

def p_list_asgn(p):
    " list : list asgn \n "

def p_list_stmt(p):
    "list : list stmt \n"

def p_list_expr(p):
    "list : list expr \n"

def p_list_error(p):
    "list : list error \n"

# ----------------------------------------------------

def p_asgn_equal(p):
    "asgn : ID ASSIGN expr "

def p_asgn_addeq(p):
    "asgn : ID ADDEQ expr "

def p_asgn_subeq(p):
    "asgn : ID SUBEQ expr "

def p_asgn_muleq(p):
    "asgn : ID MULEQ expr "

def p_asgn_diveq(p):
    "asgn : ID DIVEQ expr "

def p_asgn_modeq(p):
    "asgn : ID MODEQ expr "

# ------------------------------------------------------

def p_stmt_expr(p):
    "stmt : expr"

def p_stmt_return(p):
    "stmt : RETURN"

def p_stmt_return_expr(p):
    "stmt : RETURN expr"

def p_stmt_print(p):
    "stmt : PRINT prlist"

def p_stmt_while(p):
    "stmt : WHILE  LPARENT cond RPARENT stmt END "

def p_stmt_for(p):
    "stmt : FOR LPARENT cond SEMICOLON cond SEMICOLON cond RPARENT stmt END"

def p_stmt_if(p):
    "stmt : IF LPARENT cond RPARENT stmt END"

def p_stmt_if_else(p):
    "stmt : IF LPARENT cond RPARENT stmt END ELSE stmt END"

def p_stmt_braket(p):
    "stmt : LBRACKET stmtlist RBRACKET "

# -----------------------------------------------------

def p_cond_expr(p):
    "cond : expr "

# -----------------------------------------------------

def p_stmtlist_empty(p):
    "stmtlist : "

def p_stmlist_newline(p):
    "stmtlist : stmtlist \n"

def p_stmtlist_stmt(p):
    "stmtlist : stmtlist stmt "

# --------------------------------------------------------

def p_expr_number(p):
    "expr : NUMBER"

def p_expr_id(p):
    "expr : ID "

def p_expr_asgn(p):
    "expr : asgn"

def p_expr_function(p):
    "expr : FUNCTION BEGIN"

def p_expr_read(p):
    "expr : LPARENT ID RPARENT"

def p_expr_bltin(p):
    "expr : ID LPARENT expr RPARENT"

def p_expr_parent(p):
    "expr : LPARENT expr RPARENT"

def p_expr_plus(p):
    'expr : expr PLUS expr'

def p_expr_minus(p):
    'expr : expr MINUS expr'
    
def p_expr_times(p):
    "expr : expr TIMES expr"

def p_expr_divide(p):
    "expr : expr DIVIDE expr"

def p_expr_mod(p):
    "expr : expr MOD expr"

def p_expr_munit(p):
    "expr : MINUS expr "

def p_expr_lt(p):
    'expr : expr LT expr'

def p_expr_gt(p):
    'expr : expr GT expr'

def p_expr_le(p):
    'expr : expr LE expr'

def p_expr_ge(p):
    'expr : expr GE expr'

def p_expr_eq(p):
    'expr : expr EQ expr'

def p_expr_ne(p):
    'expr : expr NE expr'
    
def p_expr_or(p):
    'expr : expr OR expr'

def p_expr_and(p):
    'expr : expr AND expr'

def p_expr_not(p):
    'expr : expr NOT expr'

def p_expr_inc(p):
    "expr : INC ID"

def p_expr_dec(p):
    "expr : DEC ID"

def p_expr_inc2(p):
    "expr : ID INC"

def p_expr_dec2(p):
    "expr : ID DEC"

# ------------------------------------------------------

def p_prlist_expr(p):
    "prlist : expr"

def p_prlist_str(p):
    "prlist : STRING"

def p_prlist_comma_expr(p):
    "prlist : prlist COMMA expr"

def p_prlist_comma_str(p):
    "prlist : prlist COMMA STRING"

# ---------------------------------------------------------

def p_defn_func(p):
    "defn : FUNC procname"

def p_defn_proc(p):
    "defn : PROC procname"

# -----------------------------------------------------------

def p_formals_var(p):
    "formals : ID"

def p_formals_comma_var(p):
    "formals : ID COMMA formals"

# ------------------------------------------------------------

def p_procname_function(p):
    "procname : FUNCTION"

def p_procname_id(p):
    "procname : ID"

def p_procname_proc(p):
    "procname : PROCEDURE"

# ------------------------------------------------

def p_arglist_empty(p):
    "arglist : "

def p_arglist_expr(p):
    "arglist : expr"

def p_arglist_comma_expr(p):
    "arglist : arglist COMMA expr"

# ---------------------------------------------------------

def p_error(p):
    print "Syntax error in input!"

# -------------------------------------------------------

parser = yacc.yacc()

while True:
   try:
       s = raw_input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print result









