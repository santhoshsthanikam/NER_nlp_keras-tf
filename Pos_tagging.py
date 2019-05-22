import pandas as pd 
from polyglot.text import Text
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag, ne_chunk
stop_words = set(stopwords.words('english'))
df1 = pd.read_excel('PlatformWise Data (Patch Management)/MS Windows Operating system All.xlsx')
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
'smay18','production','argentina','hence','gi_generic_Ddst_s1','notice','delinquency','intranet','gabriel','cimmino','mariano','reports','review','action','deletion','follow','list', 
'test','tech','b06cxhpsy070.portsmouth.uk.ibm.com','hu.ibm.com','gi_svc_tst_s2','squad','needs','settings','frame','submission','questions','baseline','vulnerabilidad','AMERICAS-US-UISL-ZLINUX','GI_BU_GTS_GBS_S1',
'gi_bu_gts_gbs_s1','au02uap875ghox2','global','p', 'customer', 'accordance', 'have', 'question','march', 'checking', 'month', 'heath','americas-us-uisl-zlinux','equipo','aug2017','gi_generic_dst_s1',
'remove', '**privileged**', 'gi_ssc_om_s2', 'systems','spectre/meltdown', 'issue','deffect', 'btepprod.boulder.ibm.com','cve-2017-15715','cve-2018-1449','cve-2018-1450','cve-2018-1452','cve-2016-9841','cve-2018-1451',
'cve-2017-6463','cve-2017-3737','cve-2017-7562','high','sia-mvs-2018.01-8', '\x96','cve-2017-10295','cve-2018-2603','cve-2017-15715','cve-2017-10356','cve-2017-10356','scripting','termination',
'group', 'invalid','memory','leak','applications','queues','shared','user','agent','thread','log','system','feature','deadlock','attacks','side','exponentiation','advanced','messages',
 'processes','nonstop','ipadressfamily','call','help','hoc', 'authorization', 'ad', 'tasks', 'assigment', 'views', 'task','export', 'leakage','scripting','outside','portal']

useful=['flash-plugin','qemu-kvm-rhev','plexus-archiver','chromium-browser','openslp','yum-utils','kernel-alt','firefox','vdsm',
'qemu-kvm','libvirt','rhevm-setup-plugins','rhvm-appliance','kernel-rt','ghostscript-library','nautilus','nagios-nrpe','util-linux',
'unixODBC','ucode-intel','nautilus','AS2','OpenSSH','AIX']
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
Abstract =[]
Keys = []
Abstract_keyword=pd.DataFrame(columns=(['Abstract','Keys','Application','Middleware']))
i=0
for l in li:
	i+=1
	lis_NAE_tag=[]
	tokenized = nltk.word_tokenize(l)
	
	nouns = set(word for (word, pos) in nltk.pos_tag(tokenized) if (is_noun(pos) or is_nounp(pos) or word in useful) and word.lower() not in li_bad)
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
	if bool(nouns) != False:
		Keys.append(nouns)
		Abstract.append(l)
	else:
		Keys.append(None)
		Abstract.append(l)
"""
	if 'Red' in nouns and 'Hat' in nouns:
		nouns = [iter.replace('Hat','Red Hat') for iter in nouns]
		nouns.remove('Red')
	if 'MQ' in nouns and 'Websphere' in nouns:
		nouns = [iter.replace('MQ','Websphere MQ') for iter in nouns]
		nouns.remove('Websphere')
	if 'MQ' in nouns and 'WebSphere' in nouns:
		nouns = [iter.replace('MQ','WebSphere MQ') for iter in nouns]
		nouns.remove('WebSphere')
	if 'Hat' in nouns and 'Enterprise' in nouns:
		nouns =[iter.replace('Hat','Red Hat Enterprise Linux') for iter in nouns]
		nouns.remove('Enterprise')
		nouns.remove('Linux')
	if 'MQ' in nouns and 'Appliance' in nouns:
		nouns = [iter.replace('MQ','MQ Appliance') for iter in nouns]
		nouns.remove('Appliance')
	if 'IGA' in nouns and 'MX' in nouns:
		nouns = [iter.replace('IGA','IGA MX') for iter in nouns]
		nouns.remove('MX')
	if 'Java' in nouns and 'Runtime' in nouns:
		nouns = [iter.replace('Java','Java Runtime') for iter in nouns]
		nouns.remove('Runtime')
	
	if 'Microsoft' in nouns and 'Malware' in nouns and 'Protection' in nouns and 'Engine' in nouns:
		nouns = [iter.replace('Microsoft','Microsoft Malware Protection Engine') for iter in nouns]
		nouns.remove('Malware')
		nouns.remove('Protection')
		nouns.remove('Engine')
	if 'OpenShift' in nouns and 'Container' in nouns and 'Platform' in nouns:
		nouns = [iter.replace('OpenShift','OpenShift Container Platform') for iter in nouns]
		nouns.remove('Container')
		nouns.remove('Platform')
	if 'Integration' in nouns and 'Bus' in nouns:
		nouns = [iter.replace('Integration','Integration Bus') for iter in nouns]
		nouns.remove('Bus')
	if 'Websphere' in nouns and 'Broker' in nouns:
		nouns = [iter.replace('Webphere','WebSphere Message Broker') for iter in nouns]
		nouns.remove('Broker')
	if 'WebSphere' in nouns and 'Broker' in nouns:
		nouns = [iter.replace('WebSphere','WebSphere Message Broker') for iter in nouns]
		nouns.remove('Broker')
	if 'Db2' in nouns and 'Warehouse' in nouns:
		nouns = [iter.replace('Db2','Db2 Warehouse') for iter in nouns]
		nouns.remove('Warehouse')
	if 'Linux' in nouns and 'Kernel' in nouns:
		nouns = [iter.replace('Linux','Linux Kernel') for iter in nouns]
		nouns.remove('Kernel')
	if 'Hat' in nouns:
		nouns = [iter.replace('Hat','Red Hat') for iter in nouns]
	if 'Apache' in nouns and 'Struts' in nouns:
		nouns = [iter.replace('Struts','Apache Struts') for iter in nouns]
	if 'VIOS' in nouns and 'iFixes' in nouns:
		nouns = [iter.replace('iFixes','VIOS iFixes') for iter in nouns]
		nouns.remove('VIOS')
	if 'Red' in nouns and 'Hat' in nouns:
		nouns = [iter.replace('Red','Red Hat') for iter in nouns]
		nouns.remove('Hat')
	if 'Red' in nouns and 'Hat' in nouns:
		nouns = [iter.replace('Red','Red Hat') for iter in nouns]
		nouns.remove('Hat')
	if 'Apache' in nouns and 'Struts' in nouns:
		nouns = [iter.replace('Struts','Apache Struts') for iter in nouns]
		nouns.remove('Apache')
	if 'Apache' in nouns and 'Tomcat' in nouns:
		nouns = [iter.replace('Tomcat','Apache Tomcat') for iter in nouns]
		nouns.remove('Apache')
	if 'WebSphere' in nouns and 'Lombardi' in nouns:
		nouns = [iter.replace('Lombardi','WebSphere Lombardi') for iter in nouns]
		nouns.remove('WebSphere')
	if 'WebSphere' in nouns and 'Portal' in nouns:
		nouns = [iter.replace('Portal','WebSphere Portal') for iter in nouns]
		nouns.remove('WebSphere')
	if 'Adobe' in nouns and 'Flash' in nouns:
		nouns = [iter.replace('Adobe','Adobe Flash') for iter in nouns]
		nouns.remove('Flash')
"""
	

Abstract_keyword['Abstract']=Abstract
Abstract_keyword['Keys']=Keys
Abstract_keyword.to_excel('PlatformWise Data (Patch Management)/MS Windows Operating system All.xlsx')
