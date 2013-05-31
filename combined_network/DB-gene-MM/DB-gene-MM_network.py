# read in DrugBank (DB) drugs/gene data_set -- all
from csv import reader
filename = 'all_target_ids_all.csv'

def load_DB_drug_data_set(filename):
    data_set = set()
    with open(filename,'r') as f:
        for line in reader(f):
            gene = line[2].strip()
            drugs = line[14].strip().split(';')
            for drug in drugs:
                drug = drug.strip()
                if gene != '':
                    data_set.add((gene.strip(),drug))
        return data_set

def load_DB_drug_set(DB_drug_data_set):
    drug_set = set()
    for i in DB_drug_data_set:
        drug_set.add(i[1])
    return drug_set

def load_DB_gene_set(DB_drug_data_set):
    gene_set = set()
    for i in DB_drug_data_set:
        gene_set.add(i[0])
    return gene_set

DB_drug_data_set = load_DB_drug_data_set(filename)
DB_drug_set = load_DB_drug_set(DB_drug_data_set)
DB_gene_set = load_DB_gene_set(DB_drug_data_set)

#read in Morbid Map disease/gene data_set -- all
filename2 = 'morbidmap.txt'

def load_MM_disease_data_set(filename2):
    data_set = set()
    with open(filename2,'r') as f:
        for line in f:
            x = line.strip().split('|')
            y = x[1].strip().split(',')
            z = [i for i in y if i!= ' ']
            t = [i for i in z if i!= '']
            for i in t:
                i = i.strip()
                data_set.add((x[0].strip(), i))
        return data_set

def load_MM_disease_set(MM_disease_data_set):
    disease_set = set()
    for i in MM_disease_data_set:
        disease_set.add(i[1])
    return disease_set

def load_MM_gene_set(MM_disease_data_set):
    gene_set = set()
    for i in MM_disease_data_set:
        gene_set.add(i[0])
    return gene_set

MM_disease_data_set = load_MM_disease_data_set(filename2)
MM_disease_set = load_MM_disease_set(MM_disease_data_set)
MM_gene_set = load_MM_gene_set(MM_disease_data_set)

# create gexf network file
import networkx as nx

g = nx.Graph()
g.add_nodes_from(DB_drug_set,viz={'color':{'r':255,'g':0,'b':0,'a':0.5},'size':100})
g.add_nodes_from(DB_gene_set,viz={'color':{'r':0,'g':0,'b':255,'a':0.5},'size':101})
g.add_nodes_from(MM_gene_set,viz={'color':{'r':0,'g':0,'b':200,'a':0.5},'size':101})
g.add_nodes_from(MM_disease_set,viz={'color':{'r':0,'g':255,'b':0,'a':0.5},'size':102})
g.add_edges_from(DB_drug_data_set)
g.add_edges_from(MM_disease_data_set)

nx.write_gexf(g,'DB-gene_MM_network.gexf',version='1.2draft')