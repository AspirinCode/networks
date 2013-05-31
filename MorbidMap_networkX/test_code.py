### Test code #####

import networkx as nx
import matplotlib.pyplot as plt
g = nx.Graph()

nx.draw(g)
plt.show()

x = [('b','c'),('d','e'),('f','e')]

y = {}
y['a']=('b','c')
y['d']=('e','f')
y['g']=('h','i')

###############################3

def NoneType_check(genes_per_disease):
for item in genes_per_disease:
    if item[0] == 0 or item[1] == 0:
        print item

none = NoneType_check(genes_per_disease)



### to test for None values in tuples
filter(lambda x: not x[0] or not x[1],gene_edge_tuples)

fxn = lambda x: not x[0] or not x[1]