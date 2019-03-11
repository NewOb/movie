from flask import Flask, render_template, request, jsonify
import config
from exts import db
from imdb_score_model import Create_score_model
from models import xunlian

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

f_massage = {}


@app.route("/rect/", methods=['GET', 'POST'])
def rect():
    max_a = []
    max_b = []
    max_c = []
    max_d = []
    mr = {}
    d2 = []
    d4 = []
    datas = xunlian.query.all()
    # 找到导演，主演的最大值
    for i in datas:
        max_a.append(int(i.dir_like))
        max_b.append(int(i.act_one_like))
        max_c.append(int(i.act_two_like))
        max_d.append(int(i.act_three_like))
    d1 = [max(max_a), max(max_b), max(max_c), max(max_d)]
    mr['d1'] = d1

    # 计算当前导演，主演的平均点赞量
    d2.append(f_massage['dir_like'])
    act1_like = act2_like = act3_like = 0
    act1 = xunlian.query.filter(xunlian.act_one == f_massage['act1']).all()
    if act1:
        for i in act1:
            act1_like += int(i.act_one_like)
        d2.append(act1_like / len(act1))
    else:
        d2.append(0)

    act2 = xunlian.query.filter(xunlian.act_two == f_massage['act2']).all()
    if act2:
        for i in act2:
            act2_like += int(i.act_two_like)
        d2.append(act2_like / len(act2))
    else:
        d2.append(0)

    act3 = xunlian.query.filter(xunlian.act_three == f_massage['act3']).all()
    if act3:
        for i in act3:
            act3_like += int(i.act_three_like)
        d2.append(act3_like / len(act3))
    else:
        d2.append(0)

    mr['d2'] = d2
    # 计算导演，主演的平均点赞量
    adir = aact1 = aact2 = aact3 = 0
    for i in max_a:
        adir += i
    for i in max_b:
        aact1 += i
    for i in max_c:
        aact2 += i
    for i in max_d:
        aact3 += i
    d4.append(adir / len(datas))
    d4.append(aact1 / len(datas))
    d4.append(aact2 / len(datas))
    d4.append(aact3 / len(datas))
    mr['d4'] = d4
    return jsonify(mr)


@app.route("/massage/", methods=['GET', 'POST'])
def massage():
    # 前端表单所有项目
    dir_like = 0
    forrest = []
    fn = ["name", "director", "act1", "act2", "act3", "time", "type", "invest", "key_words", "popular", "CBW",
          "level"]
    # 接受表单信息
    for i in fn:
        f_massage[i] = request.form.get(i)
    f_massage['type'] = f_massage['type'].split()

    # 查询数据库中导演信息并计算导演点赞数
    dir = xunlian.query.filter(xunlian.director == f_massage['director']).all()
    if dir:
        for i in dir:
            dir_like += int(i.dir_like)
        f_massage['dir_like'] = dir_like / len(dir)
    else:
        f_massage['dir_like'] = 0

    # 预测模型所需数据,依次添加数据，将预测结果保存至forrest['result']中
    data = ["invest", "dir_like", "time", "popular", "type"]
    # print(f_massage["time"])
    for i in data:
        forrest.append(f_massage[i])
        # print(i)
    f_massage['result'] = Create_score_model(forrest)
    del forrest[:]

    a = []
    # 查找目前票房最大值
    mb = xunlian.query.all()
    for i in mb:
        a.append(int(i.Box_office))

    print(a)
    f_massage['max_box'] = max(a)
    print(f_massage)
    return jsonify(f_massage)


@app.route("/", methods=['GET'])
def Inputform():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
