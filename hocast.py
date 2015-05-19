# mpasast.py
# -*- coding: utf-8 -*-
'''
Objetos Arbol de Sintaxis Abstracto (AST - Abstract Syntax Tree).

Este archivo define las clases para los diferentes tipos de nodos del
árbol de sintaxis abstracto.  Durante el análisis sintático, se debe 
crear estos nodos y conectarlos.  En general, usted tendrá diferentes
nodos AST para cada tipo de regla gramatical.  Algunos ejemplos de
nodos AST pueden ser encontrados al comienzo del archivo.  Usted deberá
añadir más.
'''

# NO MODIFICAR
class AST(object):
	'''
	Clase base para todos los nodos del AST.  Cada nodo se espera 
	definir el atributo _fields el cual enumera los nombres de los
	atributos almacenados.  El método a continuación __init__() toma
	argumentos posicionales y los asigna a los campos apropiados.
	Cualquier argumento adicional especificado como keywords son 
	también asignados.
	'''
	_fields = []
	def __init__(self,*args,**kwargs):
		assert len(args) == len(self._fields)
		for name,value in zip(self._fields,args):
			setattr(self,name,value)
		# Asigna argumentos adicionales (keywords) si se suministran
		for name,value in kwargs.items():
			setattr(self,name,value)

	def pprint(self):
		for depth, node in flatten(self):
			print("%s%s" % (" "*(4*depth),node))

def validate_fields(**fields):
	def validator(cls):
		old_init = cls.__init__
		def __init__(self, *args, **kwargs):
			old_init(self, *args, **kwargs)
			for field,expected_type in fields.items():
				assert isinstance(getattr(self, field), expected_type)
		cls.__init__ = __init__
		return cls
	return validator

# ----------------------------------------------------------------------
# Nodos AST especificos
#
# Para cada nodo es necesario definir una clase y añadir la especificación
# del apropiado _fields = [] que indique que campos deben ser almacenados.
# A modo de ejemplo, para un operador binario es posible almacenar el
# operador, la expresión izquierda y derecha, como esto:
# 
#    class Binop(AST):
#        _fields = ['op','left','right']
# ----------------------------------------------------------------------

# Unos pocos nodos ejemplos

class PrintStatement(AST):
	'''
	print expression ;
	'''
	_fields = ['expr']

class Literal(AST):
	'''
	Un valor constante como 2, 2.5, o "dos"
	'''
	_fields = ['value']

class Program(AST):
	_fields = ['program']

@validate_fields(statements=list)
class StatementList(AST):
	_fields = ['statements']

	def append(self,e):
		self.statements.append(e)

# ED
@validate_fields(proglist=list)
class ProgList(AST):
	_fields = ['proglist']

	def append(self,e):
		self.proglist.append(e)


# ED
class ReturnValue(AST):
	_fields = ['return','value']

# ED
class PrintValue(AST):
	_fields = ['print','value']

class Statement(AST):
	_fields = ['statement']

class Extern(AST):
	_fields = ['func_prototype']

class FuncPrototype(AST):
	_fields = ['id', 'params', 'typename']

@validate_fields(param_decls=list)
class Parameters(AST):
	_fields = ['param_decls']

	def append(self,e):
		self.param_decls.append(e)

class ParamDecl(AST):
	_fields = ['id', 'typename']

class AssignmentStatement(AST):
	_fields = ['location', 'value']

class ConstDeclaration(AST):
	_fields = ['id', 'value']

class VarDeclaration(AST):
	_fields = ['id', 'typename', 'value']

class IfStatement(AST):
	_fields = ['condition', 'then_b', 'else_b']

class WhileStatement(AST):
	_fields = ['condition', 'body']

class LoadLocation(AST):
	_fields = ['name']

class StoreVar(AST):
	_fields = ['name']

class UnaryOp(AST):
	_fields = ['op', 'left']

class BinaryOp(AST):
	_fields = ['op', 'left', 'right']

class RelationalOp(AST):
	_fields = ['op', 'left', 'right']
	
class Group(AST):
	_fields = ['expression']

class FunCall(AST):
	_fields = ['id', 'params']

class ExprList(AST):
	_fields = ['expressions']

	def append(self, e):
		self.expressions.append(e)

#ED
class Expression(AST):
	_fields = ['expression']

	# def __unicode__(self):
	# 	print "expr", self.expression

class Empty(AST):
	_fields = []

	# def append(self, e):
	# 	self.expressions.append(e)
#

# class NewLine(AST):
# 	_fields = []

class GroupParent(AST):
	_fields = ['lp','expr','rp']
#
class ArgList(AST):
	_fields = ['arglist']	

	def append(self, e):
		self.arglist.append(e)
#
class FormalsList(AST):
	_fields = ['formallist']	

	def append(self, e):
		self.formallist.append(e)

class Calls(AST):
	_fields = ['function','arglist']

class LoadVar(AST):
	_fields = ['name']	

class FuncDef(AST):
	_fields = ['function','formals','stmt']

# Usted deberá añadir mas nodos aquí.  Algunos nodos sugeridos son
# BinaryOperator, UnaryOperator, ConstDeclaration, VarDeclaration, 
# AssignmentStatement, etc...

# ----------------------------------------------------------------------
#                  NO MODIFIQUE NADA AQUI ABAJO
# ----------------------------------------------------------------------

# Las clase siguientes para visitar y reescribir el AST son tomadas
# desde el módulo ast de python .

# NO MODIFIQUE
class NodeVisitor(object):
	'''
	Clase para visitar nodos del árbol de sintaxis.  Se modeló a partir
	de una clase similar en la librería estándar ast.NodeVisitor.  Para
	cada nodo, el método visit(node) llama un método visit_NodeName(node)
	el cual debe ser implementado en la subclase.  El método genérico
	generic_visit() es llamado para todos los nodos donde no hay coincidencia
	con el método visit_NodeName().
	
	Es es un ejemplo de un visitante que examina operadores binarios:

		class VisitOps(NodeVisitor):
			visit_Binop(self,node):
				print("Operador binario", node.op)
				self.visit(node.left)
				self.visit(node.right)
			visit_Unaryop(self,node):
				print("Operador unario", node.op)
				self.visit(node.expr)

		tree = parse(txt)
		VisitOps().visit(tree)
	'''
	def visit(self,node):
		'''
		Ejecuta un método de la forma visit_NodeName(node) donde
		NodeName es el nombre de la clase de un nodo particular.
		'''
		if node:
			method = 'visit_' + node.__class__.__name__
			visitor = getattr(self, method, self.generic_visit)
			return visitor(node)
		else:
			return None
	
	def generic_visit(self,node):
		'''
		Método ejecutado si no se encuentra médodo aplicable visit_.
		Este examina el nodo para ver si tiene _fields, es una lista,
		o puede ser recorrido completamente.
		'''
		for field in getattr(node,"_fields"):
			value = getattr(node,field,None)
			if isinstance(value, list):
				for item in value:
					if isinstance(item,AST):
						self.visit(item)
			elif isinstance(value, AST):
				self.visit(value)

# NO MODIFICAR
class NodeTransformer(NodeVisitor):
	'''
	Clase que permite que los nodos del arbol de sintraxis sean 
	reemplazados/reescritos.  Esto es determinado por el valor retornado
	de varias funciones visit_().  Si el valor retornado es None, un
	nodo es borrado. Si se retorna otro valor, reemplaza el nodo
	original.
	
	El uso principal de esta clase es en el código que deseamos aplicar
	transformaciones al arbol de sintaxis.  Por ejemplo, ciertas optimizaciones
	del compilador o ciertas reescrituras de pasos anteriores a la generación
	de código.
	'''
	def generic_visit(self,node):
		for field in getattr(node,"_fields"):
			value = getattr(node,field,None)
			if isinstance(value,list):
				newvalues = []
				for item in value:
					if isinstance(item,AST):
						newnode = self.visit(item)
						if newnode is not None:
							newvalues.append(newnode)
					else:
						newvalues.append(n)
				value[:] = newvalues
			elif isinstance(value,AST):
				newnode = self.visit(value)
				if newnode is None:
					delattr(node,field)
				else:
					setattr(node,field,newnode)
		return node

# NO MODIFICAR
def flatten(top):
	'''
	Aplana el arbol de sintaxis dentro de una lista para efectos
	de depuración y pruebas.  Este retorna una lista de tuplas de
	la forma (depth, node) donde depth es un entero representando
	la profundidad del arból de sintaxis y node es un node AST
	asociado.
	'''
	class Flattener(NodeVisitor):
		def __init__(self):
			self.depth = 0
			self.nodes = []
		def generic_visit(self,node):
			self.nodes.append((self.depth,node))
			self.depth += 1
			NodeVisitor.generic_visit(self,node)
			self.depth -= 1

	d = Flattener()
	d.visit(top)
	return d.nodes


from graphviz import Digraph
import datetime
import random


class DotVisitor(NodeVisitor):
	def __init__(self,node):
		self.dot2 = Digraph(comment='Compilador')
		self.dot="digraph AST{\n"
		self.id=0
		self.visit(node)

	def __str__(self):
		
		filename = 'AST/ast'+str(int(100*random.random()))+'.gv'
		self.dot2.render(filename, view=True)
		return self.dot +"\n}"

	def Id(self):
		self.id +=1
		return "n%d" % self.id 

	def visit_Literal(self,node):

		name = self.Id()
		# print name, node, node.value
		label = node.value
		if label == '\n':
			label = 'NEWLINE'
		self.dot +="\t" + name +"[label="+ str(label) + "]\n"
		self.dot2.node(name, str(str(name)+"  "+str(label)))
		return name

	def visit_BinaryOp(self,node):
		name=self.Id()
		self.dot +="\t" + name +"[label="+ node.op + "]\n"
		self.dot2.node(name, str(str(name)+"  "+str(node.op)))

		# print "-",node
		# print "-",node.left 
		# print "-",node.right
		l=self.visit(node.left)
		
		r=self.visit(node.right)
		# print r
		self.dot +="\t"+ name +"->"+ l + "\n"
		self.dot +="\t"+ name +"->"+ r + "\n"

		self.dot2.edge(name,l)
		self.dot2.edge(name,r)
		return name

	def visit_Expression(self,node):
		
		name=self.Id()
		expr = self.visit(node.expression)

		# print expr, node.expression
		# print "N1 --------",expr
		self.dot +="\t"+ name +"->"+ expr + "\n"
		self.dot +="\t" + name +"[label="+ "expr" + "]\n"

		self.dot2.edge(name,expr)
		self.dot2.node(name, str(str(name)+"  expr"))
		return name

	def visit_Statement(self,node):

		name=self.Id()
		stmt = self.visit(node.statement)


		# print "N1 --------",expr
		self.dot +="\t"+ name +"->"+ stmt + "\n"
		self.dot +="\t" + name +"[label="+ "stmt" + "]\n"

		self.dot2.edge(name,stmt)
		self.dot2.node(name, str(str(name)+"  stmt"))

		return name

	def visit_Empty(self,node):
		name = self.Id()
		self.dot +="\t" + name +"[label="+ "Empty" + "]\n"
		self.dot2.node(name, str(str(name)+"  "+"Empty"))
		return name

	def visit_ProgList(self,node):
		name = self.Id()
		self.dot +="\t" + name +"[label="+ "ProgList" + "]\n"
		self.dot2.node(name, str(name)+"  "+"ProgList")

		# print node.proglist

		for pl in node.proglist:
			list_obj = self.visit(pl)
			print "OBJ",pl,list_obj
			self.dot +="\t"+ name +"->"+ list_obj + "\n"
			self.dot2.edge(name,list_obj)

		return name


	def visit_StatementList(self,node):
		name = self.Id()
		self.dot +="\t" + name +"[label="+ "StatementList" + "]\n"
		self.dot2.node(name, str(name)+"  "+"StatementList")

		# print node.proglist

		for st in node.statements:
			list_obj = self.visit(st)
			# print "OBJ",st,list_obj
			self.dot +="\t"+ name +"->"+ list_obj + "\n"
			self.dot2.edge(name,list_obj)

		return name

	def visit_FormalsList(self,node):
		name = self.Id()
		self.dot +="\t" + name +"[label="+ "FormalsList" + "]\n"
		self.dot2.node(name, str(name)+"  "+"FormalsList")

		print "FORMALLIST", node.formallist

		for obj in node.formallist:
			list_obj = self.visit(obj)
			self.dot +="\t"+ name +"->"+ list_obj + "\n"
			self.dot2.edge(name,list_obj)

		return name

	def visit_StoreVar(self,node):
		name = self.Id()
		label = node.name

		self.dot +="\t" + name +"[label="+ str(label) + "]\n"
		self.dot2.node(name, str(str(name)+"  StoreVar("+str(label)+")"))

		return name	

	def visit_LoadVar(self,node):
		name = self.Id()
		label = node.name

		self.dot +="\t" + name +"[label="+ str(label) + "]\n"
		self.dot2.node(name, str(str(name)+"  LoadVar("+str(label)+")"))

		return name	

	def visit_GroupParent(self,node):
		name=self.Id()
		expr = self.visit(node.expr)

		
		self.dot +="\t" + name +"[label="+ "(GroupParent)" + "]\n"
		self.dot +="\t"+ name +"->"+ expr + "\n"

		self.dot2.edge(name,expr)
		self.dot2.node(name, str(str(name)+"  (GroupParent)"))
		return name

	def visit_FuncDef(self,node):
		name=self.Id()
		self.dot +="\t" + name +"[label="+ "(FuncDef)" + "]\n"
		self.dot2.node(name, str(str(name)+"  (FuncDef)"))

		# print node.function,node.formals, node.stmt

		function_id = self.visit(node.function)
		formals_id = self.visit(node.formals)
		stmt_id = self.visit(node.stmt)

		# print function,formals,stmt

		self.dot +="\t"+ name +"->"+ function_id + "\n"
		self.dot +="\t"+ name +"->"+ formals_id + "\n"
		self.dot +="\t"+ name +"->"+ stmt_id + "\n"
		self.dot2.edge(name,function_id)
		self.dot2.edge(name,formals_id)
		self.dot2.edge(name,stmt_id)

		

		return name
		

	# def visit_UnaryOp(self,node):
	# 	1,2,3,5,7

	# def visit_location(self):
	# 	name= self.Id()
	# 	self.dot += "/t"+ name +"[shape=box,label=location("+node.name+")]\n"
	# 	return name

	# def visit_literal(self,node):
	#      1,2,3