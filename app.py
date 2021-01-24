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
      return 'Error! data registration is crashed!' 
  if( request.args.get('address')[1] == 'x'):
    return 'Thank you for watching! Your Blockchain Address is registrated!'
  else:
    return 'Your address is not registrated. please try again.'

@app.route('/list')
def address_list():
  with open( "addresses.txt" , 'r') as f:
    try:
      add_list = str(f.readlines())
#      add_list2 = add_list.replace( "\\n" , "<br>").replace("\'" , "").replace("[" , "").replace("]" , "").replace("," , "")
      add_list2 = "[" + add_list.replace( "\\n" , "").replace("\'" , "\"").replace("[" , "").replace("]" , "") + "]"
      return add_list2
    except:
      return 'Error!'
