import libs.ply.yacc as yacc
from libs.ast_definitions import *
from libs.ast_graph import DotVisitor
from libs.utils import *
from libs.settings import *
from libs.symbtab import SymTabVisitor
import inspect

from lexer import *


# --------------list ----------------------------------

def p_list_empty(p):
    "list : empty"
    p[0]=ProgList([p[1]])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_list_nl(p):
    " list : list  newline "
    p[0]= p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    
    cont = cont + 1
        

def p_list_defn(p):
    "list : list defn newline"
    p[1].append(p[2])
    p[0]= p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_list_asgn(p):
    " list : list asgn newline "
    p[1].append(p[2])
    p[0]= p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    
def p_list_stmt(p):
    "list : list stmt newline "
    p[1].append(p[2])
    p[0]= p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    
    
def p_list_expr(p):
    "list : list expr newline"
    p[1].append(p[2])
    p[0]= p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_list_error(p):
    "list : list error newline"
    p[1].append(p[2])
    p[0]= p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_list_comment(p):
    "list : list COMMENT newline"
    p[1].append(p[2])
    p[0]= p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        



# --------------------------asgn--------------------------

def p_asgn_equal(p):
    "asgn : VAR ASSIGN expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_asgn_addeq(p):
    "asgn : VAR ADDEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_asgn_subeq(p):
    "asgn : VAR SUBEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_asgn_muleq(p):
    "asgn : VAR MULEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_asgn_diveq(p):
    "asgn : VAR DIVEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_asgn_modeq(p):
    "asgn : VAR MODEQ expr "
    p[0] = BinaryOp(p[2], StoreVar(p[1]), p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    

# ------------------------stmt------------------------------

def p_stmt_expr(p):
    "stmt : expr"
    # p[0] = Statement(p[1])
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    

        

def p_stmt_return_expr(p):
    "stmt : RETURN  expr "
    p[0]=ReturnValue(p[2])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1


def p_stmt_return(p):
    "stmt : RETURN"
    p[0] = Literal(p[1])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_stmt_print(p):
    "stmt : PRINT prlist"
    p[0]=p[2]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_stmt_while(p):
    "stmt : WHILE  LPARENT cond RPARENT stmt end"
    p[0]=Statement(p[1]) # Pendiente
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_stmt_for(p):
    "stmt : FOR LPARENT cond SEMICOLON cond SEMICOLON cond RPARENT stmt end"
    p[0]=Statement(p[1]) # Pendiente
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_stmt_if(p):
    "stmt : IF LPARENT cond RPARENT stmt end"
    p[0]=IfStatement(p[3],p[5],None)
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_stmt_if_else(p):
    "stmt : IF LPARENT cond RPARENT stmt  ELSE stmt end"
    p[0]=IfStatement(p[3],p[5],p[7])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_stmt_braket(p):
    "stmt : LBRACKET stmtlist RBRACKET "
    p[0]=p[2]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        
# ------------------end--------------begin----------

def p_end(p):
    "end : "
    p[0] = Empty()

def p_begin(p):
    "begin : "
    p[0] = Empty()

# ---------------------cond--------------------------------

def p_cond_expr(p):
    "cond : expr "
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    
# --------------------------stmtlist---------------------------

def p_stmtlist_empty(p):
    "stmtlist : empty "
    p[0]=StatementList([Empty()])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_stmlist_newline(p):
    "stmtlist : stmtlist newline"
    # p[1].append(p[2])
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    
def p_stmtlist_stmt(p):
    "stmtlist : stmtlist stmt "
    p[1].append(p[2])
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    
# ---------------expr-----------------------------------------

def p_expr_data(p):
    "expr : data"
    p[0] = p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    
def p_expr_asgn(p):
    "expr : asgn"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_expr_unaryop(p):
    "expr : unaryop"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_expr_binaryop(p):
    "expr : binaryop"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_expr_group(p):
    "expr : LPARENT expr RPARENT"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_data_callfunc(p):
    "expr : callfunc"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        
# ---------------data----------------------------------------

def p_data_float(p):
    "data : FLOAT"
    p[0]=Literal(p[1])

    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    

def p_data_constant(p):
    "data : CONSTANT"
    p[0]=Literal(p[1])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_data_VAR(p):
    "data : VAR "
    p[0]=LoadVar(p[1])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    


#  -------------unaryop---------------------------------------------


def p_unaryop_munit(p):
    "unaryop : UNARYMINUS expr "
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    


def p_unaryop_inc(p):
    "unaryop : INC VAR"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_unaryop_dec(p):
    "unaryop : DEC VAR"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_unaryop_inc2(p):
    "unaryop : VAR INC"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_unaryop_dec2(p):
    "unaryop : VAR DEC"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    
def p_not_expr(p):
    "unaryop : NOT  expr"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

# ----------------binaryop--------------------------------------------------


def p_binaryop_mathop(p):
    "binaryop : mathop"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_binaryop_logicop(p):
    "binaryop : logicop"
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    



# -----------------mathop------------------------------------


def p_mathop_exp(p):
    'mathop : expr EXP expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1

    
def p_mathop_plus(p):
    'mathop : expr PLUS expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_mathop_minus(p):
    'mathop : expr MINUS expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        
    
def p_mathop_times(p):
    "mathop : expr TIMES expr"
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_mathop_divide(p):
    "mathop : expr DIVIDE expr"
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_mathop_mod(p):
    "mathop : expr MOD expr"
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

# ----------------------logicop --------------

def p_logicop_lt(p):
    'logicop : expr LT expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_logicop_gt(p):
    'logicop : expr GT expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_logicop_le(p):
    'logicop : expr LE expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_logicop_ge(p):
    'logicop : expr GE expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_logicop_eq(p):
    'logicop : expr EQ expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_logicop_ne(p):
    'logicop : expr NE expr '
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        
    
def p_logicop_or(p):
    'logicop : expr OR expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_logicop_and(p):
    'logicop : expr AND expr'
    p[0] = BinaryOp(p[2], p[1], p[3])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        
    

# ---------------callfunc ---------------------------

def p_callfunc_bltn(p):
    "callfunc : BLTIN  begin LPARENT expr RPARENT"
    p[0]=Calls(Literal(p[1]),p[4],1)
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_callfunc_call(p):
    "callfunc : VAR begin LPARENT arglist RPARENT"
    p[0]=Calls(Literal(p[1]),p[4], len(p[4].arglist))
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1

# def p_callfunc_proc(p):
#     "callfunc : procedure begin LPARENT arglist RPARENT"
#     p[0]=Calls(p[2],p[3])
    
#     global cont
#     function_name = inspect.stack()[0][3]
#     print_state(p,cont,function_name)
#     cont = cont + 1
    

# ------------------------------------------------------

def p_prlist_expr(p):
    "prlist : expr"
    p[0]=PrList([p[1]])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_prlist_str(p):
    "prlist : STRING"
    p[0]=PrList([Literal(p[1])])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_prlist_comma_expr(p):
    "prlist : prlist COMMA expr"
    p[1].append(p[3])
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_prlist_comma_str(p):
    "prlist : prlist COMMA STRING"
    p[1].append(Literal(p[3]))
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

# -----------------------def func----------------------------------

def p_defn_func(p):
    "defn : FUNC procname LPARENT formals RPARENT stmt"
    p[0]=FuncDef(Literal(p[2]),p[4],p[6],len(p[4].formallist))
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1


def p_defn_proc(p):
    "defn : PROC procname LPARENT formals RPARENT stmt"
    p[0]=FuncDef(Literal(p[2]),p[4],p[6],len(p[4].formallist))
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1

# -----------------------------------------------------------


def p_procname(p):
    "procname : VAR "
    p[0]=p[1]


# def p_procedure(p):
#     "procedure : VAR"
#     p[0] = p[1]

# def p_function(p):
#     "function : VAR"
#     p[0] = p[1]


# ------------------------formals-----------------------------------

def p_formals_empty(p):
    "formals : empty"
    p[0]=FormalsList([Empty()])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
    
def p_formals_VAR(p):
    "formals : VAR"
    p[0]=FormalsList([Param(p[1])]) #modificar
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_formals_comma_VAR(p):
    "formals : formals COMMA VAR"
    p[1].append(Param(p[3]))
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

# --------------------arglist----------------------------

def p_arglist_empty(p):
    "arglist : empty"
    p[0]=ArgList([Empty()])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_arglist_expr(p):
    "arglist : expr"
    p[0]=ArgList([p[1]])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

def p_arglist_comma_expr(p):
    "arglist : arglist COMMA expr"
    p[1].append(p[3])
    p[0]=p[1]
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        

# ----------------------------------------------------

def p_empty(p):
    "empty : "
    p[0]=Empty()
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1
        
def p_newline(p):
    "newline : NEWLINE"
    p[0]=Literal(p[1])
    
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1

        
# ----------------------------Error-----------------------------

def p_error(p):
    'error : error'
    global cont
    function_name = inspect.stack()[0][3]
    print_state(p,cont,function_name)
    cont = cont + 1

    if p:
         print("Syntax error at token", p.type)
         parser.errok()
    else:
         print("Syntax error at EOF")


# --------------------------precedence------------------------------------

precedence = (
    ('right', 'ASSIGN', 'ADDEQ', 'SUBEQ', 'MULEQ', 'DIVEQ', 'MODEQ'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'GT','GE','LT','LE','EQ','NE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE','MOD'),
    ('right', 'UNARYMINUS','NOT','INC','DEC'),
    ('left', 'EXP'),
    ('left', 'NEWLINE'),
    ('left','VAR'),
    ('left','CONSTANT'),
    ('left', 'BLTIN'),
    ('left','FLOAT'),
    # ('right','LPARENT'),

)

# ---------------------------parser----------------------------

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
    
    print "\n+++++++++++++++++   AST Generado   ++++++++++++++++++++++\n\n"
    root = yacc.parse(data+ "\n")

    if PRINT_AST:
        print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
        print root.pprint()
        print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

    if GRAPH_AST:
        dot_visitor_obj = DotVisitor(root)
        dot_visitor_obj.graph()

    symtab_visitor_root=SymTabVisitor(root)
    if GRAPH_SYMTAB:
        dot_visitor_obj = DotVisitor(symtab_visitor_root.get_symtab())
        dot_visitor_obj.graph()


    
