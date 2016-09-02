import sys
from scipy.stats.stats import pearsonr   
import numpy
from difflib import SequenceMatcher

#f = open(sys.argv[1] +".txt" , "r")
#s = open(sys.argv[2] +".txt" , "r")

f = open("job_desc.txt" , "r")
s = open("text_application.txt" , "r")

word_dict = {}
first_list = []
second_list = []

for line in f.readlines():
    l = line.replace("\n", "")
    l = l.replace("\r", "")
    l = l.replace(".", " ")
    l = l.replace(",", " ")
    l = l.replace(";", "")
    l = l.split(" ")
    for i in l:
        i = i.strip()
        if i != "": 
            first_list.append(i)
l = ""

for line in s.readlines():
    l = line.replace("\n", "")
    l = l.replace("\r", "")
    l = l.replace(".", " ")
    l = l.replace(",", " ")
    l = l.replace(";", "")
    l = l.split(" ")
    for i in l:
        i = i.strip()
        if i != "": 
            second_list.append(i)

f.close()
s.close()



print (SequenceMatcher(None, first_list, second_list).ratio())
#print (pearsonr(first_list,second_list))
#print (numpy.ma.corrcoef(first_list,second_list))