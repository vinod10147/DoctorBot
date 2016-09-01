#[key][1] means dictionary
#[key][0] means 's' or 'd'
def AddingIntoDB( MedicalData , db):

	for key in MedicalData:
		if len(MedicalData[key]) > 1 :
			
			TempDict = {}
			TempDict["_id"] = key
			TempDict["value"] = MedicalData[key]


			if MedicalData[key][0] == 's':
				print "Adding Symptom" + key,
				db['symptomCollection'].insert_one(TempDict)
				
				if 'Causes' in MedicalData[key][1]:
					TempList = MedicalData[key][1]['Causes'][1]
					for l in TempList:
						TempDictForSTD = {}
						
						if  MedicalData[l][0] == 'd' :
							
							TempDictForSTD['disease'] = l
							TempDictForSTD['symptom'] = key
							db['symptomsToDisease'].insert_one(TempDictForSTD)
							print "Added"


			elif MedicalData[key][0] == 'd':
				print "Adding Disease" + key,
				db['diseaseCollection'].insert_one(TempDict)
				if 'Symptoms' in MedicalData[key][1]:
					
					TempList = MedicalData[key][1]['Symptoms'][1]
					
					for l in TempList:
						TempDictForSTD = {}
						
						if  MedicalData[l][0] == 's' :
							
							TempDictForSTD['symptom'] = l
							TempDictForSTD['disease'] = key
							db['symptomsToDisease'].insert_one(TempDictForSTD)
							print "Added"

				if 'Exams and Tests' in MedicalData[key][1]:
					
					TempList = MedicalData[key][1]['Exams and Tests'][1]
					
					for l in TempList:
						# disease to test
						TempDictForDT = {}
						
						if  MedicalData[l][0] == 't' :
							print '%$$%^$^',l,key
							TempDictForDT['test'] = l
							TempDictForDT['disease'] = key
							db['testToDisease'].insert_one(TempDictForDT)
							print "Added 1"			





			elif MedicalData[key][0] == 't':
				print "Adding test" + key,
				db['testCollection'].insert_one(TempDict)
				#print key
					
				# 	MedicalData[key][1]['Symptoms'][1] contains refrence list
				# MedicalData[key][1]['Symptoms'][0] contains data 

				if 'Why the Procedure is Performed' in MedicalData[key][1]:
					
					TempList = MedicalData[key][1]['Why the Procedure is Performed'][1]
				
					for l in TempList:
						TempDictForDT = {}
						
						if  MedicalData[l][0] == 'd' :
							print l,key
							TempDictForDT['disease'] = l
							TempDictForDT['test'] = key
							db['testToDisease'].insert_one(TempDictForDT)
							print "Added 2" 	

			elif MedicalData[key][0] == 'u':
				print "Adding Disease" + key,
				db['surgeryCollection'].insert_one(TempDict)
				#print key
				# 	MedicalData[key][1]['Symptoms'][1] contains refrence list
				# MedicalData[key][1]['Symptoms'][0] contains data 

				