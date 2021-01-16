import os
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  with open( "addresses.txt" , 'a') as f:
    try:
      f.writelines( request.args.get('address') + "\n" )
    except:
      return 'アドレスを取得できません'
  return '登録しました！' + os.environ.get('MES')
