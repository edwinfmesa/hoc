from graphviz import Digraph
import datetime
import random

dot = Digraph(comment='Compilador')

# dot  #doctest: +ELLIPSIS

#Add nodes and edges:

dot.node('A1', 'Nodo A1')
# dot.node('B1', 'Nodo B1')
# dot.node('L1', 'Nodo L1')

# dot.edges(['AB', 'AL'])
# dot.edge('A1','B1')
# dot.edge('A1','L1')
# dot.edge('B', 'L', constraint='false')


# print(dot.source)  
if __name__ == '__main__':
    filename = 'AST/ast'+str(int(100*random.random()))+'.gv'
    dot.render(filename, view=True)
    
