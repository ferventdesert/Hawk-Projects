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
def disable(etl):
	etl.Enabled=False;




照片数量控制=find(相册.etls,lambda x:x.TypeName=='数量范围选择')
execute(相册.etls,lambda x:x.Name=='测试',disable)

#########下面是正式配置文件
#是否要抓取图片？
get(主流程.etls,-1).Enabled=True;

#将相册表保存起来吗？
get(相册.etls,-1).Enabled=True;

#每个女郎最多抓取多少张照片
照片数量控制.Take=1000

#照片保存路径
path='D:\淘女郎'



find(相册.etls,lambda x:x.Name=='图片位置').NewValue=path;


#保存大图吗？False则只保存小图
find(相册.etls,lambda x:x.Name=='大图').Enabled=True
