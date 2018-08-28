from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import config
from imdb_score_model import Create_score_model, Type_conversion
import langid
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

list = []


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

        list.append(table_massage['invest'])
        list.append(table_massage['dir_like'])
        list.append(request.form.get('time'))
        list.append(request.form.get('popular'))
        list.append(table_massage['type'])
        table_massage['result'] = Create_score_model(list)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
