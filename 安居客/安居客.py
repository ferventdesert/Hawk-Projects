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

	
unabled=[户型图存储方案,户型图存储,安居客户型列表,安居客评价,安居客楼盘详情,相册存储方案,安居客相册];
for e in unabled:
	e.etls[0].Enabled=False

页数范围控制=find(安居客核心流程.etls,lambda x:x.TypeName=='数量范围选择')

#下面是可能需要修改的配置:
###################################################

重试次数='3'



##要跳过的页数，注意是翻页的数量
页数范围控制.Skip=0
##要获取的页数，可以设置的非常大，这样就一直会到末尾
页数范围控制.Take=20000000   

debug=False

#是否要进行增量抓取？
#注意：系统会在数据库里查询是否已有数据，因此可能会造成在调试时，没有任何数据显示（所有的数据都在数据库里了）
#如果无所谓重复，或为了调试观察，则
not_repeat=True

def work2(x):
	x.Enabled=not_repeat;

def work(x):
	x.MaxTryCount=重试次数;
	
execute(安居客核心流程.etls,lambda x:x.TypeName=='从爬虫转换',work)
execute(安居客核心流程.etls,lambda x:x.Name=='防重复',work2)
execute(安居客核心流程.etls,lambda x:x.TypeName=='从爬虫转换',work)



get(安居客核心流程.etls,-2).Enabled=not debug;


#是否要将完整的Json信息保存到数据库中
get(安居客核心流程.etls,-3).Enabled=False

#是否要保存相册？不论是否保存，都会将相册的路径存入数据库中
get(安居客相册.etls,-1).Enabled=True
 
#是否要保存户型图？不论是否保存，都会将户型图的路径存入数据库中
get(户型图存储.etls,-1).Enabled=True
	
#要采集的城市，使用正则表达式，如果包含全部城市，则写为''
get(安居客城市.etls,-1).Script='锦州|景德镇|吉安|济宁|金华|揭阳|晋中|九江|焦作|晋城|荆州|佳木斯|酒泉|鸡西|济源|金昌|嘉峪关'
#户型图的存储路径
get(户型图存储方案.etls,-4).Format='D:\安居客图片\{0}\户型图\{1}_{2}_{3}.jpg'
#相册的存储路径
get(相册存储方案.etls,-4).Format='D:\安居客图片\{0}\相册\{1}_{2}_{3}.jpg'