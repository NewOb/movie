import pymysql
import json
from config import dbs as db
# db = pymysql.connect(host='localhost', user='root', password='Hhgj9bjt', port=3306, db='grade')
cursor = db.cursor()

''' 生成子弹图数据,存入文件，只需更改以下变量名为对应的数据库中表的字段名，以及关键变量的值；
文件末行均为运行函数；
子弹图说明：'''

''' 查找电影对应的年份'''

'''更改区 起点'''
table = 'xl'  # 表名
film_name = 'Ride Along 2?'  # 电影的名字
storage_file = 'static/data/bullet_data.json'  # 子弹图数据文件
'''更改区 终点'''


field_film_name = 'name'  # 电影名字 字段的名字
field_time_name = 'years'  # 电影年份 字段的名字
field_box_office_name = 'Box_office'  # 电影票房 字段的名字

rates_type = ['NC-17', 'X', 'R', 'M', 'GP', 'PG', 'PG-13', 'Unrated', 'Not Rated', 'Passed', 'Approved', 'G']  # 评级排序
# 电影时长，投资金额，想看人数，内容评级范围,及该字段的名字
# all_range = [[90, 120, 330], [30000000, 80000000, 12215500000], [1000, 26000, 349000], [4, 8, 11]]
all_range = 0
current_year = 0  # 该电影的年份
all_name = ['time', 'invest', 'film_fb_like', 'level']

'''根据电影名字查找某一字段的值'''


def search_field_value(field_name):
    sql = 'SELECT `{field_name}` FROM `{table}` WHERE `{field_film_name}` = "{film_name}"' \
        .format(field_name=field_name, table=table, field_film_name=field_film_name, film_name=film_name)
    print(sql)
    cursor.execute(sql)
    return cursor.fetchone()[0]


current_year = int(search_field_value(field_time_name))
min_year = 0
max_year = 0
'''search [min_year,max_year] of data '''


def search_interval():
    global min_year, max_year
    if current_year - 5 < 1927:
        min_year = 1927
    else:
        min_year = current_year - 5
    if current_year + 5 > 2016:
        max_year = 2016
    else:
        max_year = current_year + 5
    return 'SELECT * FROM(SELECT* FROM {table} WHERE {field_time_name} BETWEEN {min_year} AND {max_year} ' \
           'ORDER BY {field_box_office_name} + 0 DESC ) AS new'.format(table=table, field_time_name=field_time_name,
                                                                       min_year=min_year, max_year=max_year,
                                                                       field_box_office_name=field_box_office_name)


# 查询某一段时间内数据并按照票房排序的sql语句；
interval_data_sql = search_interval()

''' #返回范围区间'''


# select_num   选择票房排序前select_num的数据
def return_greate_interval(field_name, select_num):
    select_num = int(select_num)
    sql = 'SET @rank = 0;'
    sql_1 = 'SELECT MAX({field_name}+0),MIN({field_name}+0)FROM( SELECT * ,@rank :=@rank + 1 AS num FROM ( ' \
            'SELECT * FROM {table} WHERE {field_time_name} BETWEEN {min_year} AND {max_year} ORDER BY {field_name} + 0 DESC ) ' \
            'AS new WHERE @rank<{select_num})AS newtwo '.format(field_name=field_name, table=table,
                                                                field_time_name=field_time_name,
                                                                select_num=select_num, min_year=min_year,
                                                                max_year=max_year)
    cursor.execute(sql)
    cursor.execute(sql_1)
    result = list(cursor.fetchone())
    return result


# print(return_greate_interval('boxOffice', 20))
''':return  three range list'''


def interval_range():
    sql = 'SELECT COUNT(*),MAX({field_name_1}+0),MAX({field_name_2}+0),MAX({field_name_3}+0)' \
          ' FROM {table} WHERE {field_time_name} BETWEEN {min_year} AND {max_year}' \
        .format(table=table, field_time_name=field_time_name, min_year=min_year, max_year=max_year,
                field_name_1=all_name[0], field_name_2=all_name[1], field_name_3=all_name[2])
    cursor.execute(sql)
    temp_arr = list(cursor.fetchall()[0])
    temp_num = temp_arr[0] * 0.9
    temp_list = []
    for field_name in all_name:
        temp_index = all_name.index(field_name)
        if temp_index == 3:
            break
        else:
            temp_variable = list(return_greate_interval(field_name, temp_num))
            temp_variable.append(int(temp_arr[temp_index + 1]))
            temp_variable.sort()
            temp_list.append(temp_variable)
    temp_list.append([4, 8, 11])
    return temp_list


# print(interval_range())
all_range = interval_range()

'''返回平均值函数'''


def return_avg(field_name):
    sql = 'select round(avg({field_name}+0),2)`{field_name}` from ({table})as newone' \
        .format(field_name=field_name, table=interval_data_sql)
    print(sql)
    cursor.execute(sql)
    return float(cursor.fetchone()[0])


# print(return_avg('filmLikeNumber'))

'''return [当前年份的值,该年的最大值] '''


def internal_content(field_name):
    # 当前值
    param_1 = int(search_field_value(field_name))
    sql = 'select MAX({field_name}+0) from {table} where {field_time_name}={current_year}' \
        .format(field_name=field_name, table=table, field_time_name=field_time_name, current_year=current_year)
    print(sql)
    cursor.execute(sql)
    param_2 = cursor.fetchone()[0]
    return [param_1, param_2]


# print(internal_content(field_name))        #bug

''' 查找电影评级字段field_name=‘rate’ 
return [[当前电影评级，和该年最大值],平均值]'''


# from  decimal import Decimal
# from  decimal import getcontext
def deal_rate(field_name):
    name = search_field_value(field_name)
    current_value = rates_type.index(name)
    rate_list = []
    for item in rates_type:
        rate_list.append(" when " + "'" + item.__str__() + "'" + " then " + rates_type.index(item).__str__() + " ")
    sql_arg_str = "".join(rate_list)
    sql = 'select Max({field_name}+0)from (select (case {field_name}{sql_arg_str} end){field_name} from (select {field_name} ' \
          'from {table} where {field_time_name}={current_year})as new1)as new' \
        .format(field_name=field_name, sql_arg_str=sql_arg_str, table=table,
                field_time_name=field_time_name, current_year=current_year)
    cursor.execute(sql)
    max_value = cursor.fetchone()[0]
    sql_avg = 'select round(avg({field_name}+0),2) from (select (case {field_name}{sql_arg_str} end){field_name} ' \
              'from {table})as new'.format(field_name=field_name, sql_arg_str=sql_arg_str, table=table)
    print(sql_avg)
    cursor.execute(sql_avg)
    value_avg = float(cursor.fetchone()[0])
    return [[current_value, max_value], value_avg]


# print(deal_rate('rate'))

''' 查找某一列最大值'''


def search_max(field_name):
    sql = 'select MAX({field_name}+0) from {table} limit 0,4000'.format(field_name=field_name, table=table)
    cursor.execute(sql)
    return cursor.fetchone()[0]


# print(search_max('filmLikeNumber'))
''' 返回[ [[a,b,c],[当前，最大值]，均值], [] ...]，所有数据'''


def pack_data():
    arr_list = []
    arr_1 = ["film's length", 'investment amount', 'number of people', 'Content rating']
    # arr_1 = ["电影时长", "投资金额", "想看人数", "内容评级"]
    arr_2 = ['minutes', '$ dollar', 'count', 'rank']
    for item in all_range:
        f_index = all_range.index(item)
        if all_range.index(item) == 3:
            arr_list.append(
                [arr_1[f_index], arr_2[f_index], item, deal_rate(all_name[3])[0], [deal_rate(all_name[3])[1]]])
            break
        arg_2 = internal_content(all_name[f_index])
        arg_3 = return_avg(all_name[f_index])
        arr_list.append([arr_1[f_index], arr_2[f_index], item, arg_2, [arg_3]])
    return arr_list


# csv 格式写入，不适用，舍弃
# def assemble_data():
#     description=['title','subtitle','ranges','practical','average']
#     with open(storage_file, 'a',encoding='utf-8',newline='')as csvfile:
#         writer = csv.writer(csvfile, delimiter=',')
#         writer.writerow(description)
#         for item in pack_data():
#             writer.writerow(item)
# assemble_data()

'''json 文件格式存储'''


def storage_json(film_name_arg):
    global film_name
    film_name=film_name_arg

    description = ['title', 'subtitle', 'ranges', 'practical', 'average']
    arr = pack_data()
    json_data = []
    with open(storage_file, 'w', newline='')as f:
        for i in all_name:
            data = {}
            for j in description:
                data[j] = arr[all_name.index(i)][description.index(j)]
            json_data.append(data)
        print(json_data)
        json.dump(json_data, f)
        f.close()

