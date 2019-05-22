import pandas as pd 
from polyglot.text import Text
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag, ne_chunk
import os

files = os.listdir("PlatformWise Data (Patch Management)")
for f in files:
	f_path = os.path.abspath('PlatformWise Data (Patch Management)/'+f)
	df1 = pd.read_excel(f_path)
	li = (df1['Abstract'].tolist())
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
	Abstract =[]
	Keys = []
	i=0
	Abstract_keyword=pd.DataFrame(columns=(['Abstract','Keys','Application','Middleware']))
	for l in li:
		i+=1
		lis_NAE_tag=[]
		tokenized = nltk.word_tokenize(l)
		
		nouns = set(word for (word, pos) in nltk.pos_tag(tokenized) if (is_noun(pos) or is_nounp(pos)) and word.lower() not in li_bad)
		#print(nouns)
		keywords_ab = ''
		try:
			text = Text(l)
			for entity in text.entities:
				if entity.tag == "I-ORG":
					nouns.add(entity)
		except :
			pass
		nouns=list(nouns)
		if bool(nouns) != False:
			Keys.append(nouns)
			Abstract.append(l)

		else:
			Keys.append(None)
			Abstract.append(l)
	Abstract_keyword['Abstract']=Abstract
	Abstract_keyword['Keys']=Keys
	print(f_path)
	Abstract_keyword.to_excel(f_path)
	
	

			