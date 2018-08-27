from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import config
import langid
from models import xunlian
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

d_type = [{'en': 'Comedy', 'zh': '喜剧', 'like': 0},
          {'en': 'Adventure', 'zh': '冒险', 'like': 0},
          {'en': 'Fantasy', 'zh': '幻想', 'like': 0},
          {'en': 'Mystery', 'zh': '悬念', 'like': 0},
          {'en': 'Thriller', 'zh': '惊悚', 'like': 0},
          {'en': 'Documentary', 'zh': '记录', 'like': 0},
          {'en': 'War', 'zh': '战争', 'like': 0},
          {'en': 'Western', 'zh': '西部', 'like': 0},
          {'en': 'Romance', 'zh': '爱情', 'like': 0},
          {'en': 'Drama', 'zh': '剧情', 'like': 0},
          {'en': 'Horror', 'zh': '恐怖', 'like': 0},
          {'en': 'Action', 'zh': '动作', 'like': 0},
          {'en': 'Sci-Fi', 'zh': '科幻', 'like': 0},
          {'en': 'Music', 'zh': '音乐', 'like': 0},
          {'en': 'Family', 'zh': '家庭', 'like': 0},
          {'en': 'Crime', 'zh': '犯罪', 'like': 0},
          ]


@app.route('/data/', methods=['GET'])
def data():
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
            if count == d_type[0]["en"]:
                d_type[0]["like"] += like
                d_type[0]["like"] /= 2
            elif count == d_type[1]["en"]:
                d_type[1]["like"] += like
                d_type[1]["like"] /= 2
            elif count == d_type[2]["en"]:
                d_type[2]["like"] += like
                d_type[2]["like"] /= 2
            elif count == d_type[3]["en"]:
                d_type[3]["like"] += like
                d_type[3]["like"] /= 2
            elif count == d_type[4]["en"]:
                d_type[4]["like"] += like
                d_type[4]["like"] /= 2
            elif count == d_type[5]["en"]:
                d_type[5]["like"] += like
                d_type[5]["like"] /= 2
            elif count == d_type[6]["en"]:
                d_type[6]["like"] += like
                d_type[6]["like"] /= 2
            elif count == d_type[7]["en"]:
                d_type[7]["like"] += like
                d_type[7]["like"] /= 2
            elif count == d_type[8]["en"]:
                d_type[8]["like"] += like
                d_type[8]["like"] /= 2
            elif count == d_type[9]["en"]:
                d_type[9]["like"] += like
                d_type[9]["like"] /= 2
            elif count == d_type[10]["en"]:
                d_type[10]["like"] += like
                d_type[10]["like"] /= 2
            elif count == d_type[11]["en"]:
                d_type[11]["like"] += like
                d_type[11]["like"] /= 2
            elif count == d_type[12]["en"]:
                d_type[12]["like"] += like
                d_type[12]["like"] /= 2
            elif count == d_type[13]["en"]:
                d_type[13]["like"] += like
                d_type[13]["like"] /= 2
            elif count == d_type[14]["en"]:
                d_type[14]["like"] += like
                d_type[14]["like"] /= 2
            elif count == d_type[15]["en"]:
                d_type[15]["like"] += like
                d_type[15]["like"] /= 2

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
    d_type.append(table_massage['type'])
    # print(jsonify(d_type[0]['en']))
    return jsonify(d_type)


# @app.route('/massage/')
# def massage():
#     message = []
#     a = []
#     years = []
#     # 中英文翻译转换
#     # print(table_massage)
#     for types in table_massage['type']:
#         if langid.classify(types)[0] != 'zh':
#             for i in d_type[0:15]:
#                 if types == i['en']:
#                     types = i['zh']
#                     a.append(types)
#         else:
#             a.append(types)
#
#     table_massage['type'] = a
#
#     data = xunlian.query.all()
#     for year in data:
#         if year.years == "NULL":
#             continue
#         elif year.years == '':
#             continue
#         elif year.years == "0":
#             continue
#         elif int(year.years) < 2000:
#             continue
#         years.append(int(year.years))
#     years = list(set(years))
#     years.sort()
#     com_box = com_sor = adv_box = adv_sor = fan_box = fan_sor = mys_box = mys_sor = thr_box = thr_sor = doc_box = doc_sor = war_box = war_sor = wes_box = wes_sor = rom_box = rom_sor = dra_box = dra_sor = hor_box = hor_sor = act_box = act_sor = sci_box = sci_sor = mus_box = mus_sor = fam_box = fam_sor = cri_box = cri_sor = 0
#     a = b = c = d = e = f = g = h = i1 = j = k = l = m = n = o = p = 0
#     year_data = {}
#     need_massage = []
#     for year in years:
#         for i in data:
#             if i.years == '':
#                 i.years = 0
#             if int(i.years) == year:
#                 need = i.type.split("|")
#                 for needs in need:
#                     # pass
#                     if i.Box_office == '':
#                         continue
#                     if i.IMDB == '':
#                         continue
#                     if needs == d_type[0]["en"]:
#                         com_box += int(i.Box_office)
#                         com_sor += float(i.IMDB)
#                         a += 1
#                         # print(a)
#                     elif needs == d_type[1]["en"]:
#                         adv_box += int(i.Box_office)
#                         adv_sor += float(i.IMDB)
#                         b += 1
#                     elif needs == d_type[2]["en"]:
#                         fan_box += int(i.Box_office)
#                         fan_sor += float(i.IMDB)
#                         c += 1
#                     elif needs == d_type[3]["en"]:
#                         mys_box += int(i.Box_office)
#                         mys_sor += float(i.IMDB)
#                         d += 1
#                     elif needs == d_type[4]["en"]:
#                         thr_box += int(i.Box_office)
#                         thr_sor += float(i.IMDB)
#                         e += 1
#                     elif needs == d_type[5]["en"]:
#                         doc_box += int(i.Box_office)
#                         doc_sor += float(i.IMDB)
#                         f += 1
#                     elif needs == d_type[6]["en"]:
#                         war_box += int(i.Box_office)
#                         war_sor += float(i.IMDB)
#                         g += 1
#                     elif needs == d_type[7]["en"]:
#                         wes_box += int(i.Box_office)
#                         wes_sor += float(i.IMDB)
#                         h += 1
#                     elif needs == d_type[8]["en"]:
#                         rom_box += int(i.Box_office)
#                         rom_sor += float(i.IMDB)
#                         i1 += 1
#                     elif needs == d_type[9]["en"]:
#                         dra_box += int(i.Box_office)
#                         dra_sor += float(i.IMDB)
#                         j += 1
#                     elif needs == d_type[10]["en"]:
#                         hor_box += int(i.Box_office)
#                         hor_sor += float(i.IMDB)
#                         k += 1
#                     elif needs == d_type[11]["en"]:
#                         act_box += int(i.Box_office)
#                         act_sor += float(i.IMDB)
#                         l += 1
#                     elif needs == d_type[12]["en"]:
#                         sci_box += int(i.Box_office)
#                         sci_sor += float(i.IMDB)
#                         m += 1
#                     elif needs == d_type[13]["en"]:
#                         mus_box += int(i.Box_office)
#                         mus_sor += float(i.IMDB)
#                         n += 1
#                     elif needs == d_type[14]["en"]:
#                         fam_box += int(i.Box_office)
#                         fam_sor += float(i.IMDB)
#                         o += 1
#                     elif needs == d_type[15]["en"]:
#                         cri_box += int(i.Box_office)
#                         cri_sor += float(i.IMDB)
#                         p += 1
#         if g == 0:
#             g = 1
#         year_data['year'] = year
#         year_data['com_box'] = com_box / a
#         year_data['com_sor'] = com_sor / a
#         year_data['adv_box'] = adv_box / b
#         year_data['adv_sor'] = adv_sor / b
#         year_data['fan_box'] = fan_box / c
#         year_data['fan_sor'] = fan_sor / c
#         year_data['mys_box'] = mys_box / d
#         year_data['mys_sor'] = mys_sor / d
#         year_data['thr_box'] = thr_box / e
#         year_data['thr_sor'] = thr_sor / e
#         year_data['doc_box'] = doc_box / f
#         year_data['doc_sor'] = doc_sor / f
#         year_data['war_box'] = war_box / g
#         year_data['war_sor'] = war_sor / g
#         year_data['wes_box'] = wes_box / h
#         year_data['wes_sor'] = wes_sor / h
#         year_data['rom_box'] = rom_box / i1
#         year_data['rom_sor'] = rom_sor / i1
#         year_data['dra_box'] = dra_box / j
#         year_data['dra_sor'] = dra_sor / j
#         year_data['hor_box'] = hor_box / k
#         year_data['hor_sor'] = hor_sor / k
#         year_data['act_box'] = act_box / l
#         year_data['act_sor'] = act_sor / l
#         year_data['sci_box'] = sci_box / m
#         year_data['sci_sor'] = sci_sor / m
#         year_data['mus_box'] = mus_box / n
#         year_data['mus_sor'] = mus_sor / n
#         year_data['fam_box'] = fam_box / o
#         year_data['fam_sor'] = fam_sor / o
#         year_data['cri_box'] = cri_box / p
#         year_data['cri_sor'] = cri_sor / p
#         need_massage.append(year_data)
#         year_data = {}
#     message.append(table_massage)
#     message.append(need_massage)
#     return jsonify(message)


@app.route('/chart/', methods=['GET'])
def index():
    return render_template('index.html')


table_massage = {}


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
        table_massage['like'] = request.form.get('like')
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
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
