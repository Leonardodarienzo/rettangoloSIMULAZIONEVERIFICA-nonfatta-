from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('result_5.html')

@app.route('/data', methods=['POST',"GET"])
def data():
    figura_selezionata = request.form['figure']
    if figura_selezionata == 'cerchio':
        figura = "img/cerchio.png"
    elif figura_selezionata == 'rettangolo':
        figura = "img/rettangolo.png"
    elif figura_selezionata == 'quadrato':
        figura = "img/quadrato.png"
    elif figura_selezionata == 'pentagono':
        figura = "img/pentagono.png"
    return render_template("result5.html", percorso = figura)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)