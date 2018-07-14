from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import config
from models import xunlian
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/data/', methods=['GET'])
def data():
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
            elif count == d_type[1]["en"]:
                d_type[1]["like"] += like
            elif count == d_type[2]["en"]:
                d_type[2]["like"] += like
            elif count == d_type[3]["en"]:
                d_type[3]["like"] += like
            elif count == d_type[4]["en"]:
                d_type[4]["like"] += like
            elif count == d_type[5]["en"]:
                d_type[5]["like"] += like
            elif count == d_type[6]["en"]:
                d_type[6]["like"] += like
            elif count == d_type[7]["en"]:
                d_type[7]["like"] += like
            elif count == d_type[8]["en"]:
                d_type[8]["like"] += like
            elif count == d_type[9]["en"]:
                d_type[9]["like"] += like
            elif count == d_type[10]["en"]:
                d_type[10]["like"] += like
            elif count == d_type[11]["en"]:
                d_type[11]["like"] += like
            elif count == d_type[12]["en"]:
                d_type[12]["like"] += like
            elif count == d_type[13]["en"]:
                d_type[13]["like"] += like
            elif count == d_type[14]["en"]:
                d_type[14]["like"] += like
            elif count == d_type[15]["en"]:
                d_type[15]["like"] += like

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

    return jsonify(d_type)


@app.route('/massage/')
def massage():
    return jsonify(table_massage)


@app.route('/chart/', methods=['GET'])
def index():
    massage = jsonify(table_massage)
    return render_template('index.html', massage=massage)


table_massage = {}


@app.route('/', methods=['GET', 'POST'])
def tabs():
    if request.method == 'GET':
        return render_template('tabs.html')
    else:
        table_massage['name'] = request.form.get('name')
        table_massage['director'] = request.form.get('director')
        table_massage['act'] = request.form.get('act').split("/")
        table_massage['type'] = request.form.get('type').split()
        table_massage['invest'] = request.form.get('invest')
        table_massage['key_word'] = request.form.get('key_words').split()
        table_massage['CBW'] = request.form.get('CBW')
        table_massage['level'] = request.form.get('level')
        dir = xunlian.query.filter(xunlian.director == table_massage['director']).all()
        dir_like = act1_like = act2_like = act3_like = 0
        act1 = xunlian.query.filter(xunlian.act_one == table_massage['act'][0]).all()
        act2 = xunlian.query.filter(xunlian.act_two == table_massage['act'][1]).all()
        act3 = xunlian.query.filter(xunlian.act_three == table_massage['act'][2]).all()
        if dir:
            i = 0
            while i < len(dir):
                dir_like = int(dir[i].dir_like)
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
