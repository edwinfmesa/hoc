#compiladores Visitor

class DotVisitor(NodeVisitor):

	def init (self,node):
		self.dot = "digraph AST{\n"
		self.id=0
		self.visit(node)

	def str (self):
		return self.dot + "\n}"

	def Id(self):
		self.id += 1
		return "n%d" % self.id

	def visit.BinOp (self,node):
		name = self.Id()
		self.dot +="\t"+ name +"[label=""+ node.Op+"]\n"
		L = self.visit(node.left)
		R = self.visit(node.right)
		self.dot + = "\t" + name + "->" + L + "\n"
		self.dot + = "\t" + name + "->" + R + "\n"
		return name
	
	
class NodeVisitor(object):

	def visit(self,node):
		if node:
			method = "visit" + node class name
			visitor = getattr(self, method , self.generic_visit)
			return visitor (node)
		else:
		return name
def generic
	
	

