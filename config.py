import pymysql
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/imdb?charset=utf8'

dbs = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='imdb')

SQLALCHEMY_TRACK_MODIFICATIONS=True

DEBUG = True