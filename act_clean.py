import pandas as pd
import src.limpieza_texto as lt

pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv("./data/attacks.csv",encoding = "ISO-8859-1")
columna='Country'
(filas,col)=df.shape
df=lt.limpia_nan(df,3)
csv='./data/continent.csv'
dicc=lt.continentes(csv)


df['Activity'] = df['Activity'].fillna('UNK')
df=lt.activity_cleaner(df,'Activity')
#######################
df.rename(columns = {'Sex ':'Sex'}, inplace=True)
df.Sex[(df.Sex!='M') & (df.Sex!='F')]=None
df.to_csv(path_or_buf='./outputs/act_out.csv',index=True)