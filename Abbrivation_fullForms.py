import pandas as pd 
df1=pd.read_excel('Final_nodup.xlsx')
Misc = df1['Misc'].tolist()
Application = df1['Application'].tolist()
Middleware = df1['Middleware'].tolist()
Misc.extend(Application)
Misc.extend(Middleware)
print(set(Misc))
appos={
	'EP':'Excessive Privileges',
	'RDP':'Remote Desktop Protocol',
	'BPM' :'Business Process Manager',
	'ESH' :'Enterprise Services Hub',
	'ESHB':'Enterprise Services Hub',
	'OSSC':'Order Status Service Component',
	'MQ':'Messge Queue',
	
}