from csv import reader
import itertools

#filename = 'all_target_ids_all_test.csv'
filename = 'all_target_ids_all.csv'

def load_data_set(filename):
    data_set = set()
    with open(filename,'r') as f:
        for line in reader(f):
            gene = line[2].strip()
            drugs = line[14].strip().split(';')
            for drug in drugs:
                if gene != '': #this ensures that drugs w/ no associated gene are not added
                    data_set.add((gene,drug.strip()))
        return data_set

def load_gene_set(data_set):
    gene_set = set()
    for item in data_set:
        gene_set.add(item[0])
    return gene_set

def load_drug_set(data_set):
    drug_set = set()
    for item in data_set:
        drug_set.add(item[1])
    return drug_set

def load_genes_per_drug(data_set):
    d = {}
    for drug in drug_set:
        for item in data_set:
            if item[1] == drug:
                if drug in d:
                    d[drug].append(item[0])
                else:
                    d[drug] = [item[0]]
    return d

def load_drugs_per_gene(data_set):
    d = {}
    for gene in gene_set:
        for item in data_set:
            if item[0] == gene:
                if gene in d:
                    d[gene].append(item[1])
                else:
                    d[gene] = [item[1]]
    return d

def create_gene_edge_tuples(genes_per_drug):
    edge_tuples_lists = []
    for drug in genes_per_drug:
        if len(genes_per_drug[drug]) > 1:
            edge_tuples_lists.append(list(itertools.combinations(genes_per_drug[drug],2)))
    edge_tuples = [item for sublist in edge_tuples_lists for item in sublist]
    return edge_tuples

def create_drug_edge_tuples(drugs_per_gene):
    edge_tuples_lists = []
    for gene in drugs_per_gene:
        if len(drugs_per_gene[gene]) > 1:
            edge_tuples_lists.append(list(itertools.combinations(drugs_per_gene[gene],2)))
    edge_tuples = [item for sublist in edge_tuples_lists for item in sublist]
    return edge_tuples

data_set = load_data_set(filename)
gene_set = load_gene_set(data_set)
drug_set = load_drug_set(data_set)
genes_per_drug = load_genes_per_drug(data_set)
drugs_per_gene = load_drugs_per_gene(data_set)
gene_edge_tuples = create_gene_edge_tuples(genes_per_drug)
drug_edge_tuples = create_drug_edge_tuples(drugs_per_gene)