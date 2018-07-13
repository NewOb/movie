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
    d_type = [{'en': 'Comedy', 'zh': '喜剧','like':0},
              {'en': 'Adventure', 'zh': '冒险','like':0},
              {'en': 'Fantasy', 'zh': '幻想','like':0},
              {'en': 'Mystery', 'zh': '悬念','like':0},
              {'en': 'Thriller', 'zh': '惊悚','like':0},
              {'en': 'Documentary', 'zh': '记录','like':0},
              {'en': 'War', 'zh': '战争','like':0},
              {'en': 'Western', 'zh': '西部','like':0},
              {'en': 'Romance', 'zh': '爱情','like':0},
              {'en': 'Drama', 'zh': '剧情','like':0},
              {'en': 'Horror', 'zh': '恐怖','like':0},
              {'en': 'Action', 'zh': '动作','like':0},
              {'en': 'Sci-Fi', 'zh': '科幻','like':0},
              {'en': 'Music', 'zh': '音乐','like':0},
              {'en': 'Family', 'zh': '家庭','like':0},
              {'en': 'Crime', 'zh': '犯罪','like':0},
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

    return jsonify(d_type)


@app.route('/chart/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def tabs():
    if request.method == 'GET':
        return render_template('tabs.html')
    else:
        name = request.form.get('name')
        director = request.form.get('director')
        act = request.form.get('act')
        type = request.form.get('type')
        invest = request.form.get('invest')
        key_word = request.form.get('key_words')
        CBW = request.form.get('CBW')
        level = request.form.get('level')
        print(name)
        print(director)
        print(act)
        print(type)
        print(invest)
        print(key_word)
        print(CBW)
        print(level)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
