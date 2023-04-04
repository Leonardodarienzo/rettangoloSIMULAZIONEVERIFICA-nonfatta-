from flask import Flask, request, render_template
import math
app = Flask(__name__)
def aR(a,b):
    return a * b

def dR(a,b):
    return math.sqrt(a**2 + b**2)

@app.route('/')
def home():
    return render_template('result_4_1.html')

@app.route('/data', methods=['POST',"GET"])
def data():
    base = float(request.args.get('base'))
    altezza = float(request.args.get('altezza'))
    calcolo=request.args.getlist('calcolo')
    calcola_area = 'area' in calcolo
    calcola_diagonale = 'diagonale' in calcolo
    risultato1=""
    risultato2=""

    if calcola_area:
        risultato1 = base * altezza
        
    if calcola_diagonale:
        risultato2 = math.sqrt(base**2 + altezza**2)

    return render_template('result_4.html', base=base, altezza=altezza, calcolo=calcolo, risultato1=risultato1, risultato2=risultato2)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)