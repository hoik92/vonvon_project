from flask import Flask, render_template, request
from faker import Faker
import random
import csv

app = Flask(__name__)
fake = Faker('ko_KR')

pl = {}
fish = []

@app.route('/')
def index():
    # 두 사람의 이름을 입력 받는다.
    return render_template('index.html')

@app.route('/match')
def match():
    # 1. fake 궁합을 알려주고,
    # 2. 우리만 알 수 있게 저장한다.
    #   - fish 리스트에 append 통해 저장한다.
    # 3. match.html에는 두 사람의 이름과 random으로 생성된 50~100사이의 수를 함께 보여준다.
    #   - XX님과 YY님의 궁합은 ZZ%입니다.
    my_name = request.args.get('me')
    your_name = request.args.get('you')
    match = random.randint(50,100)
    # fish.append([my_name,your_name])
    
    # CSV 파일을 통한 데이터 영구 저장
    with open('name_list.csv', 'a', encoding='utf-8') as f:
        name_list = csv.writer(f)
        name_list.writerow([my_name, your_name])
    # with = open한 파일을 임시적으로 제어하고 제어가 끝나면 자동으로 닫아준다.
    
    return render_template('match.html', me=my_name, you=your_name, match=match)

@app.route('/admin')
def admin():
    # 낚인 사람들의 명단
    #   - template에서 반복(for)을 써서,
    #   - fish에 들어가 있는 데이터를 모두 보여준다.
    
    data = []
    
    with open('name_list.csv', 'r', encoding='utf-8') as f:
        for name in f:
            data.append(name)
    
    return render_template('admin.html', name_list=data)








# '/' : 사용자의 이름을 입력 받습니다.
@app.route('/js')
def js():
    return render_template('jeonsaeng.html')
    
# '/pastlife' : 사용자의 (랜덤으로 생성된) 전생/직업을 보여준다.
@app.route('/pastlife')
def pastlife():
    job = fake.job()
    name = request.args.get('name')
    
    if name in pl:
        pass
    else:
        pl[name] = job
    return render_template('pastlife.html', name=name, job=pl[name])
    
