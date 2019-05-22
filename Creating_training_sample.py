import pandas as pd 
from polyglot.text import Text
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag, ne_chunk
import numpy as np 
import math
stop_words = set(stopwords.words('english'))
df1 = pd.read_excel('Final_nodup.xlsx')
li = (df1['Abstract'].tolist())

#for l in li:
#	print (ne_chunk(pos_tag(word_tokenize(l))))
is_noun = lambda pos: pos[:2] == 'NN'
is_nounp = lambda pos: pos[:2] == 'NNP'
li_bad = ['moderate','security','update','perform','failure','violation','perform','vulnerabilities','us','end','life','project','Critical',
'privileges','execution','Keys','account','configuration','low','bug','fix','deserialization','vulnerability','files','deviation','Version','common','findings','vulnerabilites',
'ibm','spectrum','protect','storage','manager','windows','macintosh','client','commons','fileupload','managed','file','transfer','component','affects','r',
'message','headers','transmission','channels','data','error','important','application','@','secure','creation','may','tool','fixes',
'code','guidance','side-channel','response','spectre','meltdown','operations','center','management','service','updates','critical',
'process','designer','business','automation','workflow','speculative','store','bypass','patch','live','speculative','enhancement','Analysis',
'violations','scan','please','refer','description','column','details','medium','behavior','insecure','permission','privilege',
'escalation',']','keys','single','sign-on','april','information','disclosure','remote','confidential','escallation','[','format','multiple','path','libraries','july',
'july','circumstances','algorithm','password','users','installation','support','cheklist','kt','s/accesses','/','id','access',
'managment','team','ac2','identity','connect','activity','history','upgrade','patches','virtualization','new','function','propagation','flaw','certificate',
'extension','ipfdressfamily','queue','clients','channel','server','entity','attack','injection','vulnerable','external','modules',
'buffer','impacts','announce','hosted','validation','overwrite','tools','new','admin','console','tm','edition','technology','health','check']

"""
bad = []
for l in li:
	try:
		text = Text(l)
		for entity in text.entities:
			if entity.tag == "I-ORG":
				print(entity)
		break
	except :
		bad.append(l)

"""
#Abs_keywords = pd.DataFrame(columns=('Abstract','Keys'),index=range(li))
Words=[]
Words_NAE_Tags=[]
i=0
df1 = pd.read_excel('Final_nodup.xlsx')
df1 = df1.fillna('')
Ab = df1['Abstract'].tolist()
Misc = df1['Misc'].tolist()
app = df1['Application'].tolist()
app_b = df1['Application-B'].tolist()
app_m =df1['Application-M'].tolist()
app_e = df1['Application-E'].tolist()
middl = df1['Middleware'].tolist()

Abstract_keyword=pd.DataFrame(columns=(['Abstract','Misc','Application','Application-B','Application-M','Application-E','Middleware','NAE_Tags']))
Words=[]
NAE_Tags=[]
i=0
for a,mis1,ap,ap_b,ap_m,ap_e,midd in zip(Ab,Misc,app,app_b,app_m,app_e,middl):
	i+=1
	NAE=[]
	words= nltk.word_tokenize(a)
	"""
	if np.isnan(ap_b):
		ap_b=[]
	if np.isnan(ap_m):
		ap_m=[]
	if np.isnan(ap_e):
		ap_e=[]
	if np.isnan(midd):
		midd=[]
	if mis1 = str:
		if math.isnan(mis1):
			mis1=[]
	"""
	for w in words:
		ap_m=str(ap_m)
		if w in ap_b:
			NAE.append('B-APP')
		elif w in ap_m:
			NAE.append('M-APP')
		elif w in ap_e:
			NAE.append('E-APP')
		elif w in ap:
			NAE.append('I-APP')
		elif w in midd:
			NAE.append('I-MIDD')
		elif w in mis1:
			NAE.append('I-MISC')
		else:
			NAE.append('O')
	NAE_Tags.append(NAE)
	Words.append(words)

print(Words)
print(NAE_Tags)

Abstract_keyword['Abstract']=df1['Abstract']
Abstract_keyword['Misc'] = df1['Misc']
Abstract_keyword['Application'] = df1['Application']
Abstract_keyword['Application-B'] = df1['Application-B']
Abstract_keyword['Application-M'] =df1['Application-M']
Abstract_keyword['Application-E'] = df1['Application-E']
Abstract_keyword['Middleware'] = df1['Middleware']
Abstract_keyword['Words']=Words
Abstract_keyword['NAE_Tags']=NAE_Tags
Abstract_keyword.to_excel('Ab_Words_NAE_Tags.xlsx')
