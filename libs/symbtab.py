#encoding:utf-8
from hocast import NodeVisitor
from utils import get_node_text
# from utils import get_node_text

class SymTab:



    def __init__(self, label, parent=None):
        self.name = label
        self.entries = {}
        self.parent = parent
        self.children = []
        self.errors = []
    
    def add(self, name, value): # agrego simbolo
        self.entries[name] = value

    def get(self, name): # o me retorna el simbolo no me retorna nada
        if self.entries.has_key(name):
            return self.entries[name]
        else:
            if self.parent != None:
                return self.parent.get(name)
            else:
                return None



class SymTabVisitor(NodeVisitor): # Se crea con el root del AST

    def __init__(self,node):
        self.id = 0
        self.current = SymTab('Program') 
        self.visit(node)
        

    def __str__(self):
        ans = """
        Para graficar el arbol se debe llamar al metodo graph(), Ej: 
        dot_visitor_obj = DotVisitor(root)
        dot_visitor_obj.graph()
        """
        return ans

    def get_symtab(self):
        return self.current

    #  ---------Definicion de visitores especificos 

    # Listas ---------------------------------

    def visit_ProgList(self,node):
        for node in node.proglist:
            # print node
            list_obj = self.visit(node)
            # if list_obj.__class__.__name__ == "FuncDef":
            #     self.current.children.append(list_obj)
            #     self.current.add(list_obj.name,node)
            # if list_obj.__class__.__name__ in ['StoreVar','Param']:
            #     self.current.add(list_obj,node)
        # return symtab

    def visit_StatementList(self,node):
        for node in node.statements:
            list_obj = self.visit(node)
            if list_obj.__class__.__name__ in ["FuncDef","BinaryOp"]:
                self.visit(node)

    def visit_FormalsList(self,node):
        for node in node.formallist:
            list_obj = self.visit(node)        
            # if list_obj.__class__.__name__ in ['Param']:
            #     self.current.add(list_obj,node)

    def visit_ArgList(self,node):
        for node in node.arglist:
            list_obj = self.visit(node)

    def visit_PrList(self,node):
        for obj in node.prlist:
            list_obj = self.visit(obj)
            


    # Varios ------------------------------------------------

    def visit_BinaryOp(self,node):
        if node.op in ["=",'+=','-=','*=','/=','%=','+','-','/','*']:
            self.visit(node.left)
            self.visit(node.right)

    def visit_FuncDef(self,node):
        function_name = node.function.value
        if function_name in self.current.entries.keys():
            error = "Error Semantico: No se puede definir dos funciones con el mismo nombre: "+function_name+""
            print error
            self.current.errors.append(error)

        self.current.add(function_name,node)
        # print "Function Name", node.function
        symbtab_func = SymTab(node.function.value,self.current)
        self.current.children.append(symbtab_func)
        self.current = symbtab_func

        self.visit(node.formals)
        self.visit(node.stmt)

        self.current= symbtab_func.parent

    def visit_Calls(self,node):
        has_function = False
        function_name = node.function.value
        if function_name in self.current.entries.keys():
            has_function = True
        p = self.current.parent
        while p:
            if function_name in self.current.parent.entries.keys():
                has_function = True
            p = p.parent 

        
        if not has_function:
            error = "Error Semantico: No se puede llamar a una funcion que no esta definida: "+function_name+""
            print error
            self.current.errors.append(error)
        else:
            call_function = node
            call_function_name = node.function.value
            def_function = self.current.get(call_function_name)

            if call_function.n_params != def_function.n_params:
                error = "Error Semantico: No se puede llamar a una funcion con un numero de parametros diferentes al definido: "+function_name+""
                print error
                self.current.errors.append(error)
                

        self.visit(node.function)
        self.visit(node.arglist)
        

    def visit_IfStatement(self,node):
        self.visit(node.cond)
        self.visit(node.then_stmt)
        else_stmt = node.else_stmt
        if else_stmt:
            self.visit(node.else_stmt)
    

    # uno ------------------------------------------------

    def visit_Statement(self,node):
        self.visit(node.statement)
        

    def visit_Expression(self,node):
        self.visit(node.expression)
        

    def visit_GroupParent(self,node): #obsoleto
        self.visit(node.expr)
        
    def visit_PrintValue(self,node): #obsoleto
        self.visit(node.value)

    # Hojas -----------------------------------------------

    def visit_Empty(self,node):
        pass

    def visit_Literal(self,node):
        # print "Value",node.value
        # label = node.value
        # node_id = self.node_id()
        # node_label = str(label)
        # node_text = get_node_text(node_id,node_label)
        
        # if label == '\n':
        #     label = 'NEWLINE'
        # self.dot.node(node_id, node_text)
        return None

    def visit_StoreVar(self,node):
        self.current.add(node.name,node)


    def visit_LoadVar(self,node):
        # print "LoadVar",node.name
        var = self.current.get(node.name)
        if not var:
            error = "Error Semantico: La variable  "+node.name+" no se encuentra definida"
            print error
            self.current.errors.append(error)
        # label = node.name
        # node_id = self.node_id()
        # node_label = "  LoadVar("+str(label)+")"
        # node_text = get_node_text(node_id,node_label)
        # self.dot.node(node_id, node_text)
        return None
        

    def visit_Param(self,node):        
        self.current.add(node.name,node)

    
