from flask import Flask, render_template, request, jsonify, url_for, redirect
from config import dbs
import line
from line import store_score_data
from flask_sqlalchemy import SQLAlchemy
import config
from imdb_score_model import Create_score_model, Type_conversion
import langid
import csv
from models import xunlian
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

table_massage = {}

l_type = [{'en': 'Comedy', 'zh': '喜剧', 'like': 0, 'Color': '#178BCA'},
          {'en': 'Adventure', 'zh': '冒险', 'like': 0, 'Color': '#CDAA7D'},
          {'en': 'Fantasy', 'zh': '幻想', 'like': 0, 'Color': '#008B00'},
          {'en': 'Mystery', 'zh': '悬念', 'like': 0, 'Color': '#9ACD32'},
          {'en': 'Thriller', 'zh': '惊悚', 'like': 0, 'Color': '#8EE5EE'},
          {'en': 'Documentary', 'zh': '记录', 'like': 0, 'Color': '#AA7D39'},
          {'en': 'War', 'zh': '战争', 'like': 0, 'Color': '#696969'},
          {'en': 'Western', 'zh': '西部', 'like': 0, 'Color': '#DB7093'},
          {'en': 'Romance', 'zh': '爱情', 'like': 0, 'Color': '#FF8C00'},
          {'en': 'Drama', 'zh': '剧情', 'like': 0, 'Color': '#20B2AA'},
          {'en': 'Horror', 'zh': '恐怖', 'like': 0, 'Color': '#000000'},
          {'en': 'Action', 'zh': '动作', 'like': 0, 'Color': '#CD2626'},
          {'en': 'Sci-Fi', 'zh': '科幻', 'like': 0, 'Color': '#FFD700'},
          {'en': 'Music', 'zh': '音乐', 'like': 0, 'Color': '#9932CC'},
          {'en': 'Family', 'zh': '家庭', 'like': 0, 'Color': '#CD96CD'},
          {'en': 'Crime', 'zh': '犯罪', 'like': 0, 'Color': '#CCCC33'},
          ]

d_type = [
    {'en': 'Action', 'zh': '动作', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#CD2626',
     'textColor': '#8B1A1A', 'waveTextColor': '#FFFAFA', 'waveColor': '#CD2626'},
    {'en': 'Adventure', 'zh': '冒险', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#CDAA7D',
     'textColor': '#8B7E66', 'waveTextColor': '#EED8AE', 'waveColor': '#CDAA7D'},
    {'en': 'Comedy', 'zh': '喜剧', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#178BCA',
     'textColor': '#045681', 'waveTextColor': '#A4DBf8', 'waveColor': '#178BCA'},
    {'en': 'Fantasy', 'zh': '幻想', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#008B00',
     'textColor': '#006400', 'waveTextColor': '#9AFF9A', 'waveColor': '#008B00'},
    {'en': 'Mystery', 'zh': '悬念', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#9ACD32',
     'textColor': '#458B00', 'waveTextColor': '#FFFFE0', 'waveColor': '#9ACD32'},
    {'en': 'Thriller', 'zh': '惊悚', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#8EE5EE',
     'textColor': '#00868B', 'waveTextColor': '#FFFAFA', 'waveColor': '#8EE5EE'},
    {'en': 'Documentary', 'zh': '记录', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#AA7D39',
     'textColor': '#8B4500', 'waveTextColor': '#D4AB6A', 'waveColor': '#AA7D39'},
    {'en': 'War', 'zh': '战争', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#696969',
     'textColor': '#000000', 'waveTextColor': '#FFFAFA', 'waveColor': '#696969'},
    {'en': 'Western', 'zh': '西部', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#DB7093',
     'textColor': '#B03060', 'waveTextColor': '#FFE4E1', 'waveColor': '#DB7093'},
    {'en': 'Romance', 'zh': '爱情', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#FF8C00',
     'textColor': '#CD661D', 'waveTextColor': '#FFDEAD', 'waveColor': '#FF8C00'},
    {'en': 'Drama', 'zh': '剧情', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#20B2AA',
     'textColor': '#668B8B', 'waveTextColor': '#B0E0E6', 'waveColor': '#20B2AA'},
    {'en': 'Horror', 'zh': '恐怖', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#000000',
     'textColor': '#000000', 'waveTextColor': '#BEBEBE', 'waveColor': '#000000'},
    {'en': 'Sci-Fi', 'zh': '科幻', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#FFD700',
     'textColor': '#8B7500', 'waveTextColor': '#FFFAFA', 'waveColor': '#FFD700'},
    {'en': 'Music', 'zh': '音乐', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#9932CC',
     'textColor': '#551A8B', 'waveTextColor': '#D8BFD8', 'waveColor': '#9932CC'},
    {'en': 'Family', 'zh': '家庭', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#CD96CD',
     'textColor': '#68228B', 'waveTextColor': '#FFFAFA', 'waveColor': '#CD96CD'},
    {'en': 'Crime', 'zh': '犯罪', 'like': 0, 'money_max': 0, 'money_min': 0, 'circleColor': '#CCCC33',
     'textColor': '#556B2F', 'waveTextColor': '#FFFAFA', 'waveColor': '#CCCC33'},
]

lists = []


@app.route('/l_data/', methods=['GET'])
def l_data():
    # com = adv = fan = mys = thr = doc = war = wes = rom = dra = hor = act = sci = mus = fam = cri = 0
    # mytype = []
    ALL = xunlian.query.all()
    while len(ALL) > 0:
        dataset = ALL.pop()
        types = dataset.type.split("|")
        like = dataset.like_all
        if like == '':
            like = 0
        # print(like)
        like = int(like)
        # print(type(like))
        # print(repr(like))
        while len(types):
            count = types.pop()
            if count == l_type[0]["en"]:
                l_type[0]["like"] += like
                l_type[0]["like"] /= 2
            elif count == l_type[1]["en"]:
                l_type[1]["like"] += like
                l_type[1]["like"] /= 2
            elif count == l_type[2]["en"]:
                l_type[2]["like"] += like
                l_type[2]["like"] /= 2
            elif count == l_type[3]["en"]:
                l_type[3]["like"] += like
                l_type[3]["like"] /= 2
            elif count == l_type[4]["en"]:
                l_type[4]["like"] += like
                l_type[4]["like"] /= 2
            elif count == l_type[5]["en"]:
                l_type[5]["like"] += like
                l_type[5]["like"] /= 2
            elif count == l_type[6]["en"]:
                l_type[6]["like"] += like
                l_type[6]["like"] /= 2
            elif count == l_type[7]["en"]:
                l_type[7]["like"] += like
                l_type[7]["like"] /= 2
            elif count == l_type[8]["en"]:
                l_type[8]["like"] += like
                l_type[8]["like"] /= 2
            elif count == l_type[9]["en"]:
                l_type[9]["like"] += like
                l_type[9]["like"] /= 2
            elif count == l_type[10]["en"]:
                l_type[10]["like"] += like
                l_type[10]["like"] /= 2
            elif count == l_type[11]["en"]:
                l_type[11]["like"] += like
                l_type[11]["like"] /= 2
            elif count == l_type[12]["en"]:
                l_type[12]["like"] += like
                l_type[12]["like"] /= 2
            elif count == l_type[13]["en"]:
                l_type[13]["like"] += like
                l_type[13]["like"] /= 2
            elif count == l_type[14]["en"]:
                l_type[14]["like"] += like
                l_type[14]["like"] /= 2
            elif count == l_type[15]["en"]:
                l_type[15]["like"] += like
                l_type[15]["like"] /= 2

    # d_type[0]["like"] = com
    # fin = xunlian.query.all()
    # FinCloud = []
    #
    # while len(fin) > 0:
    #     clouds = fin.pop()
    #     d_type['type'] = clouds.type
    #     FinCloud.append(cloud)
    #     all_data = {}
    # print(table_massage)
    # print(table_massage['type'])
    l_type.append(table_massage['type'])
    # print(jsonify(d_type[0]['en']))
    return jsonify(l_type)

@app.route('/s_bullet/',methods=['GET'])
def bullet():
    cursor = dbs.cursor()

    table = 'xl'  # 表名
    film_name = 'Ride Along 2?'  # 电影的名字
    # storage_file = 'data/bullet_data.json'  # 子弹图数据文件
    '''更改区 终点'''

    field_film_name = 'name'  # 电影名字 字段的名字
    field_time_name = 'years'  # 电影年份 字段的名字
    field_box_office_name = 'Box_office'  # 电影票房 字段的名字

    rates_type = ['NC-17', 'X', 'R', 'M', 'GP', 'PG', 'PG-13', 'Unrated', 'Not Rated', 'Passed', 'Approved',
                  'G']  # 评级排序
    # 电影时长，投资金额，想看人数，内容评级范围,及该字段的名字
    # all_range = [[90, 120, 330], [30000000, 80000000, 12215500000], [1000, 26000, 349000], [4, 8, 11]]
    all_range = 0
    current_year = 0  # 该电影的年份
    all_name = ['time', 'invest', 'like_all', 'level']

    '''根据电影名字查找某一字段的值'''

    # ------------------

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
        print(temp_arr)
        temp_num = temp_arr[0] * 0.9
        temp_list = []
        for field_name in all_name:
            temp_index = all_name.index(field_name)
            if temp_index == 3:
                break
            else:
                temp_variable = list(return_greate_interval(field_name, temp_num))
                print(temp_index)
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

    print(return_avg('filmLikeNumber'))

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

    def storage_json():
        description = ['title', 'subtitle', 'ranges', 'practical', 'average']
        arr = pack_data()
        json_data = []
        for i in all_name:
            data = {}
            for j in description:
                data[j] = arr[all_name.index(i)][description.index(j)]
            json_data.append(data)
        print(json_data)
        return jsonify(json_data)
    storage_json()


@app.route('/data/', methods=['GET'])
def data():
    ALL = xunlian.query.all()
    money_adv = []
    money_com = []
    money_fan = []
    money_mys = []
    money_thr = []
    money_doc = []
    money_war = []
    money_wes = []
    money_rom = []
    money_dra = []
    money_hor = []
    money_act = []
    money_sci = []
    money_mus = []
    money_fam = []
    money_cri = []

    grade_adv = []
    grade_com = []
    grade_fan = []
    grade_mys = []
    grade_thr = []
    grade_doc = []
    grade_war = []
    grade_wes = []
    grade_rom = []
    grade_dra = []
    grade_hor = []
    grade_act = []
    grade_sci = []
    grade_mus = []
    grade_fam = []
    grade_cri = []


    while len(ALL) > 0:
        dataset = ALL.pop()
        types = dataset.type.split("|")  # 字段拆分
        like = dataset.like_all
        money = dataset.Box_office
        grade = dataset.IMDB
        if like == '':
            like = 0

        if money == '':
            money = 0

        if grade == '':
            grade = 0

        like = int(like)
        money = int(money)
        # grade=int(grade)

        while len(types):
            count = types.pop()
            if count == d_type[0]["en"]:
                d_type[0]["like"] += like
                money_adv.append(money)
                grade_adv.append(grade)
            elif count == d_type[1]["en"]:
                d_type[1]["like"] += like
                money_com.append(money)
                grade_com.append(grade)
            elif count == d_type[2]["en"]:
                d_type[2]["like"] += like
                money_fan.append(money)
                grade_fan.append(grade)
            elif count == d_type[3]["en"]:
                d_type[3]["like"] += like
                money_mys.append(money)
                grade_mys.append(grade)
            elif count == d_type[4]["en"]:
                d_type[4]["like"] += like
                money_thr.append(money)
                grade_thr.append(grade)
            elif count == d_type[5]["en"]:
                d_type[5]["like"] += like
                money_doc.append(money)
                grade_doc.append(grade)
            elif count == d_type[6]["en"]:
                d_type[6]["like"] += like
                money_war.append(money)
                grade_war.append(grade)
            elif count == d_type[7]["en"]:
                d_type[7]["like"] += like
                money_wes.append(money)
                grade_wes.append(grade)
            elif count == d_type[8]["en"]:
                d_type[8]["like"] += like
                money_rom.append(money)
                grade_rom.append(grade)
            elif count == d_type[9]["en"]:
                d_type[9]["like"] += like
                money_dra.append(money)
                grade_dra.append(grade)
            elif count == d_type[10]["en"]:
                d_type[10]["like"] += like
                money_hor.append(money)
                grade_hor.append(grade)
            elif count == d_type[11]["en"]:
                d_type[11]["like"] += like
                money_act.append(money)
                grade_act.append(grade)
            elif count == d_type[12]["en"]:
                d_type[12]["like"] += like
                money_sci.append(money)
                grade_sci.append(grade)
            elif count == d_type[13]["en"]:
                d_type[13]["like"] += like
                money_mus.append(money)
                grade_mus.append(grade)
            elif count == d_type[14]["en"]:
                d_type[14]["like"] += like
                money_fam.append(money)
                grade_fam.append(grade)
            elif count == d_type[15]["en"]:
                d_type[15]["like"] += like
                money_cri.append(money)
                grade_cri.append(grade)

        # 取各种类型中的票房最大值和最小值
    d_type[0]['money_max'] = max(money_adv)
    d_type[1]['money_max'] = max(money_com)
    d_type[2]['money_max'] = max(money_fan)
    d_type[3]['money_max'] = max(money_mys)
    d_type[4]['money_max'] = max(money_thr)
    d_type[5]['money_max'] = max(money_doc)
    d_type[6]['money_max'] = max(money_war)
    d_type[7]['money_max'] = max(money_wes)
    d_type[8]['money_max'] = max(money_rom)
    d_type[9]['money_max'] = max(money_dra)
    d_type[10]['money_max'] = max(money_hor)
    d_type[11]['money_max'] = max(money_act)
    d_type[12]['money_max'] = max(money_sci)
    d_type[13]['money_max'] = max(money_mus)
    d_type[14]['money_max'] = max(money_fam)
    d_type[15]['money_max'] = max(money_cri)

    d_type[0]['money_min'] = min(money_adv)
    d_type[1]['money_min'] = min(money_com)
    d_type[2]['money_min'] = min(money_fan)
    d_type[3]['money_min'] = min(money_mys)
    d_type[4]['money_min'] = min(money_thr)
    d_type[5]['money_min'] = min(money_doc)
    d_type[6]['money_min'] = min(money_war)
    d_type[7]['money_min'] = min(money_wes)
    d_type[8]['money_min'] = min(money_rom)
    d_type[9]['money_min'] = min(money_dra)
    d_type[10]['money_min'] = min(money_hor)
    d_type[11]['money_min'] = min(money_act)
    d_type[12]['money_min'] = min(money_sci)
    d_type[13]['money_min'] = min(money_mus)
    d_type[14]['money_min'] = min(money_fam)
    d_type[15]['money_min'] = min(money_cri)

    d_type[0]['grade_max'] = max(grade_adv)
    d_type[1]['grade_max'] = max(grade_com)
    d_type[2]['grade_max'] = max(grade_fan)
    d_type[3]['grade_max'] = max(grade_mys)
    d_type[4]['grade_max'] = max(grade_thr)
    d_type[5]['grade_max'] = max(grade_doc)
    d_type[6]['grade_max'] = max(grade_war)
    d_type[7]['grade_max'] = max(grade_wes)
    d_type[8]['grade_max'] = max(grade_rom)
    d_type[9]['grade_max'] = max(grade_dra)
    d_type[10]['grade_max'] = max(grade_hor)
    d_type[11]['grade_max'] = max(grade_act)
    d_type[12]['grade_max'] = max(grade_sci)
    d_type[13]['grade_max'] = max(grade_mus)
    d_type[14]['grade_max'] = max(grade_fam)
    d_type[15]['grade_max'] = max(grade_cri)

    d_type[0]['grade_min'] = min(grade_adv)
    d_type[1]['grade_min'] = min(grade_com)
    d_type[2]['grade_min'] = min(grade_fan)
    d_type[3]['grade_min'] = min(grade_mys)
    d_type[4]['grade_min'] = min(grade_thr)
    d_type[5]['grade_min'] = min(grade_doc)
    d_type[6]['grade_min'] = min(grade_war)
    d_type[7]['grade_min'] = min(grade_wes)
    d_type[8]['grade_min'] = min(grade_rom)
    d_type[9]['grade_min'] = min(grade_dra)
    d_type[10]['grade_min'] = min(grade_hor)
    d_type[11]['grade_min'] = min(grade_act)
    d_type[12]['grade_min'] = min(grade_sci)
    d_type[13]['grade_min'] = min(grade_mus)
    d_type[14]['grade_min'] = min(grade_fam)
    d_type[15]['grade_min'] = min(grade_cri)

    # print(table_massage)
    return jsonify(d_type)


@app.route('/massage/')
def massage():
    # print(table_massage)
    return jsonify(table_massage)


@app.route('/chart/', methods=['GET'])
def index():
    film_type_list = ['Action', 'Drama']
    store_score_data(film_type_list)
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def tabs():
    if request.method == 'GET':
        return render_template('tabs.html')
    else:
        table_massage['name'] = request.form.get('name')
        table_massage['director'] = request.form.get('director')
        table_massage['act1'] = request.form.get('act1')
        table_massage['act2'] = request.form.get('act2')
        table_massage['act3'] = request.form.get('act3')
        table_massage['time'] = request.form.get('time')
        table_massage['popular'] = request.form.get('popular')
        table_massage['type'] = request.form.get('type').split()
        table_massage['invest'] = request.form.get('invest')
        table_massage['key_word'] = request.form.get('key_words').split()
        table_massage['CBW'] = request.form.get('CBW')
        table_massage['level'] = request.form.get('level')
        data = xunlian.query.all()
        dir = xunlian.query.filter(xunlian.director == table_massage['director']).all()
        dir_like = act1_like = act2_like = act3_like = 0
        act1 = xunlian.query.filter(xunlian.act_one == table_massage['act1']).all()
        act2 = xunlian.query.filter(xunlian.act_two == table_massage['act2']).all()
        act3 = xunlian.query.filter(xunlian.act_three == table_massage['act3']).all()
        # i = 0
        dir_like_l = []
        act1_like_l = []
        act2_like_l = []
        act3_like_l = []
        act_like_l = []
        # print(data[0].dir_like)


        for like in data:
            if like.dir_like == '':
                like.dir_like = 0
            if like.act_one_like == '':
                like.act_one_like = 0
            if like.act_two_like == '':
                like.act_two_like = 0
            if like.act_three_like == '':
                like.act_three_like = 0
            dir_like_l.append(int(like.dir_like))
            act1_like_l.append(int(like.act_one_like))
            act2_like_l.append(int(like.act_two_like))
            act3_like_l.append(int(like.act_three_like))
            # act1_like_l[i]=int(data[i].act_one_like)
            # act2_like_l[i]=int(data[i].act_two_like)
            # act3_like_l[i]=int(data[i].act_three_like)
            # i+=1
        act_like_l.append(max(act1_like_l))  # 尽量避免角标，使用append（）方法
        act_like_l.append(max(act2_like_l))
        act_like_l.append(max(act3_like_l))
        # print(act_like_l)
        table_massage['all_act_like'] = max(act_like_l)
        table_massage['all_dir_like'] = max(dir_like_l)
        if dir:
            i = 0
            while i < len(dir):
                dir_like += int(dir[i].dir_like)
                i += 1
            table_massage['dir_like'] = dir_like / len(dir)
        if act1:
            i = 0
            while i < len(act1):
                act1_like += int(act1[i].act_one_like)
                i = i + 1
            table_massage['act1_like'] = act1_like / len(act1)
        if act2:
            i = 0
            while i < len(act2):
                act2_like += int(act2[i].act_one_like)
                i = i + 1
            table_massage['act2_like'] = act2_like / len(act2)
        if act3:
            i = 0
            while i < len(act3):
                act3_like += int(act3[i].act_one_like)
                i = i + 1
            table_massage['act3_like'] = act3_like / len(act3)

        lists.append(table_massage['invest'])
        lists.append(table_massage['dir_like'])
        lists.append(request.form.get('time'))
        lists.append(request.form.get('popular'))
        lists.append(table_massage['type'])
        table_massage['result'] = Create_score_model(lists)


        #针对电影类型做中英文转换
        # for item in table_massage['type']:
        #     print(langid.classify(item))
        #     if langid.classify(item)[0] != "en":
        #         for ck in l_type:
        #             if item==ck.zh or item==ck.en:
        #                 pass

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
