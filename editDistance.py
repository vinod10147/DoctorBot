#from nltk import edit_distance

from nltk import metrics

from nltk.stem.lancaster import LancasterStemmer

st = LancasterStemmer()


def editDistance(word1, word2):
	len_1=len(word1)

	len_2=len(word2)

	x =[[0]*(len_2+1) for _ in range(len_1+1)] # the matrix whose last element ->edit distance

	for i in range(0,len_1+1): # initialization of base case values

	    x[i][0]=i
	for j in range(0,len_2+1):

	    x[0][j]=j
	
	for i in range (1,len_1+1):


	    for j in range(1,len_2+1):

	        if word1[i-1]==word2[j-1]:
	            x[i][j] = x[i-1][j-1] 

	        else :
	            x[i][j]= min(x[i][j-1],x[i-1][j],x[i-1][j-1])+1

	return x[i][j]

def similarity( word , AllWords ):
	minDist = 999999
	matchedWord = ""
	inr=0
	tword=word
	ln = len(word)
	for i in range(ln):
		
		for eachWord in AllWords:

			dist =inr + min(editDistance(st.stem(tword),st.stem(eachWord)),editDistance(tword,eachWord))
			if dist==0:
					return eachWord
			if dist < minDist:
				minDist = dist
				matchedWord = eachWord
		if i !=ln-1:
			tword=word[0:i]+word[i+1]+word[i]+word[i+2:]
		inr=1
	return matchedWord			

#print similarity('tuber')

#print similarity('whch')

#print similarity('tuberculos')
