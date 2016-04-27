#coding:utf-8
import urllib2
import urllib 
from bs4 import BeautifulSoup
import cookielib
import requests
from time import sleep
import random
import os
fp = open('K:\Tatp\jobid.txt','r')
count = 0
for line in fp.readlines():
	count = count + 1
	url = 'http://www.cbs.dtu.dk/cgi-bin/webface2.fcgi?jobid='+ line
	filepath = 'K:\Tatp\TatP---%d.txt'%count
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
		begin = content.find('<PRE>')
		end = content.rfind('//')
		if begin!=-1 and end!=-1:
			writefp = open(filepath,'w')
			writefp.write(content[begin:end])
			writefp.close()
			print 'find and write'
	else :
		print 'processing NO.%d ........'%count
		errorpath = 'K:\Tatp\error.txt'
		errorfp = open(errorpath,'a')
		errorfp.write("WA　　　　%d"%count+"　　　　"+line)
		errorfp.close()  
		print 'error' 
	
	