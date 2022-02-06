import os
import pandas as pd

abspath = os.path.abspath('__file__')
dname = os.path.dirname(abspath)
os.chdir(dname)
data=pd.read_csv("DataBitcoin.csv", encoding='ISO-8859-1') #Se extraen los datos
df=pd.DataFrame(data) 
#df=df.filter(items=['Timestamp','Close']) #[4857377 rows x 2 columns]
df=df.dropna()
df.to_csv('Bitcoin_clean.csv',index=False)