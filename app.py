from flask import Flask, render_template, request, jsonify
import config
from exts import db
from imdb_score_model import Create_score_model
from models import xunlian

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# 将颜色统一设定
@app.route("/color/",methods=['GET','POST'])
def color():
    type_color = [{'name': 'Comedy', 'Color': '#178BCA'},
              {'name': 'Advnameture', 'Color': '#CDAA7D'},
              {'name': 'Fantasy', 'Color': '#008B00'},
              {'name': 'Mystery', 'Color': '#9ACD32'},
              {'name': 'Thriller', 'Color': '#8EE5EE'},
              {'name': 'Documnametary', 'Color': '#AA7D39'},
              {'name': 'War', 'Color': '#696969'},
              {'name': 'Western', 'Color': '#DB7093'},
              {'name': 'Romance', 'Color': '#FF8C00'},
              {'name': 'Drama', 'Color': '#20B2AA'},
              {'name': 'Horror', 'Color': '#000000'},
              {'name': 'Action', 'Color': '#CD2626'},
              {'name': 'Sci-Fi','Color': '#FFD700'},
               {'name': 'Music', 'Color': '#9932CC'},
              {'name': 'Family', 'Color': '#CD96CD'},
              {'name': 'Crime', 'Color': '#CCCC33'},
              ]
    return jsonify(type_color)

@app.route("/ball_data/", methods=['GET'])
def ball():
    pass


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
    return jsonify(f_massage)


@app.route("/", methods=['GET'])
def Inputform():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
