import sys

total_dict = {}
for d in sys.argv[1:]:
    f=open(d, "r")
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
                 if i in total_dict[d]:
                     total_dict[d][i] = total_dict[d][i]+1
                 else:
                     total_dict[d][i]=1

term = str(input("End of file: "))

for d in total_dict:
    if term in total_dict[d]:
        print("doc: "+ d+ " term: "+ term+ " count: "+ str(total_dict[d][term]))
    else:
        print("doc: "+ d+ " term: "+ term+ " count: NOT IN DOCUMENT")


                 