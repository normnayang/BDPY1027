import graphviz as gv

g1 = gv.Digraph(format='svg')

g1.node('A')
g1.node('B')
g1.edge('A','B')
g1.edge('B','A')
print(g1.source)
g1.render(filename='graph/lab59')