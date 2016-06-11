# coding=utf-8
##this script file works for project.xml
##教程.xml is just a example, it is easier but too simple to crawl target website.

def get(ar,index):
	l=len(ar);
	if index<0:
		return ar[l+index];
	else:
		return ar[index];
		
def find(ar,filter):
	for r in ar:
		if filter(r):
			return r;
	return None;

def execute(ar,filter,action):
	for r in ar:
		if filter(r):
			action(r);

#here you can edit city id 
#1:shanghai 2:beijing ...
#get more id from http://www.dianping.com/citylist
			
cityid='1'
类别.etls[0].Content=cityid;
区域.etls[0].Content=cityid;