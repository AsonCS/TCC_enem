import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class BaseEnem:

    "Classe responsável por lidar com o predict."
    "Nomes das colunas"
    "'UF_RESIDENCIA','IDADE','TP_SEXO','ST_CONCLUSAO','ANO_CONCLUIU','TP_ESCOLA','TP_ESTADO_CIVIL','TP_COR_RACA','IDX'"
    "'NOTA_CN','NOTA_CH','NOTA_LC','NOTA_MT','NU_NOTA_REDACAO','IDX'"
    "'UF_RESIDENCIA', 'IDADE', 'TP_SEXO', 'ST_CONCLUSAO', 'TP_ESCOLA', 'TP_ESTADO_CIVIL', 'TP_COR_RACA'"

    natu  = None
    human = None
    ling  = None
    matem = None
    redac = None

    def __init__(self):
        # Ler os arquivos e transforma em DataFrame
        x_train = pd.read_csv("dados/p_enem_train.csv")
        y_train = pd.read_csv("dados/nts_enem_train.csv")

        # Configura o DataSet
        x_train = self.ap(x_train)

        # Cria os e constroi os objetos
        self.natu  = DecisionTreeClassifier()
        self.human = DecisionTreeClassifier()
        self.ling  = DecisionTreeClassifier()
        self.matem = DecisionTreeClassifier()
        self.redac = DecisionTreeClassifier()

        # Treina os modelos
        self.natu.fit( x_train, y_train['NOTA_CN'])
        self.human.fit(x_train, y_train['NOTA_CH'])
        self.ling.fit( x_train, y_train['NOTA_LC'])
        self.matem.fit(x_train, y_train['NOTA_MT'])
        self.redac.fit(x_train, y_train['NU_NOTA_REDACAO'])

        # Limpa a memória
        del x_train
        del y_train
    
    def trip(self, n): return n * 3
    
    def doub(self, n): return n * 2
    
    # Prepara dodos para fazer predict
    def prepair(self, data):
        if data != None:
            data = pd.DataFrame(data,columns=['UF_RESIDENCIA', 'IDADE', 'TP_SEXO', 'ST_CONCLUSAO', 'TP_ESCOLA', 'TP_ESTADO_CIVIL', 'TP_COR_RACA'])
            return data
        return None

    # Configura o DataSet
    def ap(self, dd):
        if not dd.empty:
            dd = dd[['UF_RESIDENCIA', 'IDADE', 'TP_SEXO', 'ST_CONCLUSAO', 'TP_ESCOLA', 'TP_ESTADO_CIVIL', 'TP_COR_RACA']]
            dd.iloc[:0].apply(self.doub)
            dd.iloc[:1].apply(self.trip)
            dd.iloc[:2].apply(self.trip)
            dd.iloc[:3].apply(self.trip)
            dd.iloc[:4].apply(self.trip)
            dd.iloc[:5].apply(self.doub)
            dd.iloc[:6].apply(self.doub)
            return(dd)
        return None

    # Descrição dos argumentos
    '''
    args = DataFrame

    response =
    {
        'natu'  : ''
        'human' : ''
        'ling'  : ''
        'matem' : ''
        'redac' : ''
    }
    '''
    def predict(self, args):
        if not args.empty:
            response = {}
            response['natu' ] = str(  self.natu.predict( self.ap(args) )[0] )
            response['human'] = str( self.human.predict( self.ap(args) )[0] )
            response['ling' ] = str(  self.ling.predict( self.ap(args) )[0] )
            response['matem'] = str( self.matem.predict( self.ap(args) )[0] )
            response['redac'] = str( self.redac.predict( self.ap(args) )[0] )
            return response
        return ""
