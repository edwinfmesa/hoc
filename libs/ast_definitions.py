#encoding:utf-8
from hocast import AST
from hocast import validate_fields

# ----------------------------------------------------------------------
# Nodos AST especificos
#
# En este archivo se definen los nodos especificos del AST, cada uno 
# tiene definido un campo _fields que contiene la lista de atributos
# que tendra el nodo al momento de declararse un objeto de esta clase.
# 
# ----------------------------------------------------------------------


# Listas -----------------------------------------------

@validate_fields(statements=list)
class StatementList(AST):
    _fields = ['statements']

    def append(self,e):
        self.statements.append(e)


@validate_fields(proglist=list)
class ProgList(AST):
    _fields = ['proglist']

    def append(self,e):
        self.proglist.append(e)

@validate_fields(arglist=list)
class ArgList(AST):
    _fields = ['arglist']    

    def append(self, e):
        self.arglist.append(e)

@validate_fields(formallist=list)
class FormalsList(AST):
    _fields = ['formallist']    

    def append(self, e):
        self.formallist.append(e)


@validate_fields(prlist=list)
class PrList(AST):
    _fields = ['prlist']

    def append(self, e):
        self.prlist.append(e)


# Tres campos --------------------------------------------

class FuncDef(AST):
    _fields = ['function','formals','stmt','n_params']

class IfStatement(AST):
    _fields = ['cond', 'then_stmt', 'else_stmt']

class BinaryOp(AST):
    _fields = ['op', 'left', 'right']

class GroupParent(AST):
    _fields = ['lp','expr','rp']


# Dos campos ----------------------------------------------

class ReturnValue(AST):
    _fields = ['value']

class PrintValue(AST):
    _fields = ['value']

class WhileStatement(AST):
    _fields = ['condition', 'body']

class UnaryOp(AST):
    _fields = ['op', 'left']

# class FunCall(AST):
#     _fields = ['id', 'params']

class Calls(AST):
    _fields = ['function','arglist','n_params']


# Un campo ------------------------------

class Statement(AST):
    _fields = ['statement']

class StoreVar(AST):
    _fields = ['name']

class Group(AST):
    _fields = ['expression']

class Expression(AST):
    _fields = ['expression']

class LoadVar(AST):
    _fields = ['name']    

class Param(AST):
    _fields = ['name']   

class Literal(AST):
    _fields = ['value']

class Program(AST):
    _fields = ['program']


# Sin campos ------------------------------

class Empty(AST):
    _fields = []

