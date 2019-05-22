import pandas as pd 
import nltk
import os
files = os.listdir('NAE_final')
df2=pd.DataFrame()
for f in files:
	df1=pd.read_excel('NAE_final/'+f)
	df2=df2.append(df1)

df2.to_excel('Final.xlsx')


