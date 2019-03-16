from flask import Flask, url_for, render_template, request
from Predict import Predict
import sys

arg = sys.argv[len(sys.argv) - 1]

app = Flask(__name__)

pred = Predict()

@app.route('/')
def hello_world():
    return 'Hello, World!<br/><br/>' + pred.predict_pad()

@app.route('/kill')
def fin():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    return "Shutting down..."

@app.route('/form',  methods=['POST'])
def form2():
    data = []
    data += [ int( request.form.get('UF_RESIDENCIA'  ,1) ) ]
    data += [ int( request.form.get('IDADE'          ,1) ) ]
    data += [ int( request.form.get('TP_SEXO'        ,1) ) ]
    data += [ int( request.form.get('ST_CONCLUSAO'   ,1) ) ]
    data += [ int( request.form.get('TP_ESCOLA'      ,1) ) ]
    data += [ int( request.form.get('TP_ESTADO_CIVIL',1) ) ]
    data += [ int( request.form.get('TP_COR_RACA'    ,1) ) ]
    result = pred.predict(data)
    return render_template('form_dados.html', result=result)

@app.route('/form', methods=['GET'])
def form1(name=None):
    return render_template('form_dados.html')

if arg == "debug":
    if __name__ == '__main__':
        app.run(port='8292', host='0.0.0.0', debug=True)
else:
    if __name__ == '__main__':
        app.run(port='8292', host='0.0.0.0')