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
  return 'NFT年賀状の配布ページは1月1日公開です。<a href="https://twitter.com/NandemoToken">Twitter</a>でご案内します。お待ちください。</br><img src="https://raw.githubusercontent.com/nandemotoken/New-Years-Card-Server/gh-pages/hagaki.png">'
