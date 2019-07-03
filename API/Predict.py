from BaseEnem import BaseEnem
import json

class Predict:

	"Classe responsavel por intermediar a comunicação"

	bs = None

	def __init__(self):
		Predict.bs = BaseEnem()

	def put_sex(self, data, man = 1):
		if man == 1:
			data['ling' ] = str( int( data['ling' ] ) - 100 )
			data['human'] = str( int( data['human'] ) - 100 )
			data['natu' ] = str( int( data['natu' ] ) + 100 )
			data['matem'] = str( int( data['matem'] ) + 100 )
			#data['redac'] = str( int( data['redac'] ) + 100 )
		else:
			data['ling' ] = str( int( data['ling' ] ) + 200 )
			data['human'] = str( int( data['human'] ) + 200 )
			data['natu' ] = str( int( data['natu' ] ) + 100 )
			data['matem'] = str( int( data['matem'] ) + 100 )
			data['redac'] = str( int( data['redac'] ) + 200 )
		return data


	def put_age(self, data, age = 20):
		if age < 15 | age > 50:
			data['ling' ] = str( int( data['ling' ] ) - 200 )
			data['human'] = str( int( data['human'] ) - 200 )
			data['natu' ] = str( int( data['natu' ] ) - 200 )
			data['matem'] = str( int( data['matem'] ) - 200 )
			data['redac'] = str( int( data['redac'] ) - 200 )
		elif age >= 15 & age <= 19:
			data['ling' ] = str( int( data['ling' ] ) + 100 )
			data['human'] = str( int( data['human'] ) + 100 )
			data['natu' ] = str( int( data['natu' ] ) + 100 )
			data['matem'] = str( int( data['matem'] ) + 100 )
			data['redac'] = str( int( data['redac'] ) + 100 )
		else:
			data['ling' ] = str( int( data['ling' ] ) + 200 )
			data['human'] = str( int( data['human'] ) + 200 )
			data['natu' ] = str( int( data['natu' ] ) + 200 )
			data['matem'] = str( int( data['matem'] ) + 200 )
			data['redac'] = str( int( data['redac'] ) + 200 )
		return data


	def put_sit_concl(self, data, sit = 1):
		if sit == 1:
			data['ling' ] = str( int( data['ling' ] ) + 100 )
			data['human'] = str( int( data['human'] ) + 100 )
			data['natu' ] = str( int( data['natu' ] ) + 100 )
			data['matem'] = str( int( data['matem'] ) + 100 )
			data['redac'] = str( int( data['redac'] ) + 100 )
		elif sit == 4:
			data['ling' ] = str( int( data['ling' ] ) - 100 )
			data['human'] = str( int( data['human'] ) - 100 )
			data['natu' ] = str( int( data['natu' ] ) - 100 )
			data['matem'] = str( int( data['matem'] ) - 100 )
			data['redac'] = str( int( data['redac'] ) - 100 )
		return data


	def limit_1000(self, num = '1000'):
		num = int(num)
		if num == 1000:
			return '900'
		elif num > 1000:
			return '1000'
		elif num < 0:
			return '0'
		else:
			return str( num )


	def put_limit(self, data):
		data['ling' ] = self.limit_1000( data['ling' ] )
		data['human'] = self.limit_1000( data['human'] )
		data['natu' ] = self.limit_1000( data['natu' ] )
		data['matem'] = self.limit_1000( data['matem'] )
		data['redac'] = self.limit_1000( data['redac'] )
		return data


	def predict_pad(self):
		args = Predict.bs.prepair( [[25,60,1,1,2,0,2]] )
		response = Predict.bs.predict(args)
		self.put_sex(response, 1)
		self.put_age(response, 60)
		self.put_sit_concl(response, 1)
		self.put_limit(response)
		return str(json.dumps(response))

	'''
	data = ['UF_RESIDENCIA', 'IDADE', 'TP_SEXO', 'ST_CONCLUSAO', 'TP_ESCOLA', 'TP_ESTADO_CIVIL', 'TP_COR_RACA']
	'''
	def predict(self, data = [1,1,1,1,1,1]):
		args = Predict.bs.prepair( [data] )
		response = Predict.bs.predict(args)
		self.put_sex(response, data[2])
		self.put_age(response, data[1])
		self.put_sit_concl(response, data[3])
		self.put_limit(response)
		return str(json.dumps(response))
