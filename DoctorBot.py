from scrapper import *

from query import *

from dbController import *
import pickle
import requests
import pymongo 
import sys
import re
import urllib.parse # import urlparse
from bs4 import BeautifulSoup
from pymongo import MongoClient
reload(sys)

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client.DoctorBotDBV2

symptoms_url =  "https://www.umms.org/ummc/patients-visitors/health-library/medical-encyclopedia/symptoms?c=c"

disease_url = "https://www.umms.org/ummc/patients-visitors/health-library/medical-encyclopedia/diseases?c=c"

test_url = "https://www.umms.org/ummc/patients-visitors/health-library/medical-encyclopedia/tests?c=c"

surgery_url = "https://www.umms.org/ummc/patients-visitors/health-library/medical-encyclopedia/surgery?c=c"

 #ExtractSymptomsOrDiseasesOrTestList(symptoms_url);

MedicalData = {}

print ("extracting Disease List")
ExtractList(disease_url , MedicalData , 'd')

print ("extracting Symptoms List")
ExtractList(symptoms_url , MedicalData , 's')

print ("extracting Test List")
ExtractList(test_url , MedicalData , 't' )

print ("extracting surgery List")
ExtractList(surgery_url , MedicalData , 'u' )

ContentUrl = "https://www.nlm.nih.gov/medlineplus/ency/encyclopedia_"

print ("Crawling data")

CrawlData( ContentUrl , MedicalData )

print ("Adding into Database")

f = open("newDict",'w')

pickle.dump(MedicalData, f, pickle.HIGHEST_PROTOCOL)



#AddingIntoDB( MedicalData , db )

# s = raw_input("Enter Diseases")


# l = dict(getDiseasesFromSymptoms(s.split(":"),db)).items()

# l.sort(key=lambda x:x[1],reverse=True)
# l = dict(getSymptomsFromDisease(s,db)).items()

# l.sort(key=lambda x:x[1],reverse=True)
#print l


#print DiseaseNamesList
