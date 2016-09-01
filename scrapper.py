import requests
import pymongo 
import sys
import re
import urlparse
from bs4 import BeautifulSoup
reload(sys)


# url = "http://umm.edu/health/medical/ency/symptoms?c=B"

def ExtractList( url , MedicalData , ch ):

	
	leftUrl =url;
	for i in range(26):
		print "extracting ",chr(65+i) , ch
		url = leftUrl + chr(65+i)
		req = requests.get(url)
		if req.status_code == 200:
			soup = BeautifulSoup(req.content,"lxml")
			categories = soup.find_all("ul", {"class": "letter"})
			for category in categories:
				links = category.find_all("a")
				for link in links:
					MedicalData[link.text.lower()] = [ch]



def CrawlData( url , MedicalData ):

	
	leftUrl =url;
	for i in range(26):
		print "Crawling ",chr(65+i)
		url = leftUrl + chr(65+i) + ".htm"
		req = requests.get(url)
		if req.status_code == 200:
			soup = BeautifulSoup(req.content,"lxml")
			categories = soup.find_all("ul", {"id": "index"})
			for category in categories:
				links = category.find_all("a")
				for link in links:

					if link.text.lower() in MedicalData.keys():
						print link.text
						data  = {}
						newUrl = urlparse.urljoin(req.url, link.get("href"))
						ExtractData( newUrl, data ,MedicalData )
						MedicalData[link.text.lower()].append(data)
						

def ExtractData( url , data , MedicalData ):

	
	req = requests.get(url)
	if req.status_code == 200:
		soup = BeautifulSoup(req.content,"lxml")
		content = soup.find("div", {"id": "d-article"})
		description = content.find("div",{"id":"ency_summary"})
		sections = content.find_all("div",{"class":"section"})
		for section in sections:
			sectionHeader = section.find("div",{"class":"section-header"}).text.strip('\t\r\n ').lower()
			sectionBody = section.find("div",{"class":"section-body"})
			
			#sectionBody = sectionBody.findAll()
			#print sectionBody
			
			InSection = sectionBody.find_all( recursive=False)

			#print secti
			textBetweenTags = ""
			referenceList = sectionBody.find_all("a")
			references = []
			count=0
			for reference in referenceList:
				if reference.text.lower() in MedicalData:
					count+=1
					references.append(reference.text.lower())
			print "\tSection Header", sectionHeader,"references count",count
			for eachElement in  InSection:
				
				if str(eachElement).find("<p>") >= 0 :
					textBetweenTags += eachElement.text + "\n"
				elif str(eachElement).find("<ul>") >= 0 :
					listItems = eachElement.find_all("li")
					for item in listItems:
						if item.text.lower() in MedicalData:
							references.append(item.text.lower()) 
						textBetweenTags += item.text + "\n"
					

			data[ sectionHeader ] = textBetweenTags,references

	else:
		print url		

			
			

		






	

			


				
		



# url = "https://www.nlm.nih.gov/medlineplus/ency/encyclopedia_"
#def Spider(	url ):

	

	
