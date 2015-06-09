from libs.hocast import *
import libs.ply.yacc as yacc
from collections import defaultdict
import pprint 


# Definicion de diccionarios
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

# Clase principal que hereda de NodeVisitor
class GenerateCode(NodeVisitor):
  
    def __init__(self):
        super(GenerateCode, self).__init__()
        self.versions = defaultdict(int) 
        self.code = []
        self.start_block = self.code
        self.externs = []

    # crea variables temporales
    def new_temp(self):
        name = "%s_%d" % ("float", self.versions['float'])
        self.versions['float'] += 1
        return name

    # Visitantes para cada una de las definiciones de hoc

    def visit_Literal(self,node):
        target = self.new_temp()
        inst = ('literal_float', node.value, target)
        self.code.append(inst)
        node.gen_location = target

    def visit_BinaryOp(self,node):
        try:
            opcode = binary_ops[node.op] + "_float"
        except:
            opcode = None

        self.visit(node.left)
        self.visit(node.right)
        
        if opcode:
            target = self.new_temp()
            inst = (opcode, node.left.gen_location, node.right.gen_location, target)
            self.code.append(inst)
            node.gen_location = target

        else:
            opcode = "store_float"
            inst = (opcode, node.right.gen_location, node.left.gen_location)
            self.code.append(inst)
    
    def visit_PrList(self,node):
        self.visit(node.prlist[0])
        inst = ('print_float', node.prlist[0].gen_location)
        self.code.append(inst)


    def visit_StoreVar(self,node):
    	target = self.new_temp()
        node.gen_location = target
        inst = ('alloc_float', 
                node.name)
        self.code.append(inst)
        inst = ('store_float',
                node.gen_location,
                node.name)
        self.code.append(inst)


    def visit_LoadVar(self,node):
        target = self.new_temp()
        inst = ('load_float',
                node.name,
                target)
        self.code.append(inst)
        node.gen_location = target

   
    def visit_UnaryOp(self,node):
        self.visit(node.right)
        target = self.new_temp()
        node.gen_location = target
        opcode = unary_ops[node.op] + "_float" 
        inst = (opcode, node.right.gen_location,node.gen_location)
        self.code.append(inst)



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

    code_obj = generate_code(root)

    print '\n CODE \n'
    pprint.pprint(code_obj.code )
    
    