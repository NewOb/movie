# movie
vis forecast  

# 公用函数  
get_massage --获取用户表单输入信息  
get_color --获取电影类型统一配色表

# 后端文件结构 
config.py --配置文件  
exts.py --创建db用于建立数据库模型  
manage.py --用于写脚本命令 数据迁移  
models.py --数据库模型  
imdb_score_model.py --预测模型文件  
data.csv --预测模型参考文件  
app.py --主文件

# 前端主要文件说明
index.html --数据可视化页面  
gauge.js --仪表盘图  
zy_ball.js --结果波动图  
ball.js --结果波动图模板插件
d3.layout.cloud.js --词云图布局插件  
cloud.js --词云图

# 其他说明  
数据库字段名称可以在models.py文件下查找  
