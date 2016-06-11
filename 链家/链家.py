# coding=utf-8
#下面的代码是接口函数，无关
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

	




#下面是可能需要修改的配置:
###################################################

#修改城市缩写

get(链家二手房清洗.etls,0).Content='su'

#如果照片已经存在，则直接跳过
#修改路径 {0}:二手房ID, 1：city, 2:照片id
get(照片抓取流程.etls,-2).Format='D:\链家二手房\{1}\{0}-{2}.jpg'


##下面不是配置文件


照片选择逻辑=	find(照片抓取流程.etls,lambda x:x.TypeName=='从爬虫转换');
if(get(链家二手房清洗.etls,0).Content=='bj'):
	照片选择逻辑.CrawlerSelector='照片抓取'
else:
	照片选择逻辑.CrawlerSelector='照片抓取2'

