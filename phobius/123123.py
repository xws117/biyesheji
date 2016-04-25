'''
Created on 2016-1-6

@author: Mark
'''
#coding:utf-8
import urllib  
import urllib2  
import bs4
import re
from bs4 import BeautifulSoup
import string

url = 'http://phobius.sbc.su.se/cgi-bin/predict.pl'  
fp2 = open('C:\Users\Mark\Desktop\uniport.fasta','r') # 778253
count = 1
seq = ''
for i in range(778254):
    line = fp2.readline()
    if '>tr' in line or '>sp' in line or line is None:
        if seq == '':
            seq = line
            continue
        
        values = {  
                    'format':'short',
                    'protseq':seq
                    }  
        try:
            #print seq
            data = urllib.urlencode(values) 
            req = urllib2.Request(url, data)  
            response = urllib2.urlopen(req)  
            the_page = response.read()
            soup = BeautifulSoup(the_page,'html.parser')
            answer1 = soup.find('pre') 
            answer2 = answer1.__str__()
            answer3 = answer2.split()    #  5,6,7,8   name  number number string
            print answer3
            fp = open('phobius--test.txt','a')
            fp.write('AC %d     '%count )
            fp.write(answer3[5]+'    ') #'SEQENCE ID  
            fp.write(answer3[6]+'    ') #'TM'
            fp.write(answer3[7]+'    ') #'SP ='
            fp.write(answer3[8]+'    ') #'PREDICTION'
            fp.write('\n')
            fp.close()
            print 'number %d:    '%count +'write is done'
            count = count + 1
        except Exception,ex:
            print 'number %d:    '%count +'write is failed'
            fp = open('test.txt','a')
            fp.write('WA %d    \n'%count)
            fp.close()
            count = count + 1 
            
        seq = line
        continue

    seq = seq + line
fp2.close()

