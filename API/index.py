from flask import Flask, url_for, render_template, request
from Predict import Predict

app = Flask(__name__)

pred = Predict()

@app.route('/')
def hello_world():
    return 'Hello, World!<br/><br/>' + pred.predict_pad()

@app.route('/test')
def test():
	data = []
	data += [ int( request.args.get('uf'     ,1) ) ]
	data += [ int( request.args.get('idade'  ,1) ) ]
	data += [ int( request.args.get('sexo'   ,1) ) ]
	data += [ int( request.args.get('sit_con',1) ) ]
	data += [ int( request.args.get('tp_esc' ,1) ) ]
	data += [ int( request.args.get('est_civ',1) ) ]
	data += [ int( request.args.get('cor_rac',1) ) ]
	#print(data)
	return '<h1>O test foi:</h1><br/><br/><h2>' + pred.predict(data) + '</h2>'

@app.route('/funcionario')
@app.route('/funcionario/<name>')
def funcionario(name=None):
    return render_template('funcionario.html', name=name)

if __name__ == '__main__':
    app.run(port='8292', host='0.0.0.0', debug=True)