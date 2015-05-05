import libs.ply.yacc as yacc
from lexer import *

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

# ----------------------------------------------------

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

# ------------------------------------------------------

def p_stmt_expr(p):
    "stmt : expr"
    pass

def p_stmt_return(p):
    "stmt : RETURN"
    pass

def p_stmt_return_expr(p):
    "stmt : RETURN expr"
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

# --------------------------------------------------------

def p_expr_number(p):
    "expr : NUMBER"
    pass

def p_expr_id(p):
    "expr : ID "
    pass

def p_expr_asgn(p):
    "expr : asgn"
    pass

def p_expr_function(p):
    "expr : FUNCTION BEGIN"
    pass

def p_expr_read(p):
    "expr : LPARENT ID RPARENT"
    pass

def p_expr_bltin(p):
    "expr : ID LPARENT expr RPARENT"
    pass

def p_expr_parent(p):
    "expr : LPARENT expr RPARENT"
    pass

def p_expr_plus(p):
    'expr : expr PLUS expr'
    pass

def p_expr_minus(p):
    'expr : expr MINUS expr'
    pass
    
def p_expr_times(p):
    "expr : expr TIMES expr"
    pass

def p_expr_divide(p):
    "expr : expr DIVIDE expr"
    pass

def p_expr_mod(p):
    "expr : expr MOD expr"
    pass

def p_expr_munit(p):
    "expr : MINUS expr "
    pass

def p_expr_lt(p):
    'expr : expr LT expr'
    pass

def p_expr_gt(p):
    'expr : expr GT expr'
    pass

def p_expr_le(p):
    'expr : expr LE expr'
    pass

def p_expr_ge(p):
    'expr : expr GE expr'
    pass

def p_expr_eq(p):
    'expr : expr EQ expr'
    pass

def p_expr_ne(p):
    'expr : expr NE expr'
    pass
    
def p_expr_or(p):
    'expr : expr OR expr'
    pass

def p_expr_and(p):
    'expr : expr AND expr'
    pass

def p_expr_not(p):
    'expr : expr NOT expr'
    pass

def p_expr_inc(p):
    "expr : INC ID"
    pass

def p_expr_dec(p):
    "expr : DEC ID"
    pass

def p_expr_inc2(p):
    "expr : ID INC"
    pass

def p_expr_dec2(p):
    "expr : ID DEC"
    pass

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
    print "Syntax error in input!"
    # return "ERROR"

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









