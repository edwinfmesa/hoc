# digraph AST{
#         n1[shape=box,label ="location(9)"];
# 	.
# 	.
# 	.
# 	n1->n2

# }

class Node_visitor(object):
	def visit(self,node):
		if node:
			method = "visit_"+node.__class__.__name__
			visitor= getattr(self, method, self.generic_visit)
			return visitor(node)
		else:
			return None

	def generic_visit(self,node):

		for field in getattr(node,"_fields"):
			value = getattr(node,field,None)
			if isinstance(value,list):
				for item in value:
					if isinstance(item,AST):
						self.visit(item)
			elif isinstance(value,AST):
				self.visit(None)
			else:
				return value


class DotVisitor(Node_visitor):
	def __init__(self,node):
		self.dot="diagraph AST{\n"
		self.id=0
		self.visit(node)

	def __str__(self):
		return self.dot +"\n}"

	# def Id(self):
	# 	self.id +=1
	# 	return "n%d" % self.id 
		
	# def visit_BinaryOp(self,node):
	# 	name=self.Id()
	# 	self.dot +="/t" + name +"[label="+ node.op + "]\n"

	# i=self.visit(node,left)
	# r=self.visit(node,right)
	# self.dot +="/t"+ name +"->"+ i + "\n"
	# self.dot +="/t"+ name +"->"+ r + "\n"
	# return name

	# def visit_UnaryOp(self,node):
	# 	1,2,3,5,7

	# def visit_location(self):
	# 	name= self.Id()
	# 	self.dot += "/t"+ name +"[shape=box,label=location("+node.name+")]\n"
	# 	return name

	# def visit_literal(self,node):
	#      1,2,3