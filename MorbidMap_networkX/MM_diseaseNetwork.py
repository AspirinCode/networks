
# Basic networkx graph

import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()
g.add_edges_from(data_set)
nx.draw(g)
plt.show()

# Graph with edges and single nodes
g = nx.Graph()
g.add_edges_from(disease_edge_tuples)
nx.draw_networkx(g,with_labels=False,node_size=50,width=5.0,edge_color='k')
plt.show()

g.add_nodes_from(disease_single_nodes)



# Basic pygraphviz graph -- diseases

import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

g=pgv.AGraph()
g.node_attr['label'] = ' '
g.node_attr['style'] = 'filled'
g.node_attr['color'] = 'slategrey'
g.node_attr['width'] = '0.1'
g.node_attr['height'] = '0.1'
g.add_edges_from(disease_edge_tuples)
g.node_attr['label'] = ' '
g.node_attr['style'] = 'filled'
g.node_attr['color'] = 'green4'
g.node_attr['width'] = '0.1'
g.node_attr['height'] = '0.1'
g.add_nodes_from(disease_single_nodes)
g.draw('MM_disease_circo.png', format='png', prog='circo')


g=pgv.AGraph()
g.node_attr['label'] = ' '
g.node_attr['style'] = 'filled'
g.node_attr['color'] = 'green4'
g.node_attr['width'] = '0.05'
g.node_attr['height'] = '0.05'
g.add_edges_from(disease_edge_tuples)
g.draw('MM_disease_edges_neato.png', format='png', prog='neato')
g.draw('MM_disease_edges_fdp.png', format='png', prog='fdp')
g.draw('MM_disease_edges_sfdp.png', format='png', prog='sfdp')
g.draw('MM_disease_edges_twopi.png', format='png', prog='twopi')
g.draw('MM_disease_edges_circo.png', format='png', prog='circo')

#Error
g.draw('MM_disease_edges_dot.png', format='png', prog='dot')



# Basic pygraphviz graph -- genes

import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz as pgv

g=pgv.AGraph()
g.node_attr['label'] = ' '
g.node_attr['style'] = 'filled'
g.node_attr['color'] = 'green4'
g.node_attr['width'] = '0.05'
g.node_attr['height'] = '0.05'
g.add_edges_from(gene_edge_tuples)
g.draw('MM_gene_edges_neato.png', format='png', prog='neato')
g.draw('MM_gene_edges_fdp.png', format='png', prog='fdp')
g.draw('MM_gene_edges_sfdp.png', format='png', prog='sfdp')
g.draw('MM_gene_edges_twopi.png', format='png', prog='twopi')
g.draw('MM_gene_edges_circo.png', format='png', prog='circo')


nx.write_gexf(g,'disease_edges.gexf')