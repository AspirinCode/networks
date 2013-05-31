# Notes:
- .gexf is Graph Exchange XML Format.  This is exported by NetworkX and read into gephi.
- .gephi are graphs that I have tweaked in gephi and saved.
- Gephi tips:
  - Uncheck 'resize/rescale nodes' box (I forget the exact wording).
  - I like the ForceAtlas2.  Look at one of my graphs to see the options I check.  Currently, this is purely for visual preference/clarity.
- PLEASE email me with any questions.  Some of this may be confusing, but I understand it all very well and can help immediately.  
- There are a lot of underscores missing below.  Github has a weird markup and it was changing font size so I removed.

# Practice Networks

## MorbidMap_networkX (first network created)

- contains morbidmap.txt from OMIM
- contains some preliminary graphics from NetworkX visualization (pre-gephi). 
- MM_edges.py ignore
- MM_tuples manipulates the data.  I create: 
  - Dictionaries of all diseases per gene, and all genes per diseases.
  - Tuples that contain 2 diseases that both target the same gene, as well as 2 genes that target the same disease.  These can be used to draw an edge between two nodes (the tuple items).
- MM_diseaseNetwork.py makes the .gexf file.  Copy and paste the desired code into ipython (mostly at the top) and the gexf command at the very bottom, , after running the _tuples.py file..  This was my first attempt at making gexf and is very poorly documented - sorry! 


## DrugBank_network

- contains all target_ids.csv from DrugBank.  This is formated by gene and lists the drugs that target it.
- DB_tuples.py manipulates the data.  I create: 
  - Dictionaries of all genes per drug, and all drugs per gene.
  - Tuples that contain 2 genes that both target the same drug, as well as 2 drugs that target the same gene.  These can be used to draw an edge between two nodes (the tuple items).
- DB_network.py makes the .gexf file.  Copy and paste the top part of the file (ignore the pygraphviz section) into ipython, after running the _tuples.py file.

## PathwayCommons_network

- ignore GeneSets network (similiar data to GSEA_network, slightly different format -- see README.TXT)
- GSEA network contains PathWay commons data in GSEA format
- same format as MM and DB above, but this time with pathways and genes

## PharmGKB_network

- reads in PharmGKB drug info and pulls out Drug Bank ID.  Does same for DB info, then creates list of overlaps (duplicates) bewteen the two sets.  This was the last code I worked on.  Utilimately it will be used to begin a ranking/confidence system.  

# More advanced networks - combined_network
- I typically now have one .py file to read in the data and export .gexf.  Make sure you comment out the write_gexf line, so you don't overwrite the existing file.


## DB gene MM

- Basic outline:
  - Read in DB data
  - Read in MM disease info. 
- Note: not super informative.

## OMIM-GSEA
- Basic outline:
  - First you need to read in MM info from the MM_tuple file above.  Then manually run line 2.
  - Then read in GSEA info (also above) and run line 5. 
  - Find common genes with line 27-end.
  - I'm not entirely sure where I was going with this, and should investigate further.

# Target Drug List (currently has both diabetes drugs and anticoagulants). 
- This is more evolved code and should be easier to read/work on.  
- 3 different version (2 complete, 1 in progress).
- target drug network.py
  Basic outline:
    - Read in a list of target drugs.  See filename1.
    - Read in DB drug/genes, only if DB drug is one of the target drugs.  Creates a corresponding gene set of all genes influenced by the kept DB drugs. 
    - Prints out if a target drug was not found in DB.
    - read in Morbid Map disease/gene data set, only if gene overlaps with culled gene_set.  Note, filter out disease if contains one of the words below (as a whole word OR fragment, not case sensitive). 
    - Create graph.
- target drug network w Pathway
  Basic outline:
    - Same as above, although now it goes target drugs -> DB gene (if target of target drug) -> pathway -> disease from MM (if has any gene in the pathway).  
- target drug network w PGKB
  This is NOT finished - will not work.  Eventually, this will incorporate the first ranking system by giving more weight (via node size/color) to drugs found in both PGKB and DB.

# Target Disease (currently just for breast cancer, but VERY easy to add more).
- Very similiar to Target Drug list above.
- Difference from Target Drug:
  - No need to import a target disease list.  This is a text filter at the top of the file.  Type whatver you want.  MM data will be filtered and kept ONLY if it contains this word/phrase.
  - DB read in and drug kept if it targets a gene kept in first filter.
  - Currently no pathway info.
  - Weakness: I don't currently filter out drugs ALREADY USED to treat the disease.  This would require reading in a list of known drugs (via DB Ids).  Not hard, but just not done yet.
