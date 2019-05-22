import os
import pandas as pd
import nltk
import math
abst_l = df1['Abstract'].tolist()
keys_l = df1['Keys'].tolist()
df2 = pd.DataFrame(columns=['Words','Tags'])
Words =[]
Tags=[]
i=0
for ab,key in zip(abst_l,keys_l):
	i+=1
	Abst_sub=[]
	keys_sub=[]
	tokenized = nltk.word_tokenize(ab)
	for w in tokenized:
		if type(key) == str:
			if str(w) in key:
				keys_sub.append('I-APP')
			else:
				keys_sub.append('O\n')
		else:
			keys_sub.append('O\n')
	Words.append(tokenized)
	Tags.append(keys_sub)
df2['Words']=Words
df2['Tags']=Tags
df2 = df2.sample(frac=1).reset_index(drop=True)
df2.to_excel('Linux_Words_tags.xlsx')





