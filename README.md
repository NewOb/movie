# movie
vis forecast  

# 后端文件结构 
config --配置文件  
exts --创建db用于建立数据库模型  
manage --用于写脚本命令 数据迁移  
models --数据库模型  
imdb_score_model --预测模型文件  
data.csv --预测模型参考文件  
IMDB --主文件


# 后端数据说明
l_type --词云图数据 *url:'/l_data/'*  
d_type --结果波动图数据 *url:'/data/'*  
lists --预测模型输入列表 *url:'/'*  
fin_data --词云图交互数据 *url:'/cloud_rect'*  
table_massage --用户输入的信息 *接收url:'/' 返回url:'/massage/'*  
table_massage为字典型数据，其他数据均为列表型数据，列表里的元素为字典。


#前端主要文件说明
tabs.html --用户输入表单页面  
index.html --数据可视化页面  
gauge.js --仪表盘图  
d_ball.js --结果波动图  
ball.js --结果波动图模板插件
d3.layout.cloud.js --词云图布局插件  
cloud.js --词云图

#其他说明  
数据库字段名称可以在models.py文件下查找  
