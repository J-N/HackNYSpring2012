#!pythonpath

import json
import re

def parseJSONnytimes(jsonobject, mode):

	#turn jsonobject into type dict
	data = json.loads(jsonobject)

	if (mode == 'article'):
	
		length = len(data['results'])

		#make empty 2d array with 3 columns
		infoList = [[] for j in range(3)]

		#add title, url, and date to each row
		for i in range(length):
			infoList[0].append(data['results'][i]['title'])
			infoList[1].append(data['results'][i]['url'])
			infoList[2].append(data['results'][i]['date'])
		for list in infoList:
			for string in list:
				# Unicode and whitespace tab vs space is stupid. Seriously
				string = string.encode('utf-8')
	elif (mode == 'semantic'):
	
		infoList = data['results'][0]['pages']
		for string in list:
			# Unicode and whitespace tab vs space is stupid. Seriously
			string = string.encode('utf-8')
	return infoList
	
def parseJSONlyrics(jsonobject):

	#turn jsonobject into type dict
	data = json.loads(jsonobject)
	
	length = len(data['response']['docs'])
	
	#define empty list
	titleList = []
	
	#if there are less than 5 articles returned, use all of them
	if length < 5:
		for i in range(length):
			titleList.append(data['response']['docs'][i]['title'])
	
	#if there are more than 5 articles returned, only use the first 5
	else:
		for i in range(5):
			titleList.append(data['response']['docs'][i]['title'])
	
	#get rid of all '\xa0' in the titles		
	listLength = len(titleList)
	for i in range(listLength):
		match = re.search('\xa0', titleList[i])
		if match:
			titleList[i] = titleList[i].replace(u'\xa0', ' ')
		titleList[i] = titleList[i].encode('utf-8')
			
	return titleList