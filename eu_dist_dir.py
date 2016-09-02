import sys
import os
import copy


### Feed this a document and it will generate the Euclidean distance
### between that document and every other .txt file in the current
### working directory.

### usage: python eu_dist_dir.py [reference document]


total_dict = {}
master_words = {}
docs = []
ref_doc = str(sys.argv[2])
directory= str(sys.argv[1])
for d in os.listdir(directory):
    if d.endswith(".txt"):
        docs.append(d)
        f=open(directory+"/"+d, "r")
        print("Document: ", str(d))
        total_dict[d] = {}
        for line in f.readlines():     
             l = line.replace("\n", "")
             l = l.replace("\r", "")
             l = l.replace(".", " ")
             l = l.replace(",", " ")
             l = l.replace(";", "")
             l = l.split(" ")
             for i in l:
                 i = i.strip()
                 i = i.lower()
                 if i != "": 
                     if i in master_words:
                         master_words[i] = master_words[i]+1
                     else:
                         master_words[i]=1
                     if i in total_dict[d]:
                         total_dict[d][i] = total_dict[d][i]+1
                     else:
                         total_dict[d][i]=1

for d in docs:
    eu_distance = 0
    temp_ref_doc = copy.copy(total_dict[ref_doc])
    temp_compare = copy.copy(total_dict[d])
    for word in list(temp_ref_doc.keys()) + list(temp_compare.keys()):
        if word in temp_ref_doc and word not in temp_compare:
            temp_compare[word] = .0001;
        if word in temp_compare and word not in temp_ref_doc:
            temp_ref_doc[word] = .0001;
            
        f1 = float(temp_ref_doc[word])
        f2 = float(temp_compare[word])
        eu_distance = eu_distance + ((f1-f2)**2)
    eu_distance = eu_distance**.5    
   
    print("Eu Dist: " + ref_doc + " | " + d + " = " + str(eu_distance))    
    




