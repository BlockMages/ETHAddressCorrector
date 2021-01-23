import os
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def address_collector():
  with open( "addresses.txt" , 'a') as f:
    try:
      f.writelines( request.args.get('address') + "\n" )
    except:
      return 'アドレスを取得できません' 
  if( request.args.get('address')[1] == 'x'):
    return '登録しました！' + '動画を視聴してくれてありがとう！'
  else:
    return 'エラーが発生しています。もう一度お試しください'
