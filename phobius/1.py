#coding:utf-8
'''
Created on 2016-1-15

@author: Mark
'''
import urllib
import urllib2
from bs4 import BeautifulSoup
import re
import string 
from time import sleep
import random
import string
from collections import Counter
import threading
from time import sleep,ctime
import cookielib
def findname(name):
    begin = name.find('|')
    end = name.rfind('|')
    return name[begin+1:end]
def randomUserAgent():
    p = random.randint(0,7)
    ans = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'User-Agent:Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',

        ]
    return ans[p]

def do(name,tmp,values,count,testlujing):  #  来具体的爬取  遇到问题sleep10秒钟然后重新爬取
                                      #  tmp是seq序列  values是表单  count表示个数  test路径表示存储的位置
    #print name,tmp
    try:
        cookies = cookielib.CookieJar()
        handler = urllib2.HTTPCookieProcessor(cookies)
        opener = urllib2.build_opener(handler)
        headers = {
            
            'User-Agent':randomUserAgent(),
        }

        url = 'http://phobius.sbc.su.se/cgi-bin/predict.pl'
        data = urllib.urlencode(values) 
        req = urllib2.Request(url, data,headers = headers)  
        response = opener.open(req)  # 下次加上超时处理
        the_page = response.read()
        #print the_page
        #########################################读取网页内容#############################
        #soup = BeautifulSoup(the_page,'html.parser')
        #print soup.find('pre').get_text()
        #  分类讨论  1   直接返回结果  2  返回job ID
        soup = BeautifulSoup(the_page,'html.parser')
        title = soup.find('title').get_text().split()
        while(title[0]=='Job'):
            if title[0] == 'Job':
                url = 'http://www.cbs.dtu.dk//cgi-bin/webface2.fcgi?jobid='+title[3]
                #print 'url',url
                req = urllib2.Request(url)
                sleep(3)
                response = urllib2.urlopen(req,timeout=10)  # 下次加上超时处理
                the_page = response.read()
                title = soup.find('title').get_text().split()
                #print the_page
                soup = BeautifulSoup(the_page,'html.parser') 
        if title[0] == 'Illegal':
            fp = open(testlujing,'a')
            fp.write('AC %d : %s\n    '%(count,name))
            fp.write('Input exceeded maximal number of residues for a given sequence : 5000')
            fp.close()
            return 
        answer1 = soup.find('pre') 
        answer2 = answer1.__str__()
        answer3 = answer2.split()    #  5,6,7,8   name  number number string
        #print answer3
        fp = open(testlujing,'a')
        fp.write('AC %d     '%count )
        #print answer3
        fp.write(answer3[5]+'    ') #'SEQENCE ID  
        fp.write(answer3[6]+'    ') #'TM'
        fp.write(answer3[7]+'    ') #'SP ='
        fp.write(answer3[8]+'    ') #'PREDICTION'
        fp.write('\n')
        fp.close()
        
    except Exception,e:
        sleep(10)
        print 'Soming is wrong'
        log = open('phobius--errorlog.txt','a')       # 将错误写进log文件
        log.write('WA   %d'%count+'retry\n'+tmp)
        log.write(str(e)+'\n'+tmp)
        log.close()
        do(name,tmp,values,count,testlujing)
    
def craw(fp,testlujing):              #选择fasta格式的蛋白质序列 ，并传给do（）函数来运行   fp是文件的指针
    tmp = ''
    count = 1
    name = ''
    #print fp
    tmp = fp.readline()
    for line in fp.readlines():
        #print line
        if '>sp' in line or '>tr' in line :
            values = {                     # 传入的表单
                    'format':'short',
                    'protseq':tmp,

                    }
            #threadslock.acquire()
            do(name,tmp,values,count,testlujing)
            print 'AC  %d'%count +'     is done      '+testlujing
            count = count + 1
            #threadslock.release()
            tmp = ''
        tmp = tmp + line

    
threadslock = threading.Lock()
def main(fileName,testlujing):
     #将filename作为参数出入。。
    print fileName,testlujing
    fp = open(fileName,'r')
    craw(fp,testlujing)      #  这！！！！！！！！！！！！！！！！！！！！！！！！！！路径没有传进去！！！！
    fp.close()
    
if __name__ == '__main__':
    
    threads = [] # 初始化线程

    for i in range(12,23):  # 定义线程
        fileName = 'C:\Users\Mark\Desktop\protein-fasta'+'\seq-%d.txt'%i
        testlujing = 'test-new-%d.txt'%i
        t = threading.Thread(
                target = main,
                args = (fileName,testlujing)
            )
        threads.append(t)

    for i in range(0,11): # 开始运行线程
        threads[i].start()

    for i in range(0,11):
        threads[i].join()

    print 'all work done at :',ctime()