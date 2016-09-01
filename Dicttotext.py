import pickle
import sys
import codecs
reload(sys)

sys.setdefaultencoding("utf-8")

f=open('newDict')
D=pickle.load(f)

f=open('Medicaltext',"w")
s=""
for item in D:
	print item
	if len(D[item])>1:
		for key in D[item][1]:	
			s+=D[item][1][key][0]
		
f.write(s.encode('utf8'))
f.close()