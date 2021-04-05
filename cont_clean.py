import pandas as pd
import src.limpieza_texto as lt
import matplotlib.pyplot as plt
import seaborn as sns
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv("./data/attacks.csv",encoding = "ISO-8859-1")
columna='Country'
(filas,col)=df.shape
df=lt.limpia_nan(df,3)

csv='./data/continent.csv'
dicc=lt.continentes(csv)

df['Country'].fillna('', inplace=True)
df=lt.trunca_comas(df,'Country')
df=lt.busca_contienente(df,'Country','Continent',dicc)
df=lt.pide_continente(df,dicc,'Country','Continent')
df.rename(columns = {'Sex ':'Gender'}, inplace=True)
df=lt.clean_gender(df,'Gender')
df.to_csv(path_or_buf='./outputs/cont_out.csv',index=True)
