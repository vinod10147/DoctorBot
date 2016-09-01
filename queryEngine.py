import nltk

import editDistance as ed

from nltk.util import ngrams

from nltk.stem.lancaster import LancasterStemmer

st = LancasterStemmer()

import re

import pickle

f = open("MedicalData")

AllWords = f.read().split('\n')

generalWords = ['symptoms','exams and tests','surgery','causes']

given = []

toFind = []

f = open('stopwords.txt')

stopwords = f.read().split(',');

mainDict = pickle.load(open('newDict'))

MedicalList = []





def askQuery():

	return raw_input("Enter your query ")

# return the tokens of the query

def tokenize( query ):

	return nltk.word_tokenize(query)	


def correctTokens( tokens ):

	#  permut + implement trie 
	pass



def filterTokens( tokens ):

	# remove stopwords
	filteredTokens = []
	for i in range(len(tokens)):
		if tokens[i]  not in stopwords:
			filteredTokens.append( tokens[i] ) 
	return filteredTokens

def reCorrectTokens( tokens ):

	# applying  edit distance
	for i in range(len(tokens)):
		tokens[i] =  ed.similarity( tokens[i] , AllWords ) 


def fMeasure(word1, word2):
	w1_c = [0]*256
	w2_c = [0]*256
	for i in word1:
		w1_c[ord(i)] += 1 
	for i in word2:
		w2_c[ord(i)] += 1
	matched_words = 0
	for i in xrange(256):
		matched_words += min(w1_c[i], w2_c[i])
	if (matched_words == 0):
		return 99999
	return (max(len(word1), len(word2)) / float(matched_words))		


def processQuery( tokens , flexibility):
	
	# for 4 to 2 grams
	for gram in range(4,1,-1):
		ngramsTokens = ngrams(tokens,gram) 
	#	print ngramsTokens
		for eachGram in ngramsTokens:
			key = reduce(lambda x,y :x+" "+y,eachGram)
			if key in mainDict:
				given.append((key,mainDict[key][0]))
			else:
				stemedkey = reduce(lambda x,y :st.stem(x)+" "+st.stem(y),eachGram)
				print key
				minimum = 9999999999
				for word in mainDict:
					w = reduce(lambda x,y :st.stem(x)+" "+st.stem(y),word.split())
					fValue = min(fMeasure( w.encode('ascii', 'ignore') , stemedkey ),fMeasure(word.encode('ascii', 'ignore'),key))
					if fValue < minimum:
						minimum = fValue
						matchedWord = word

				if minimum <= flexibility*gram:
					#print matchedWord
					given.append((matchedWord,mainDict[matchedWord][0]))

	
			
	# for 1 grams

	for key in tokens:
		if key in mainDict:
			given.append((key,mainDict[key][0]))
		else:
			newkey = st.stem(key)
			for word in generalWords:
				if word.count(newkey)!=0:
					toFind.append(word)


def findResult():
	for element in given:
		for find in set(toFind):
			print mainDict[element[0]][1][find]
					

	


query = askQuery()
print "tokenizing"
tokens = tokenize( query.lower() )
print tokens
print "Correcting tokens"
correctTokens(tokens)
print tokens
print "filering tokens"
tokens=filterTokens(tokens)
print tokens
print "recorrect"
reCorrectTokens( tokens )
print tokens
print "Processing Query"
flexibility=0.15
processQuery( tokens ,flexibility)

print "Given list:",given

print "To find list",toFind

findResult()
