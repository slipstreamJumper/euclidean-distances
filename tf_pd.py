import sys
import math

### Feed this a reference term (sys.argv[1]) and a list of documents
### sys.argv[2:] and it will generate the Term Document Frequency of 
### the reference term against the corpus of provided documents. 

### usage: python tf_pd.py [reference_term] [doc1] [doc2] ... [docN]



total_dict = {}
master_term = str(sys.argv[1])
master_words = {}
for d in sys.argv[2:]:
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

print("")
print("")

print("Term for Reference: '" + str(master_term + "'"))
print("Master Term Count: " + str(len(master_words.keys())))
if master_term in master_words:
    
    to= float(len(master_words.keys()))
    te = float(master_words[master_term])
    print("Total Term Count: " + str(te))
    tf = te/to
    print("Total Term Freq: " + str(tf))    
    print("")
    for doc in total_dict:
        if master_term in total_dict[doc]:
            total = float(len(total_dict[doc].keys()))
            term= float(total_dict[doc][master_term])
            print("Total Word Count in " + str(doc) + ": " + str(total))            
            print("Total Term Count in " + str(doc) + ": " + str(term))
            tdf = term/total
            print("Total Term Freq in " + str(doc) + ": " + str(round(tdf,10)))
            print("")
        else:
            print("Term not in " + str(doc) + "!!!")
            print("")
else:
    print("Term not in any documents!!") 



    