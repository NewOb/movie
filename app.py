from flask import Flask, render_template, request, jsonify
import config
from exts import db
from imdb_score_model import Create_score_model
from models import xunlian

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route("/massage/", methods=['GET', 'POST'])
def massage():
    # 前端表单所有项目
    global f_massage
    f_massage = {}
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

    a=[]
    #查找目前票房最大值
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
