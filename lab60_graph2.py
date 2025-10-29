import graphviz as gv
import functools

graph = functools.partial(gv.Graph,format='svg')
digraph = functools.partial(gv.Digraph,format='svg')

g3 = graph()
g4 = digraph()


def add_nodes(g,nodes):
    for n in nodes:
        if isinstance(n,tuple):
            pass
        else:
            g.add_node(n)
    return g

nodes = ['A','B','C','D','E','F']
g3 = add_nodes(g3,nodes)

g3.render(filename='graph/lab60_g3')
