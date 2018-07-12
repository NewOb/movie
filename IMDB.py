from flask import Flask,render_template,request, jsonify,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
import config
from  models import xunlian
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)


@app.route('/data/',methods=['GET'])
def data():
    ALL=xunlian.query.filter(xunlian.country=='USA').all()
    all_data={}
    ALLDATA=[]
    while len(ALL)>0:
        all_xl=ALL.pop()
        all_data['NAME']=all_xl.name
        ALLDATA.append(all_data)
        all_data={}

    return jsonify(ALLDATA)

@app.route('/chart/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/',methods=['GET','POST'])
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
        print(level)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()