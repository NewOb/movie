from exts import db

class xunlian(db.Model):
    __tablename__='xl'
    name= db.Column(db.String(255), primary_key=True)  #电影名称
    years= db.Column(db.String(255))                   #电影年份
    director= db.Column(db.String(255))                #导演
    country= db.Column(db.String(255))                 #国家
    language= db.Column(db.String(255))                #语言
    invest= db.Column(db.String(255))                  #投资
    type= db.Column(db.String(255))                    #类型
    key_words= db.Column(db.String(255))               #剧情关键字
    screen= db.Column(db.String(255))                  #屏幕比例
    face= db.Column(db.String(255))                    #海报中出现的面孔数
    dir_like= db.Column(db.String(255))                #导演点赞量
    time = db.Column(db.String(255))                   #电影时常
    color= db.Column(db.String(255))                   #色彩
    level= db.Column(db.String(255))                   #级别
    act_one= db.Column(db.String(255))                 #演员1
    act_one_like=db.Column(db.String(255))             #演员1的点赞量
    act_two= db.Column(db.String(255))                 #演员2
    act_two_like= db.Column(db.String(255))            #演员2的点赞量
    act_three= db.Column(db.String(255))               #演员3
    act_three_like= db.Column(db.String(255))          #演员3的点赞量
    act_all_like= db.Column(db.String(255))            #全部演员的点赞量
    like_all= db.Column(db.String(255))                #电影的点赞量
    pro_review=db.Column(db.String(255))               #专业评论数
    user_review=db.Column(db.String(255))              #用户评论数
    film_fb_like=db.Column(db.String(255))             #电影在facebook上的点赞量
    IMDB=db.Column(db.String(255))                     #imdb评分
    Box_office=db.Column(db.String(255))               #票房
    link=db.Column(db.String(255))                     #连接
