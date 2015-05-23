#encoding:utf-8
from graphviz import Digraph
import datetime
import random
from hocast import NodeVisitor
from utils import get_node_text

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
        node_label = "Program"
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)

        for node in node.proglist:
            if not (node.__class__.__name__ == "Empty"):
                list_obj = self.visit(node)
                self.dot.edge(node_id,list_obj)
        return node_id

    def visit_StatementList(self,node):
        node_id = self.node_id()
        node_label = "Statements"
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)
        for node in node.statements:
            if not (node.__class__.__name__ == "Empty"):
                list_obj = self.visit(node)

                self.dot.edge(node_id,list_obj)
        return node_id

    def visit_FormalsList(self,node):
        node_id = self.node_id()
        node_label = "Formals"
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)
        for node in node.formallist:
            if not (node.__class__.__name__ == "Empty"):
                list_obj = self.visit(node)
                self.dot.edge(node_id,list_obj)
        return node_id

    def visit_ArgList(self,node):
        node_id = self.node_id()
        node_label = "Args"
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)
        for node in node.arglist:
            if not (node.__class__.__name__ == "Empty"):
                list_obj = self.visit(node)
                self.dot.edge(node_id,list_obj)
        return node_id

    def visit_PrList(self,node):
        node_id = self.node_id()
        node_label = "Print"
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)
        for obj in node.prlist:
            if not (node.__class__.__name__ == "Empty"):
                list_obj = self.visit(obj)
                self.dot.edge(node_id,list_obj)
        return node_id


    # Varios ------------------------------------------------

    def visit_BinaryOp(self,node):
        node_id=self.node_id()
        node_label = str(node.op)
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)
        l=self.visit(node.left)
        r=self.visit(node.right)
        self.dot.edge(node_id,l)
        self.dot.edge(node_id,r)
        return node_id

    def visit_FuncDef(self,node):
        node_id=self.node_id()
        node_label = " Def "+str(node.n_params)
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)
        function_id = self.visit(node.function)
        formals_id = self.visit(node.formals)
        stmt_id = self.visit(node.stmt)
        self.dot.edge(node_id,function_id)
        self.dot.edge(node_id,formals_id)
        self.dot.edge(node_id,stmt_id)
        return node_id

    def visit_Calls(self,node):
        node_id=self.node_id()
        node_label = " Calls "+str(node.n_params)
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)
        function_id = self.visit(node.function)
        arglist_id = self.visit(node.arglist)
        
        self.dot.edge(node_id,function_id)
        self.dot.edge(node_id,arglist_id)        
        return node_id

    def visit_IfStatement(self,node):
        node_id=self.node_id()
        node_label = " If "
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)

        cond_id = self.visit(node.cond)
        then_stmt_id = self.visit(node.then_stmt)

        else_stmt = node.else_stmt

        if else_stmt:
            else_stmt_id = self.visit(node.else_stmt)
            self.dot.edge(node_id,else_stmt_id)
        
        self.dot.edge(node_id,cond_id)
        self.dot.edge(node_id,then_stmt_id)        
        return node_id


    def visit_ReturnValue(self,node):
        node_id=self.node_id()
        node_label = " Return "
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)

        value_id = self.visit(node.value)
        self.dot.edge(node_id,value_id)        
        return node_id

    # uno ------------------------------------------------

    def visit_Statement(self,node):
        node_id=self.node_id()
        node_label = "  stmt"
        node_text = get_node_text(node_id,node_label)
        stmt = self.visit(node.statement)
        self.dot.edge(node_id,stmt)
        self.dot.node(node_id, node_text)
        return node_id

    def visit_Expression(self,node):
        node_id=self.node_id()
        node_label = "  expr"
        node_text = get_node_text(node_id,node_label)
        expr = self.visit(node.expression)
        self.dot.edge(node_id,expr)
        self.dot.node(node_id, node_text)
        return node_id

    def visit_GroupParent(self,node): #obsoleto
        node_id=self.node_id()
        node_label =  " Group "
        node_text = get_node_text(node_id,node_label)
        expr = self.visit(node.expr)
        self.dot.edge(node_id,expr)
        self.dot.node(node_id, node_text)
        return node_id


    def visit_PrintValue(self,node): #obsoleto
        node_id=self.node_id()
        node_label = "  Print "
        node_text = get_node_text(node_id,node_label)
        value_id = self.visit(node.value)
        self.dot.edge(node_id,value_id)
        self.dot.node(node_id, node_text)
        return node_id        

    # Hojas -----------------------------------------------

    def visit_Empty(self,node):
        node_id = self.node_id()
        node_label =  "Empty"
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id,node_text)
        return node_id

    def visit_Literal(self,node):
        label = node.value
        node_id = self.node_id()
        node_label = str(label)
        node_text = get_node_text(node_id,node_label)
        
        if label == '\n':
            label = 'NEWLINE'
        self.dot.node(node_id, node_text)
        return node_id

    def visit_StoreVar(self,node):
        label = node.name
        node_id = self.node_id()
        node_label = "  StoreVar("+str(label)+")"
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)
        return node_id    

    def visit_LoadVar(self,node):
        label = node.name
        node_id = self.node_id()
        node_label = "  LoadVar("+str(label)+")"
        node_text = get_node_text(node_id,node_label)
        self.dot.node(node_id, node_text)
        return node_id    

    def visit_Param(self,node):
        label = node.name
        node_id = self.node_id()
        node_label = "  Param("+str(label)+")"
        node_text = get_node_text(node_id,node_label)
        
        self.dot.node(node_id, node_text)
        return node_id    

    def visit_SymTab(self,node):
        node_id = self.node_id()
        node_label = node.name
        node_text = get_node_text(node_id,node_label)
        node_text += "\n-------------\n"
        for p in node.entries.keys():
            node_text += p+"\n"
        # if len(node.errors)>0:
        #     print "===========Errores Semanticos==============="
        #     for error in node.errors:
        #         print error
        # print node_text

        self.dot.node(node_id, node_text)

        for child in node.children:
            child_id = self.visit(child)
            self.dot.edge(node_id,child_id)

        return node_id
