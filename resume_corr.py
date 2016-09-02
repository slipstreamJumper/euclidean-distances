import sys


f = open(sys.argv[1] +".txt" , "r")
o = open(sys.argv[1] + ".csv", "w")

word_dict = {}

for line in f.readlines():
    l = line.replace("\n", "")
    l = l.replace("\r", "")
    l = l.replace(".", " ")
    l = l.replace(",", " ")
    l = l.replace(";", "")
    l = l.split(" ")
    for i in l:
        i = i.strip()
        if i in word_dict:
            word_dict[i] = word_dict[i] + 1
        elif i not in word_dict and i != "": 
            word_dict[i] = 1

o.write("word,count" + '\n')
for k in word_dict:
    o.write(k +"," +str(word_dict[k])+"\n")

f.close()
o.close()