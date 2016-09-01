import collections

import re
def getDiseasesFromSymptoms( symptoms , db ):

	AllDiseases = []
	for symptom in symptoms:
		val = re.compile(symptom.strip('\n\r\t '),re.IGNORECASE)
		#val=symptom
		#var regex = new RegExp(["^", symptom, "$"].join(""), "i");
		
		cursor = db.symptomsToDisease.find({ 'symptom':val})
		for c in cursor:
			AllDiseases.append( c['disease'])
	
	return  collections.Counter(AllDiseases)	

def getSymptomsFromDisease( disease , db ):

	AllSymptoms = []
	val = re.compile(disease.strip('\n\r\t '),re.IGNORECASE)
		#val=symptom
		#var regex = new RegExp(["^", symptom, "$"].join(""), "i");
		
	cursor = db.symptomsToDisease.find({ 'disease':val})
	for c in cursor:
		AllSymptoms.append( c['symptom'])
	
	return  collections.Counter(AllSymptoms)			
	