import pandas as pd
from sklearn.tree import DecisionTreeClassifier

class BaseEnem:
    """
    Classe responsável por lidar com o predict.
    Nomes das colunas::
    'UF_RESIDENCIA','IDADE','TP_SEXO','ST_CONCLUSAO','ANO_CONCLUIU','TP_ESCOLA','TP_ESTADO_CIVIL','TP_COR_RACA','IDX'
    'NOTA_CN','NOTA_CH','NOTA_LC','NOTA_MT','NU_NOTA_REDACAO','IDX'
    'UF_RESIDENCIA', 'IDADE', 'TP_SEXO', 'ST_CONCLUSAO', 'TP_ESCOLA', 'TP_ESTADO_CIVIL', 'TP_COR_RACA'
    """

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

        #: Limpa a memória x_train
        del x_train
        #: Limpa a memória y_train
        del y_train
    
    def trip(self, n): return n * 3
    
    def doub(self, n): return n * 2
    
    
    def prepair(self, data):
        """ Prepara dodos para fazer predict """
        if data != None:
            data = pd.DataFrame(data,columns=['UF_RESIDENCIA', 'IDADE', 'TP_SEXO', 'ST_CONCLUSAO', 'TP_ESCOLA', 'TP_ESTADO_CIVIL', 'TP_COR_RACA'])
            return data
        return None

    
    def ap(self, dd):
        """ Configura o DataSet """
        if not dd.empty:
            data = dd[['UF_RESIDENCIA', 'IDADE', 'TP_SEXO', 'ST_CONCLUSAO', 'TP_ESCOLA', 'TP_ESTADO_CIVIL', 'TP_COR_RACA']]
            data['IDADE2'] = dd.iloc[:,1] ^ 2
            data['TP_SEXO2'] = dd.iloc[:,2] ^ 2
            data['TP_SEXO3'] = dd.iloc[:,2] ^ 3
            data['ST_CONCLUSAO2'] = dd.iloc[:,3] ^ 2
            data['ST_CONCLUSAO3'] = dd.iloc[:,3] ^ 3
            return(data)
        return None
    
    
    def predict(self, args):
        """
        Descrição dos argumentos
        args = DataFrame

        response =
        {
        'natu'  : ''
        'human' : ''
        'ling'  : ''
        'matem' : ''
        'redac' : ''
        }
        """
        if not args.empty:
            response = {}
            response['natu' ] = str(  self.natu.predict( self.ap(args) )[0] )
            response['human'] = str( self.human.predict( self.ap(args) )[0] )
            response['ling' ] = str(  self.ling.predict( self.ap(args) )[0] )
            response['matem'] = str( self.matem.predict( self.ap(args) )[0] )
            response['redac'] = str( self.redac.predict( self.ap(args) )[0] )
            return response
        return ""
