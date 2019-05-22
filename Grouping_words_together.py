import nltk
import pandas as pd 
import re
import itertools
df1=pd.read_excel('Final_nodup.xlsx')
list_=[('Db2', 'Connect', 'Server'),('Business', 'Process', 'Manager', 'Process', 'Admin', 'Console'),('Business', 'Process', 'Manager', 'Process', 'Center', 'Console'),('Business', 'Process', 'Manager', 'web', 'Process', 'Designer'),('MQ', 'Appliance', 'WebGUI'),('MQ', 'Managed', 'File' ,'Transfer'),('Db2', "Warehouse"),('Java','SDK'),('Java', 'Runtime'),('FlashCopy', 'Manager'),('DB2', 'JDBC', 'driver'),('InfoSphere', 'Information', 'Server'),
('Spectrum', 'Protect', '(Tivoli', 'Storage', 'Manager)', 'Windows'),('Macintosh', 'Client'),('Spectrum', 'Protect', '(formerly', 'Tivoli', 'Storage', 'Manager)', 'Client'),('Spectrum', 'Protect', '(formerly', 'Tivoli', 'Storage', 'Manager)'),
('MVS', 'APAR'),('MV', 'APAR'),('VM', 'APAR'),('Symantec', 'Endpoint', 'Protection'),('Integration', 'Bus'),('WebSphere', 'Message', 'Broker'),('SQL', 'Server'),
('Websphere', 'MQ'),('Red', 'Hat', 'Enterprise', 'Linux'),('SPO', 'Servers'),('AC2', 'LPARS'),('WebSphere', 'Application', 'Server'),('WINDOWS\APACHE', 'TOMCAT'),
('HC', 'Cycle'),('Linux', '-', 'SuSE,'),('Linux', '-', 'RedHat,'),('Linux', '-', 'CentOS'),('WebSphere', 'Portal'),('Linux', 'Kernel'),('Linux', 'kernel'),('bug', 'fix'),
('kernel', 'security'),('OpenShift', 'Container', 'Platform'),('OpenSSL', 'Security', 'Advisory'),('Azure', 'Guest', 'OS', 'Machine', 'Key', 'Generation' ,'Algorithm'),
('SLE', '12', 'SP2)'),('SLE', '12' ,'SP1)'),('SLE', '12', 'SP3)'),('oracleasm', 'kmp'),('HTTP', 'Server'),('Apache', 'Struts'),('Apache', 'Commons'),('WebSphere', 'Application', 'Server', 'Admin' ,'Console'),
('WebSphere', 'Application', 'Server', 'Liberty'),('Apache', 'Commons' ,'HttpClient'),('WebSphere', 'Application', 'Server', 'Edge', 'Caching', 'Proxy'),
('Java', 'Server', 'Faces'),('Performance', 'Management' ,'product'),('Apache' ,'CXF'),('Rational', 'ClearQuest'),('Rational', 'ClearCase'),('Client', 'Management', 'Service'),('MQ.NET', 'Managed', 'Client'),('MQ', 'Appliance'),('MQ','PAM'),
('MQ' ,'Clients'),('Queue', 'Manager'),('GNU' ,'C' 'library'),('Process', 'Designer'),('Business', 'Automation', 'Workflow'),('Business', 'Process', 'Manager'),
('BigFix', 'Remote', 'Control'),('DataPower', 'Gateways'),('WebSphere', 'DataPower', 'XC10', 'Appliance'),('Adobe', 'Flash'),('Remote', 'Desktop', 'Protocol', '(RDP)', 'Denial', 'of', 'Service'),('bug', 'fix,'),
('Red', 'Hat')]
tokenizer = nltk.MWETokenizer(list_, separator=' ')
Abstract=df1['Abstract'].tolist()
keywords=[]
keywords_update=[]
for ab in Abstract:
	keywords.append(tokenizer.tokenize(ab.split()))
for key in keywords:
	keywords_=[re.split(',|\)|\(',k) for k in key]
	flat_list = [item for sublist in keywords_ for item in sublist]
	keywords_update.append(flat_list)
print(keywords_update)