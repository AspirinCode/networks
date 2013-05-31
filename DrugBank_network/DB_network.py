import networkx as nx

g = nx.Graph()
g.add_edges_from(gene_edge_tuples)
nx.write_gexf(g,'DB_gene_edges.gexf')

g = nx.Graph()
g.add_edges_from(drug_edge_tuples)
nx.write_gexf(g,'DB_drug_edges.gexf')


import pygraphviz as pgv
g=pgv.AGraph()
g.node_attr['label'] = ' '
g.node_attr['style'] = 'filled'
g.node_attr['color'] = 'green4'
g.node_attr['width'] = '0.05'
g.node_attr['height'] = '0.05'
g.add_edges_from(gene_edge_tuples)
g.draw('DB_gene_edges_circo.png', format='png', prog='circo')
