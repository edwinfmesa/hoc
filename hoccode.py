from libs.hocast import *
import libs.ply.yacc as yacc
from collections import defaultdict
import pprint 

binary_ops = {
    '+':'add',
    '-':'sub',
    '*':'mul',
    '/':'div',
}



unary_ops = {
    '+' : 'uadd',
    '-' : 'usub',
}


class GenerateCode(NodeVisitor):
  
    def __init__(self):
        super(GenerateCode, self).__init__()

        self.versions = defaultdict(int)

        self.code = []
        self.start_block = self.code

        self.externs = []

    def new_temp(self):
        name = "%s_%d" % ("float", self.versions['float'])
        self.versions['float'] += 1
        return name


    def visit_Literal(self,node):
        target = self.new_temp()

        inst = ('literal_float', node.value, target)
        self.code.append(inst)

        node.gen_location = target

    def visit_BinaryOp(self,node):
        self.visit(node.left)
        self.visit(node.right)

        target = self.new_temp()

        opcode = binary_ops[node.op] + "_float"
        inst = (opcode, node.left.gen_location, node.right.gen_location, target)
        self.code.append(inst)

        # Almacena localizacion del resultado en el nodo
        node.gen_location = target

    def visit_StoreVar(self,node):
    	target = self.new_temp()
    	node.gen_location = target

    # def visit_PrintStatement(self,node):
    #     # Visit la expresion print
    #     self.visit(node.expr)

    #     # Cree el opcode y agregarlo a la lista
    #     inst = ('print_'+node.expr.type.name, node.expr.gen_location)
    #     self.code.append(inst)

  

    # def visit_ConstDeclaration(self,node):
    #     # localice en memoria
    #     inst = ('alloc_'+node.type.name, 
    #             node.id)
    #     self.code.append(inst)
    #     # almacene valor inicial
    #     self.visit(node.value)
    #     inst = ('store_'+node.type.name,
    #             node.value.gen_location,
    #             node.id)
    #     self.code.append(inst)

    # def visit_VarDeclaration(self,node):
    #     # localice en memoria
    #     inst = ('alloc_'+node.type.name, 
    #             node.id)
    #     self.code.append(inst)
    #     # almacene pot. val inicial
    #     if node.value:
    #         self.visit(node.value)
    #         inst = ('store_'+node.type.name,
    #                 node.value.gen_location,
    #                 node.id)
    #         self.code.append(inst)

    # def visit_LoadLocation(self,node):
    #     target = self.new_temp(node.type)
    #     inst = ('load_'+node.type.name,
    #             node.name,
    #             target)
    #     self.code.append(inst)
    #     node.gen_location = target

   
    # def visit_UnaryOp(self,node):
    #     self.visit(node.left)
    #     target = self.new_temp(node.type)
    #     opcode = unary_ops[node.op] + "_" + node.left.type.name
    #     inst = (opcode, node.left.gen_location)
    #     self.code.append(inst)
    #     node.gen_location = target

   
def generate_code(node):
    '''
    Genera codigo SSA desde el nodo AST entregado.
    '''
    gen = GenerateCode()
    gen.visit(node)
    return gen

if __name__ == '__main__':
    from hocparser import make_parser
    import sys 
    

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
    
    print "\n+++++++++++++++++   Generar AST   ++++++++++++++++++++++\n\n"
    root = make_parser(data)

    
    print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    print root.pprint()
    print "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

    code = generate_code(root)

    # print 'CODE_OBJ \n', code 
    print '\n CODE \n'
    pprint.pprint(code.code )
    