import pandas as pd 
from polyglot.text import Text
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag, ne_chunk

def keywords(sent):
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
	'buffer','impacts','announce','hosted','validation','overwrite','tools','new','admin','console','packages','tm','edition','technology','health','check','container','platform',
	'novell','suse','impact','bulletin','control','vulnerabities','unsafe','driver','party','library','hardware','power','\x96','high',
	'space','environments','protection','performance','liberty','product','denial','gateways','appliance','caching','splitting','proxy','edge',
	'faces','affect','source','open','malformed','certficate','editor','protection','forgery','request','cross','site','machine','guest','key','os',
	'advisory','generation','august','june','desktop','protocol','malware','engine','elevation','variant','time','implementation','midrange',
	'applications','servers','s/accesses','contracts','online','below','need','activities','compliance','policies','date','target','days','openssh-unix-announce',
	'softwares','pack','risk','system','belongs','endpoint','issues','mar','apr','au02uap875ghox2.ahe.au.ibm.com','version','sk.ibm.com','g01cxnp20065','b03zcimq101.boulder.ibm.com',
	"'s/accesses",'.the','port','gi_svc_spo_s1','rsk100018054','services1bte.pok.ibm.com','suport','gi_cba_sap_s3','gi_svc_gsc_s1','canada','ownership','revalidation',
	'corrección','apr2017','exc','desviaciones','cycle','chapter','currency','ends','unsecured','group1','analysis','protocols','g01aciwas062.ahe.pok.ibm.com','b06cxhd0p0230.portsmouth.uk.ibm.com', 'b06cxhd0p0330.portsmouth.uk.ibm.com', 'b06cxnr0p0231.portsmouth.uk.ibm.com',
	'b06cxnr0p0232.portsmouth.uk.ibm.com','analysis','scanning-jan-2016','protocols','g01aciwas062.ahe.pok.ibm.com','instance','smallbluep8.pok','authorization',
	'smay18','production','argentina']

	useful=['flash-plugin','qemu-kvm-rhev','plexus-archiver','chromium-browser','openslp','yum-utils','kernel-alt','firefox','vdsm',
	'qemu-kvm','libvirt','rhevm-setup-plugins','rhvm-appliance','kernel-rt','ghostscript-library','nautilus','nagios-nrpe','util-linux',
	'unixODBC','ucode-intel','nautilus','AS2','OpenSSH','AIX']

	tokenized = nltk.word_tokenize(sent)
	
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
	java = ''
	for j in tokenized:
		if j[0:4] =='java' or j[0:8] =='rh-mysql' or j[0:6]=='python' or j[0:6] =='xmlrpc' or j[0:6] =='rh-php' or j[0:10]=='go-toolset' or j[0:7]=='rh-java' or j[0:8]=='rh-maven':
			java=j
	if java not in nouns and java !='':
		nouns.append(java)
	for k in nouns:
		if k[0:4] == 'RHSA' or k[0:4] =='SUSE' or k[0:3]=='CVE' or k[0:3]=='SIA' or k[0:4]=='CVE-' or k[0:5]=='MEESA':
			nouns.remove(k)
	for k in nouns:
		if k[0:3]=='CVE' or k[0:3] =='CVE' or k[0:4]=='bo3z' or k[0:6] =='AC2_GI':
			nouns.remove(k)
	if 'bug' in tokenized and 'fix' in tokenized:
		nouns.append('bug fix')
	if 'dhcp' in tokenized:
		nouns.append('dhcp')
	for j in tokenized:
		if j in useful and j not in nouns:
			nouns.append(j)
	try:
		if 'SLE' in nouns:
			index = tokenized.index('SLE')
			nouns = [iter.replace('SLE',tokenized[index]+" "+tokenized[index+1]+' '+tokenized[index+2]) for iter in nouns]
			nouns.remove(tokenized[index+2])
	except:
		pass

	return nouns
