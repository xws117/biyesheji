#coding:utf-8
import urllib2
import urllib 
from bs4 import BeautifulSoup
import cookielib
import requests
from time import sleep
import random
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
for k in range(23,30):
    try:
        headers = {
        'Referer':'http://www.cbs.dtu.dk/services/NetNGlyc/',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'User-Agent':randomUserAgent(),
        'Cookie':'__utma=151498347.1130369555.1452513773.1452567626.1452579854.5; __utmz=151498347.1452513773.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=151498347; __utmb=151498347.1.10.1452579854; __utmt=1',
        'Connection':'keep-alive',
        'Host':'www.cbs.dtu.dk',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        }
        openfile = 'C:\Users\Mark\Desktop\wenjian\seq-%d.fasta'%(k+1)
        url = 'http://www.cbs.dtu.dk/cgi-bin/webface2.fcgi'
        files={'configfile':(None,'/usr/opt/www/pub/CBS/services/NetNGlyc-1.0/NetNGlyc.cf'),
            'SEQPASTE':(None,''),
            'SEQSUB':('seq-%d.fasta'%(k+1),open(openfile,'rb'),'application/octet-stream'),

         }
        response=requests.post(url,files=files,headers = headers)
        ans = response.text
        soup = BeautifulSoup(ans,'html.parser')
        sleeptime = 5
        print 'seq--%d'%(k+1)+' is running'
        jobid = soup.find('h1').get_text().split()[2]
        print 'jobid ==   '+jobid
        new_url = 'http://www.cbs.dtu.dk//cgi-bin/webface2.fcgi?jobid='+soup.find('h1').get_text().split()[2]
        new_url = new_url + '&email=1179066213%40qq.com&wait=20&submit=Send+email'
        sleep(sleeptime)
        haha = requests.get(new_url)
        if haha.text.find('1179066213@qq')!=-1:
            print 'find 1179066213  true'
            fp = open('K:\\netNg\jobid.txt','a')
            fp.write(jobid)
            fp.write('\n')
            fp.close()
            print 'seq-----%d'%(k+1)+'    is  ok'

        
    except Exception,e:
        print str(e)
        print 'seq--%d is wrong '%(k+1)

    