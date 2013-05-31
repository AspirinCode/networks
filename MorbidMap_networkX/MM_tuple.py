import itertools

#filename = 'morbidmap_test2.txt'
filename = 'morbidmap.txt'

def load_data_set(file):
    data_set = set()
    with open(file,'r') as f:
        for line in f:
            x = line.strip().split('|')
            y = x[1].strip().split(',')
            z = [i for i in y if i!= ' ']
            t = [i for i in z if i!= '']
            for i in t:
                data_set.add((str(x[0]), str(i.strip())))
        return data_set

def load_disease_set(file):
    disease_set = set()
    with open(file,'r') as f:
        for line in f:
            x = line.strip().split('|')
            disease_set.add(x[0])
        return disease_set

def load_gene_set(data_set):
    gene_set = set()
    for i in data_set:
        gene_set.add(i[1])
    return gene_set

def load_diseases_per_gene(data_set):
    d = {}
    for gene in gene_set:
        for item in data_set:
            if item[1] == gene:
                if gene in d:
                    d[gene].append(item[0])
                else:
                    d[gene] = [item[0]]
    return d

def load_genes_per_disease(data_set):
    d = {}
    for disease in disease_set:
        for item in data_set:
            if item[0] == disease:
                if disease in d:
                    d[disease].append(item[1])
                else:
                    d[disease] = [item[1]]
    return d

def create_disease_edge_tuples(diseases_per_gene):
    edge_tuples_lists = []
    for gene in diseases_per_gene:
        if len(diseases_per_gene[gene]) > 1:
            edge_tuples_lists.append(list(itertools.combinations(diseases_per_gene[gene],2)))
    edge_tuples = [item for sublist in edge_tuples_lists for item in sublist]
    return edge_tuples


def find_disease_single_nodes(diseases_per_gene):
    single_nodes_lists = []
    for gene in diseases_per_gene:
        if len(diseases_per_gene[gene]) == 1:
            single_nodes_lists.append(diseases_per_gene[gene])
    single_nodes = [item for sublist in single_nodes_lists for item in sublist]
    return single_nodes

def create_gene_edge_tuples(genes_per_disease):
    edge_tuples_lists = []
    for disease in genes_per_disease:
        if len(genes_per_disease[disease]) > 1:
            edge_tuples_lists.append(list(itertools.combinations(genes_per_disease[disease],2)))
    edge_tuples = [item for sublist in edge_tuples_lists for item in sublist]
    #edge_tuples_clean = [item for item in edge_tuples if item is not None]
    #edge_tuples_clean = filter(lambda x: x[0] is not None and x[1] is not None,edge_tuples)
    return edge_tuples


def find_gene_single_nodes(genes_per_disease):
    single_nodes_lists = []
    for disease in genes_per_disease:
        if len(genes_per_disease[disease]) == 1:
            single_nodes_lists.append(genes_per_disease[disease])
    single_nodes = [item for sublist in single_nodes_lists for item in sublist]
    return single_nodes

data_set = load_data_set(filename)
disease_set = load_disease_set(filename)
gene_set = load_gene_set(data_set)
diseases_per_gene = load_diseases_per_gene(data_set)
genes_per_disease = load_genes_per_disease(data_set)
disease_edge_tuples = create_disease_edge_tuples(diseases_per_gene)
disease_single_nodes = find_disease_single_nodes(diseases_per_gene)
gene_edge_tuples = create_gene_edge_tuples(genes_per_disease)
gene_single_nodes = find_gene_single_nodes(genes_per_disease)