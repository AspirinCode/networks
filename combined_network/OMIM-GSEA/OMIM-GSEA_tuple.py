# load MM_tuples
MM = gene_set

# load GSEA_tuples
GSEA = gene_set

# intersect - produce new set with elements in common to both
common = MM & GSEA

"""# for testing
common = ['AKT','p53','BRCA1']
diseases_per_gene = {}
diseases_per_gene['AKT']=['D1']
diseases_per_gene['p53']=['D2','D3','D4']
diseases_per_gene['BRCA1']=['D1','D4']
pathways_per_gene = {}
pathways_per_gene['AKT']=['P1','P2']
pathways_per_gene['p53']=['P3']
pathways_per_gene['BRCA1']=['P1','P2','P4']"""


# Loop through common geens and combine disease and pathway from gene/disease dict
# and gene/pathway dict
## Note: gene/disease dict from MM is diseases_per_gene
## Note: gene/pathway dict from GSEA is pathways_per_gene

import itertools

def create_diseases_and_pathways(common):
    diseases_and_pathways = []
    for gene in common:
        diseases = diseases_per_gene[gene]
        pathways = pathways_per_gene[gene]
        temp = [(x, y) for y in pathways for x in diseases]
        diseases_and_pathways = diseases_and_pathways + temp
        #diseases_and_pathways.append(temp)
        #diseases_and_pathways = [item for sublist in diseases_and_pathways for item in sublist]
    return diseases_and_pathways


diseases_and_pathways = create_diseases_and_pathways(common)


## Exporting edge list tuples to gephi
import networkx as nx

g = nx.Graph()
g.add_edges_from(diseases_and_pathways)
nx.write_gexf(g, 'OMIM-GSEA_edges.gexf')
