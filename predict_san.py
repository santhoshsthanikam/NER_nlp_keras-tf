import numpy as np 
from validation import compute_f1
from keras.models import Model
from keras.layers import TimeDistributed,Conv1D,Dense,Embedding,Input,Dropout,LSTM,Bidirectional,MaxPooling1D,Flatten,concatenate
from San_pre import createMatrices,addCharInformatioin,padding
from keras.utils import Progbar
from keras.preprocessing.sequence import pad_sequences
from keras.initializers import RandomUniform
from keras.models import model_from_json
#from keras import backend as K
import nltk
import pickle
import pandas as pd
#sent='sree is a language'
label2Idx = {}
word2Idx = {}
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights("model.h5")
with open('label2Idx.pickle', 'rb') as handle2:
	label2Idx = pickle.load(handle2)

with open('filename.pickle', 'rb') as handle:
	word2Idx = pickle.load(handle)
def model_predict(sent):
	words = []
	sent_word=nltk.word_tokenize(sent)
	testSentences = [sent_word]
	testSentences = addCharInformatioin(testSentences)
	case2Idx = {'numeric': 0, 'allLower':1, 'allUpper':2, 'initialUpper':3, 'other':4, 'mainly_numeric':5, 'contains_digit': 6, 'PADDING_TOKEN':7}
	caseEmbeddings = np.identity(len(case2Idx), dtype='float32')
	char2Idx = {"PADDING":0, "UNKNOWN":1}
	for c in " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,-_()[]{}!?:;#'\"/\\%$`&=*+@^~|ó\x96":
		char2Idx[c] = len(char2Idx)
	test_set = padding(createMatrices(testSentences, word2Idx,case2Idx,char2Idx))
	idx2Label = {v: k for k, v in label2Idx.items()}
	"""
	json_file = open('model.json', 'r')
	loaded_model_json = json_file.read()
	json_file.close()
	model = model_from_json(loaded_model_json)
	model.load_weights("model.h5")
	"""
	predLabels = []
	for i,data in enumerate(test_set):
		tokens, casing,char = data
		tokens = np.asarray([tokens])
		casing = np.asarray([casing])
		char = np.asarray([char])
		pred = model.predict([tokens, casing,char], verbose=False)[0]   
		pred = pred.argmax(axis=-1) #Predict the classes            
		predLabels.append(pred)
	label_correct = []
	for sentence in predLabels:
		label_correct.append([idx2Label[element] for element in sentence])
	#print(label_correct)
	lis = np.array([j for i in label_correct for j in i])
	sent_word=nltk.word_tokenize(sent)
	indices = np.where(lis=='B-APP')[0]
	if indices.size !=0:
		for i in indices:
			if (lis.item(i+1)) == 'M-APP':
				words.append(sent_word[i]+' '+sent_word[i+1]+' '+sent_word[i+2])
			if (lis.item(i+1)) == 'E-APP':
				words.append(sent_word[i] +' '+sent_word[i+1])
	indices =np.where(lis =='I-APP')[0]
	if len(indices) !=0:
		for i in indices:
			words.append(sent_word[i])
	indices = np.where(lis =='I-MIDD')[0]
	if indices.size !=0:
		for i in indices:
			words.append(sent_word[i])
	indices = np.where(lis =='I-MISC')[0]
	if indices.size !=0:
		for i in indices:
			words.append(sent_word[i])
	words = [w for w in words if w != '-' or w != ',`']
	return(words)


df1 = pd.read_excel('Ab_Words_NAE_Tags.xlsx')
abstract = df1['Abstract'].tolist()
for ab in abstract:
	print(ab)
	print(model_predict(ab))
