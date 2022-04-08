#徐琪 
#2020.4.7

'''
单进程运行，时间久，预计大概66小时左右
import requests
from urllib.request import urlopen
from multiprocessing import Pool
import time
import urllib.request
import re
from requests_html import HTMLSession

file=open('d:\\1.txt')
file2=open('D:\\test.txt','w')
i=0
for line in file.readlines():
    i=i+1
    line=line.strip('\n')
    url='https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids='+str(line)
    data=urllib.request.urlopen(url).read()
    data=data.decode("utf-8")  
    file2.write(data)
    print(i)
file2.close()

'''

'''
多进程，速度快，缺点是会丢失大量数据，需要不断利用excel寻找遗漏的数据，大概3轮左右即可得到完整数据。时间大概6小时

import time
import requests
from concurrent import futures
import requests
from urllib.request import urlopen
import urllib3
from multiprocessing import Pool
import time
import requests
import urllib.request
import re

file=open('e:\\uid.txt')
pmid=file.readlines()
file2=open('e:\\test.txt','a')#数据信息
file3=open('e:\\use.txt','a')#追加写入，处理过的uid
def get_data1(url):
    data=urllib.request.urlopen(url).read()#获取网站的信息
    data=data.decode("utf-8")
    file2.write(data)#写入文件中
    file3.write(url)#保存记录的uid号，因为在并行中会遗漏一些数据，所以保存下已经处理的uid号，之后在excel中找出未被处理的uid号并再次处理
    return 1

def get_url1():#这个函数代码借鉴了黄紫嫣学姐等人的代码，主要是让我写也就这么写，实在没有重写和优化的必要了
    url_list=[]
    for i in pmid:
        url='https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/pubtator?pmids='+str(i)
        url_list.append(url)
    return url_list

s=time.time()
urls=get_url1()
executor = futures.ThreadPoolExecutor(max_workers=10)#数字越大处理越快，不过遗漏的信息就越多。比如100线程时会遗漏50%的信息，10线程时大概会遗漏5%的信息
fs=[]
for url in urls:
    f=executor.submit(get_data1, url)#提交到多线程池里
    fs.append(f)
    
futures.wait(fs)
print(time.time()-s)#等待处理结束，并提醒程序已经结束了

'''

'''

excel辅助多进程处理
使用countif函数即可，sumif函数也可以使用，在此不赘述、

'''
