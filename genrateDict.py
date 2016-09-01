
import pickle

f = open('newDict')

d = pickle.load(f)

for key in d:
	l = key.replace('-',' ').split()
	for i in l:
		print i.encode('ascii', 'ignore')