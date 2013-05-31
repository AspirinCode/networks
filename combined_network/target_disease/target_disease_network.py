### target disease -- we will select any diseases that contain these words
target_diseases = ['breast']


### read in MorbidMap disease and gene data

filename = 'morbidmap.txt'

def load_MM_culled_disease_data_set(filename):
    data_set = set()
    with open(filename,'r') as f:
        for line in f:
            x = line.strip().split('|')
            disease = x[0].strip()
            gene = x[1].strip().split(',')
            # these remove 1 space / no spaces in gene field
            z = [i for i in gene if i!= ' ']
            t = [i for i in z if i!= '']
            if any(target_disease in disease.lower() for target_disease in target_diseases):
                for i in t:
                    data_set.add((disease, i.strip()))
        return data_set

def create_MM_culled_disease_set(MM_culled_disease_data_set):
    disease_set = set()
    for item in MM_culled_disease_data_set:
        disease_set.add(item[0])
    return disease_set

def create_MM_culled_gene_set(MM_culled_disease_data_set):
    gene_set = set()
    for item in MM_culled_disease_data_set:
        gene_set.add(item[1])
    return gene_set

MM_culled_disease_data_set = load_MM_culled_disease_data_set(filename)
MM_culled_disease_set = create_MM_culled_disease_set(MM_culled_disease_data_set)
MM_culled_gene_set = create_MM_culled_gene_set(MM_culled_disease_data_set)

### read in DrugBank (DB) drugs/gene data_set and keep only if gene overlaps with MM_culled_gene_set

from csv import reader

filename2 = 'all_target_ids_all.csv'

def load_DB_culled_drug_data_set(filename2):
    data_set = set()
    with open(filename2,'r') as f:
        for line in reader(f):
            gene = line[2].strip()
            drugs = line[14].strip().split(';')
            for culled_gene in MM_culled_gene_set:
                if culled_gene == gene:
                    for drug in drugs:
                        if gene != '':
                            drug = drug.strip()
                            data_set.add((gene,drug))
        return data_set

def create_DB_culled_drug_set(DB_culled_drug_data_set):
    drug_set = set()
    for item in DB_culled_drug_data_set:
        drug_set.add(item[1])
    return drug_set

DB_culled_drug_data_set = load_DB_culled_drug_data_set(filename2)
DB_culled_drug_set = create_DB_culled_drug_set(DB_culled_drug_data_set)

### create gexf network file

import networkx as nx

g = nx.Graph()
g.add_nodes_from(MM_culled_disease_set,viz={'color':{'r':10,'g':200,'b':10,'a':0.5},'size':1})
g.add_nodes_from(MM_culled_gene_set,viz={'color':{'r':10,'g':10,'b':200,'a':0.5},'size':1})
g.add_nodes_from(DB_culled_drug_set,viz={'color':{'r':200,'g':10,'b':10,'a':0.5},'size':1})
g.add_edges_from(MM_culled_disease_data_set)
g.add_edges_from(DB_culled_drug_data_set)

# make sure to update fileNAME
nx.write_gexf(g,'breast_network.gexf',version='1.2draft')