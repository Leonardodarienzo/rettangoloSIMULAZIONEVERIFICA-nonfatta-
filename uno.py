from flask import Flask,render_template,request
app = Flask(__name__)

import datetime
@app.route('/')
def home():
    return render_template('uno_1.html')

@app.route('/Area', methods = ['GET'])
def Arearett():
    base = float(request.args.get('base'))
    altezza = float(request.args.get('altezza'))
    area = base * altezza
    return render_template('result_1.html',Base = base,Altezza=altezza, Area = area)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)