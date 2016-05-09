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

def work(x):
	x.MaxTryCount=重试次数;
execute(安居客核心流程.etls,lambda x:x.TypeName=='从爬虫转换',work)

##要跳过的页数，注意是翻页的数量
页数范围控制.Skip=0
##要获取的页数，可以设置的非常大，这样就一直会到末尾
页数范围控制.Take=20000000   



debug=True

if debug:
	get(安居客核心流程.etls,-2).Enabled=False
	get(安居客核心流程.etls,-1).Enabled=True



#是否要将完整的Json信息保存到数据库中
get(安居客核心流程.etls,-3).Enabled=False

#是否要保存相册？不论是否保存，都会将相册的路径存入数据库中
get(安居客相册.etls,-1).Enabled=True

#是否要保存户型图？不论是否保存，都会将户型图的路径存入数据库中
get(户型图存储.etls,-1).Enabled=True	
	
#要采集的城市，使用正则表达式，如果包含全部城市，则写为''
get(安居客城市.etls,-1).Script='常德|郴州承德|长治|池州|滁州|朝阳|潮州|楚雄|巢湖|昌都|长葛|崇左'
#户型图的存储路径
get(户型图存储方案.etls,-2).Format='E:\安居客图片\{0}\户型图\{1}_{2}_{3}.jpg'
#相册的存储路径
get(相册存储方案.etls,-2).Format='E:\安居客图片\{0}\相册\{1}_{2}_{3}.jpg'