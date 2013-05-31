from csv import reader
import itertools

#filename = 'homo-sapiens-9606-gene-symbol_test.gmt'
#filename = 'homo-sapiens-9606-gene-symbol_head250.gmt'
filename = 'homo-sapiens-9606-gene-symbol.gmt'

# while we could make a dictionary from the input data, using a set ensures no
# repeated entries and allows to edit out '' and 'NOT_SPECIFIED'
def load_data_set(filename):
    data_set = set()
    f=reader(open(filename,'r'),delimiter='\t')
    for line in f:
        pathway = line[0].strip()
        genes = line[2:]
        for gene in genes:
            if gene != '' and gene != 'NOT_SPECIFIED':
                data_set.add((str(pathway),str(gene.strip())))
    return data_set

def load_pathway_set(data_set):
    pathway_set = set()
    for item in data_set:
        pathway_set.add(item[0])
    return pathway_set

def load_gene_set(data_set):
    gene_set = set()
    for item in data_set:
        gene_set.add(item[1])
    return gene_set

def load_genes_per_pathway(data_set):
    d = {}
    for pathway in pathway_set:
        for item in data_set:
            if item[0] == pathway:
                if pathway in d:
                    d[pathway].append(item[1])
                else:
                    d[pathway] = [item[1]]
    return d

def load_pathways_per_gene(data_set):
    d = {}
    for gene in gene_set:
        for item in data_set:
            if item[1] == gene:
                if gene in d:
                    d[gene].append(item[0])
                else:
                    d[gene] = [item[0]]
    return d

def create_gene_edge_tuples(genes_per_pathway):
    edge_tuples_lists = []
    for pathway in genes_per_pathway:
        if len(genes_per_pathway[pathway]) > 1:
            edge_tuples_lists.append(list(itertools.combinations(genes_per_pathway[pathway],2)))
    edge_tuples = [item for sublist in edge_tuples_lists for item in sublist]
    return edge_tuples

def create_pathway_edge_tuples(pathways_per_gene):
    edge_tuples_lists = []
    for gene in pathways_per_gene:
        if len(pathways_per_gene[gene]) > 1:
            edge_tuples_lists.append(list(itertools.combinations(pathways_per_gene[gene],2)))
    edge_tuples = [item for sublist in edge_tuples_lists for item in sublist]
    return edge_tuples

data_set = load_data_set(filename)
pathway_set = load_pathway_set(data_set)
gene_set = load_gene_set(data_set)
genes_per_pathway = load_genes_per_pathway(data_set)
pathways_per_gene = load_pathways_per_gene(data_set)
gene_edge_tuples = create_gene_edge_tuples(genes_per_pathway)
pathway_edge_tuples = create_pathway_edge_tuples(pathways_per_gene)

# Trying to find non-ascii-encoded value
"""
for item in pathway_edge_tuples:
    for value in item:
        try:
            value.decode('ascii')
        except UnicodeDecodeError:
            print value
            print "It was not an ascii-encoded unicode string"
            """