#encoding:utf-8
from graphviz import Digraph
import datetime
import random
from hocast import NodeVisitor

# ----------------------------------------------------------------------
# Graficador de AST
# 
# El siguiente codigo describe una clase que puede recorrer
# un arbol de sintaxis y crear un grafico con la libreria Digraph,
# los graficos se generan en dos formatos .gv que es la notacion estandar 
# para Graficos de nodos y .gv.pdf que dibuja el arbol en un documento pdf
# 
# ----------------------------------------------------------------------

class DotVisitor(NodeVisitor):
    """
    Para utilizar el graficador, se debe crear un objeto DotVisitor pasandole 
    como parametro la raiz del arbol de sintaxis y posteriormente 
    utilizar su metodo Graph 

    Ej: 

    dot_visitor_obj = DotVisitor()
    dot_visitor_obj.graph()

    """

    def __init__(self,node):
        self.dot = Digraph(comment='Compilador')
        self.id=0
        self.visit(node)

    def __str__(self):
        ans = """
        Para graficar el arbol se debe llamar al metodo graph(), Ej: 
        dot_visitor_obj = DotVisitor(root)
        dot_visitor_obj.graph()
        """
        return ans

    def graph(self):
        filename = 'AST_output/ast'+str(int(10000*random.random()))+'.gv'
        self.dot.render(filename, view=True)

    def node_id(self):
        self.id +=1
        return "n%d" % self.id 

    #  ---------Definicion de visitores especificos 

    # Listas ---------------------------------

    def visit_ProgList(self,node):
        node_id = self.node_id()
        self.dot.node(node_id, str(node_id)+"  "+"ProgList")
        for pl in node.proglist:
            list_obj = self.visit(pl)
            self.dot.edge(node_id,list_obj)
        return node_id

    def visit_StatementList(self,node):
        node_id = self.node_id()
        self.dot.node(node_id, str(node_id)+"  "+"StatementList")
        for st in node.statements:
            list_obj = self.visit(st)
            self.dot.edge(node_id,list_obj)
        return node_id

    def visit_FormalsList(self,node):
        node_id = self.node_id()
        self.dot.node(node_id, str(node_id)+"  "+"FormalsList")
        for obj in node.formallist:
            list_obj = self.visit(obj)
            self.dot.edge(node_id,list_obj)
        return node_id

    def visit_ArgList(self,node):
        node_id = self.node_id()
        self.dot.node(node_id, str(node_id)+"  "+"ArgList")
        for obj in node.arglist:
            list_obj = self.visit(obj)
            self.dot.edge(node_id,list_obj)
        return node_id


    # Varios ------------------------------------------------

    def visit_BinaryOp(self,node):
        node_id=self.node_id()
        self.dot.node(node_id, str(node_id)+"  "+str(node.op))
        l=self.visit(node.left)
        r=self.visit(node.right)
        self.dot.edge(node_id,l)
        self.dot.edge(node_id,r)
        return node_id

    def visit_FuncDef(self,node):
        node_id=self.node_id()
        self.dot.node(node_id, str(node_id)+"  (FuncDef)")
        function_id = self.visit(node.function)
        formals_id = self.visit(node.formals)
        stmt_id = self.visit(node.stmt)
        self.dot.edge(node_id,function_id)
        self.dot.edge(node_id,formals_id)
        self.dot.edge(node_id,stmt_id)
        return node_id

    def visit_Calls(self,node):
        node_id=self.node_id()
        self.dot.node(node_id, str(node_id)+" (Calls)")
        function_id = self.visit(node.function)
        arglist_id = self.visit(node.arglist)
        
        self.dot.edge(node_id,function_id)
        self.dot.edge(node_id,arglist_id)
        
        return node_id

    # uno ------------------------------------------------

    def visit_Statement(self,node):
        node_id=self.node_id()
        stmt = self.visit(node.statement)
        self.dot.edge(node_id,stmt)
        self.dot.node(node_id, str(node_id)+"  stmt")
        return node_id

    def visit_Expression(self,node):
        node_id=self.node_id()
        expr = self.visit(node.expression)
        self.dot.edge(node_id,expr)
        self.dot.node(node_id, str(node_id)+"  expr")
        return node_id

    def visit_GroupParent(self,node):
        node_id=self.node_id()
        expr = self.visit(node.expr)
        self.dot.edge(node_id,expr)
        self.dot.node(node_id, str(node_id)+"  (GroupParent)")
        return node_id

    # Hojas -----------------------------------------------

    def visit_Empty(self,node):
        node_id = self.node_id()
        self.dot.node(node_id, str(node_id)+"  "+"Empty")
        return node_id

    def visit_Literal(self,node):
        node_id = self.node_id()
        label = node.value
        if label == '\n':
            label = 'NEWLINE'
        self.dot.node(node_id, str(node_id)+"  "+str(label))
        return node_id

    def visit_StoreVar(self,node):
        node_id = self.node_id()
        label = node.name
        self.dot.node(node_id, str(node_id)+"  StoreVar("+str(label)+")")
        return node_id    

    def visit_LoadVar(self,node):
        node_id = self.node_id()
        label = node.name
        self.dot.node(node_id, str(node_id)+"  LoadVar("+str(label)+")")
        return node_id    
