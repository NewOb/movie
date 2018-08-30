import pymysql
import csv

db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='imdb')
cursor = db.cursor()
'''只需更改以下变量的初值即可，功能是将折线数据放入line_data.csv中，多余的函数已注释掉 '''

'''折线图数据处理，更改起点'''
table = 'xl'  # 表名
file_name = 'line_data.csv'  # 保存的文件路径
# 记：电影类型【】要么通过 电影名 查找数据库得到，要么直接从输入框中得到
film_type_list = ['Action', 'Drama']  # 电影类型list
''' 更改终点'''

field_type_name = 'type'  # 表中 类型 对应字段名字
field_time_name = 'years'  # 表中 时间 对应字段名字
field_grade_name = 'IMDB'  # 表中 评分 对应字段名字
field_box_office_name = 'Box_office'  # 表中 票房 对应字段名字

# 记录该函数执行次数，用于清空文件和标记字段写入，不用改
query_grade_cout = 0



# '''查询包含模糊字符串的记录,并写入type.csv文件'''
# '''field 字段名，param 模糊参数'''
# def query(field, param):
#     sql = 'SELECT * FROM `{table}` WHERE `{field}` LIKE "{param}" LIMIT 0, 4000' \
#         .format(table=table, field=field, param=param)
#     try:
#         row_number = cursor.execute(sql)
#         description = [i[0] for i in cursor.description]
#         with open('data/type.csv', 'w', newline='')as csvfile:
#             writer = csv.writer(csvfile, delimiter=',')
#             writer.writerow(description)
#             while row_number:
#                 row = cursor.fetchone()
#                 writer.writerow(list(row))
#                 row_number = row_number - 1
#     except IOError as e:
#         print(e)


# query(field_type_name, param='%Action%')

# '''查询 field字段 类型种类，返回列表'''

#
# def query_type(field):
#     sql = 'SELECT `{field}` FROM `{table}`'.format(field=field, table=table)
#     row_number = cursor.execute(sql)
#     setObject = set()
#     while row_number:
#         row = cursor.fetchone()
#         str = "".join(row)
#         arr = str.split('|')
#         for i in arr:
#             setObject.add(i)
#         row_number = row_number - 1
#     return list(setObject)


# a = query_type(field_type_name)
# print(a, len(a))


''' 查询某一类型电影的时间和评分，将类型，时间，评分（根据时间分组求平均）写入file_name文件 '''

def query_grade_ticket(film_type):
    sql = 'select "{film_type}" as `{field_type_name}`,`{field_time_name}`,round(avg(`{field_grade_name}`),2)`{field_grade_name}`,round(avg(`{field_box_office_name}`),0)`{field_box_office_name}` ' \
          'from (SELECT  `{field_type_name}`,`{field_time_name}`,`{field_grade_name}`,`{field_box_office_name}` FROM `{table}` WHERE `{field_type_name}` ' \
          'LIKE "%{film_type}%" LIMIT 0, 4000 )as new group by `{field_time_name}` order by `{field_time_name}`' \
        .format(field_type_name=field_type_name, film_type=film_type, field_time_name=field_time_name,
                field_grade_name=field_grade_name,
                field_box_office_name=field_box_office_name, table=table)
    try:
        row_number = cursor.execute(sql)
        description = [i[0] for i in cursor.description]
        global query_grade_cout
        if query_grade_cout == 0:
            with open(file_name, 'w')as f:
                f.write('')
        with open(file_name, 'a', newline='')as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            if query_grade_cout == 0:  # csvfile.truncate();不能清空
                query_grade_cout = query_grade_cout + 1
                writer.writerow(description)
            while row_number:
                row = cursor.fetchone()
                writer.writerow(list(row))
                row_number = row_number - 1
    except IOError as e:
        print(e)


'''参数电影类型list，将每个类型的数据存入评分csv'''


def store_score_data(file_type_list=[]):
    for item in file_type_list:
        query_grade_ticket(item)
    global query_grade_cout
    query_grade_cout = 0


store_score_data(film_type_list)
