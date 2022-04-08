import requests
from urllib.request import urlopen
from multiprocessing import Pool
import time
import urllib.request
import re
from requests_html import HTMLSession

file2=open('e:\\r\\18.txt')
disease=open('e:\\disease.txt','a')#因为有多份数据，所以要不断追加书写
gene=open('e:\\gene.txt','a')
chemical=open('e:\\chemical.txt','a')
mutation=open('e:\\mutation.txt','a')
species=open('e:\\species.txt','a')
cellline=open('e:\\cellline.txt','a')
zy=open('e:\\zy.txt','a')

Species = re.compile('Species'+'\t')#正则表达，提取信息
Disease = re.compile('Disease'+'\t')
Chemical = re.compile('Chemical'+'\t')
Mutation = re.compile('Mutation'+'\t')
Gene = re.compile('Gene'+'\t')
Cellline = re.compile('Cellline'+'\t')

for line in file2.readlines():
    if(re.search(Species, line, flags=0)):
        species.write(line)
    elif(re.search(Disease, line, flags=0)):
        disease.write(line)
    elif(re.search(Chemical, line, flags=0)):
        chemical.write(line)
    elif(re.search(Mutation, line, flags=0)):
        mutation.write(line)
    elif(re.search(Gene, line, flags=0)):
        gene.write(line)
    elif(re.search(Cellline, line, flags=0)):
        cellline.write(line)
    else:
        zy.write(line)
    
disease.close()
gene.close()
chemical.close()
mutation.close()
species.close()
cellline.close()
zy.close()