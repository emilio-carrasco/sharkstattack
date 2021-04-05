import pandas as pd
import src.limpieza_texto as lt

pd.options.mode.chained_assignment = None  # default='warn'
srk = pd.read_csv("./data/attacks.csv",encoding = "ISO-8859-1")
column_years='Years'
srk = lt.year_cleaner(srk,column_years)
pais = 'AUSTRALIA'
srk_country = lt.clean_one_country(srk, pais)
temp = lt.read_temp("./data/temp.csv", column_years)
magnitud='Attacks'
srk_hist = lt.histograma(srk_country,column_years,magnitud)

primero = 1950
ultimo = 2017
temp = lt.filter_years(temp, primero, ultimo)
srk_hist  = lt.filter_years(srk_hist, primero, ultimo)

df=lt.unir(temp,srk_hist)
df.to_csv(path_or_buf='./outputs/anyos_out.csv',index=True)