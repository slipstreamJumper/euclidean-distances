import sys

### Feed this two documents (sys.argv[1] and sys.argv[2]) and it will 
### generate the Euclidean distance between those two documents. 

### usage: python euclidean_dist_dir.py [document1] [document2]


total_dict = {}

master_words = {}
docs = []
for d in sys.argv[1:]:
    docs.append(d)
    f=open(d, "r")
    #print("Document: ", str(d))
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
eu_distance = 0

for word in list(total_dict[docs[0]].keys()) + list(total_dict[docs[1]].keys()):
    if word in total_dict[docs[0]] and word not in total_dict[docs[1]]:
        total_dict[docs[1]][word] = .0001;
    if word in total_dict[docs[1]] and word not in total_dict[docs[0]]:
        total_dict[docs[0]][word] = .0001;
        
    f1 = float(total_dict[docs[0]][word])
    f2 = float(total_dict[docs[1]][word])
    eu_distance = eu_distance + ((f1-f2)**2)

eu_distance = eu_distance**.5
print("")
print("")

print("E-Distance " + str(docs[0]) + " | " + str(docs[1]) + " = " + str(eu_distance))
