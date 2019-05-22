import os
import pandas as pd
import glob
df2 = pd.DataFrame()
directories = os.listdir('Quote to Cash and Services - CIRATS Status Report')
for dir in directories:
	for files in os.listdir('Quote to Cash and Services - CIRATS Status Report/'+dir):
		fname = os.path.abspath('Quote to Cash and Services - CIRATS Status Report/'+dir+'/'+files)
		print(fname)
		df1 = pd.read_excel(fname,skiprows=[0,1,2,3,4,5,6,7])
		lis=['Abstract','Platform']
		df2=df2.append(df1[lis])
		
print(df2.to_excel('test.xlsx'))