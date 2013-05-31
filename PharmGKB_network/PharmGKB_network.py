from csv import reader

### reading in PharmGKB drug names and assocaited DB id's

PGKB_filename = 'drugs.tsv'
#PGKB_filename = 'drugs_test.tsv'

def load_PGKB_data_set(filename):
    data_set = set()
    with open(filename,'r') as f:
        for line in reader(f,delimiter='\t'):
            drug_name = line[1].strip()
            crossref = line[6].strip().split(',')
            drugBank = filter(lambda x: 'drugBank' in x,crossref) #this returns string 'drugBank:DB#####'
            if drugBank != []:
                DB_id = drugBank[0][9:] # returns just the DB id #
                data_set.add((drug_name,DB_id))
        return data_set

def load_PGKB_drugName_set(data_set):
    drugName_set = set()
    for item in data_set:
        drugName_set.add(item[0])
    return drugName_set

def load_PGKB_drugID_set(data_set):
    drugID_set = set()
    for item in data_set:
        drugID_set.add(item[1])
    return drugID_set

PGKB_data_set = load_PGKB_data_set(PGKB_filename)
PGKB_drugName_set = load_PGKB_drugName_set(PGKB_data_set)
PGKB_drugID_set = load_PGKB_drugID_set(PGKB_data_set)

### reading in DrugBank drugs and gene targets

DB_filename = 'all_target_ids_all.csv'
#DB_filename = 'all_target_ids_all_test.csv'

def load_DB_data_set(filename):
    data_set = set()
    with open(filename,'r') as f:
        for line in reader(f):
            gene = line[2].strip()
            drugs = line[14].strip().split(';')
            for drug in drugs:
                if gene != '': #this ensures that drugs w/ no associated gene are not added
                    data_set.add((gene,drug.strip()))
        return data_set

def load_DB_gene_set(data_set):
    gene_set = set()
    for item in data_set:
        gene_set.add(item[0])
    return gene_set

def load_DB_drug_set(data_set):
    drug_set = set()
    for item in data_set:
        drug_set.add(item[1])
    return drug_set

DB_data_set = load_DB_data_set(DB_filename)
DB_gene_set = load_DB_gene_set(DB_data_set)
DB_drug_set = load_DB_drug_set(DB_data_set)

### Make list of drugs present in both PGKB and DB

# (more) pythonic way!
def check_duplicates(DB_drug_set):
    duplicates = set()
    for drug in DB_drug_set:
        if any(PGKB_drugID in drug for PGKB_drugID in PGKB_drugID_set):
            duplicates.add(drug)
    return duplicates

# longer way to do this
"""def check_duplicates(DB_drug_set):
    duplicates = set()
    for DB_drug in DB_drug_set:
        for PGKB_drugID in PGKB_drugID_set:
            if DB_drug == PGKB_drugID:
                duplicates.add(DB_drug)
    return duplicates"""

duplicates = check_duplicates(DB_drug_set)

# create gexf network file

import networkx as nx

g = nx.Graph()
g.add_nodes_from(PGKB_drugID_set,viz={'color':{'r':200,'g':10,'b':10,'a':0.5},'size':15})
g.add_nodes_from(DB_drug_set,viz={'color':{'r':100,'g':10,'b':10,'a':0.5},'size':15})
g.add_nodes_from(duplicates,viz={'color':{'r':10,'g':200,'b':10,'a':0.5},'size':20})

# make sure to updated fileNAME
nx.write_gexf(g,'PharmGKB_network.gexf',version='1.2draft')


#### TESTING #####
"""
'red'= {'r':200,'g':10,'b':10,'a':0.5}

nodeAtt = {}
nodeAtt['label']='test'
nodeAtt['size']=2


g = nx.Graph()


nx.write_gexf(g,'test.gexf',version='1.2draft')
"""