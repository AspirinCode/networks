import networkx as nx

g = nx.Graph()
g.add_edges_from(gene_edge_tuples)
nx.write_gexf(g,'GSEA_gene_edges.gexf')

g = nx.Graph()
g.add_edges_from(pathway_edge_tuples)
nx.write_gexf(g,'GSEA_pathway_edges.gexf')