# read in list of target drugs and pull out DB ID's

#filename1 = 'diabetic_drugs.txt'
filename1 = 'anticoagulant_drugs.txt'

def load_target_drug_data_set(file):
    data_set = set()
    with open(file,'r') as f:
        for line in f:
            x = line.strip().split('|')
            y = x[1].strip().split(',')
            z = [i for i in y if i!= ' ']
            t = [i for i in z if i!= '']
            for i in t:
                data_set.add((str(x[0].strip()), str(i.strip())))
        return data_set

def load_target_drug_list(drug_data_set):
    drug_list = []
    for i in target_drug_data_set:
        drug_list.append(i[1])
    return drug_list

def load_target_drugname_dict(drug_data_set):
    d = {}
    for drug in target_drug_list:
        for item in target_drug_data_set:
            if item[1] == drug:
                if drug in d:
                    d[drug].append(item[0])
                else:
                    d[drug] = [item[0]]
    return d

target_drug_data_set = load_target_drug_data_set(filename1)
target_drug_list = load_target_drug_list(target_drug_data_set)
target_drugname_dict = load_target_drugname_dict(target_drug_data_set)

# read in DrugBank (DB) drugs/gene data_set -- only if drug overlaps with target_drugs
from csv import reader
filename2 = 'all_target_ids_all.csv'

def load_DB_culled_drug_data_set(filename2):
    data_set = set()
    rejected_drugs = set()
    with open(filename2,'r') as f:
        for line in reader(f):
            gene = line[2].strip()
            drugs = line[14].strip().split(';')
            for drug in drugs:
                for target_drug in target_drug_list:
                    drug = drug.strip()
                    if drug == target_drug and gene != '':
                        data_set.add((gene,drug))
        return data_set

def create_DB_culled_drug_set(DB_culled_drug_data_set):
    drug_set = set()
    for item in DB_culled_drug_data_set:
        drug_set.add(item[1])
    return drug_set

def create_culled_gene_set(DB_culled_drug_data_set):
    gene_set = set()
    for item in DB_culled_drug_data_set:
        gene_set.add(item[0])
    return gene_set

DB_culled_drug_data_set = load_DB_culled_drug_data_set(filename2)
DB_culled_drug_set = create_DB_culled_drug_set(DB_culled_drug_data_set)
culled_gene_set = create_culled_gene_set(DB_culled_drug_data_set)

# print out the drugs not kept from the target list
from collections import Counter

found = DB_culled_drug_set
expected = set(target_drug_list)
diff = expected.difference(found)
for drug in diff:
    print "Either not in DB or no known gene: %s" % drug
print

#read in Morbid Map disease/gene data_set -- only if gene overlaps with culled_gene_set

filename3 = 'morbidmap.txt'

# filter out any diseases that include these words
#filter_list = ['diabete','insulin']
filter_list = ['thrombo','heparain','stroke','warfarin','clot','platelet','plasmin']

def load_MM_culled_disease_data_set(filename3):
    data_set = set()
    with open(filename3,'r') as f:
        for line in f:
            x = line.strip().split('|')
            y = x[1].strip().split(',')
            z = [i for i in y if i!= ' ']
            t = [i for i in z if i!= '']
            for i in t:
                i = i.strip()
                for gene in culled_gene_set:
                    if i == gene:
                        if any(disease in x[0].lower() for disease in filter_list):
                            print "Removing %s" % x[0]
                        else:
                            data_set.add((x[0], i))
        return data_set

def create_MM_culled_disease_set(MM_culled_disease_data_set):
    disease_set = set()
    for item in MM_culled_disease_data_set:
        disease_set.add(item[0])
    return disease_set

MM_culled_disease_data_set = load_MM_culled_disease_data_set(filename3)
MM_culled_disease_set = create_MM_culled_disease_set(MM_culled_disease_data_set)

# create gexf network file

import networkx as nx

g = nx.Graph()
g.add_nodes_from(DB_culled_drug_set,viz={'color':{'r':200,'g':10,'b':10,'a':0.5},'size':1})
g.add_nodes_from(culled_gene_set,viz={'color':{'r':10,'g':10,'b':200,'a':0.5},'size':1})
g.add_nodes_from(MM_culled_disease_set,viz={'color':{'r':10,'g':200,'b':10,'a':0.5},'size':1})
g.add_edges_from(DB_culled_drug_data_set)
g.add_edges_from(MM_culled_disease_data_set)

# make sure to updated fileNAME
nx.write_gexf(g,'anticoagulant_network.gexf',version='1.2draft')
