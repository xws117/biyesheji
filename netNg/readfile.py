#coding:utf-8
import urllib2
import urllib 
from bs4 import BeautifulSoup
import cookielib
import requests
from time import sleep
import random
import os
fp = open('K:\\netNg\jobid.txt','r')
count = 0
for line in fp.readlines():
	count = count + 1
	url = 'http://www.cbs.dtu.dk/cgi-bin/webface2.fcgi?jobid='+ line
	filepath = 'K:\\netNg\\netNg---%d.txt'%count
	if os.path.exists(filepath):
		print '%d.txt----file is exits'%count
		continue
	req = urllib2.Request(url)
	responce = urllib2.urlopen(req, timeout=20)
	the_page = responce.read()
	print the_page 
	print url
	soup = BeautifulSoup(the_page,'html.parser')
	if soup.find('title').get_text().find('results'):
		print 'processing NO.%d ........'%count
		content = the_page
		writefp = open(filepath,'w')
		writefp.write(content)
		writefp.close()
		print 'find and write'
	else :
		print 'processing NO.%d ........'%count
		errorpath = 'K:\\netNg\error.txt'
		errorfp = open(errorpath,'a')
		errorfp.write("WA　　　　%d"%count+"　　　　"+line)
		errorfp.close()  
		print 'error' 
	
	