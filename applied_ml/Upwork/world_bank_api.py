import urllib.request
import json
from bs4 import BeautifulSoup

#token = ""
#api_Key = 'e8b1d567e935e45ae0e76ab087d898390f27f52eb96e84687c18fa5e085a1fa8'
#secret = '20b6186772d2972389b46c7408b4a6e166a61f42ca9fb27f42051186ff2e9760'
import json
from urllib.request import urlopen
def getCountry(request_url):
	response = urlopen(request_url).read().decode('utf-8')
	responseJson = json.loads(response)
	return responseJson
print(getCountry('http://api.worldbank.org/countries/all/indicators/SP.POP.TOTL?date=2000:2001&format=json'))


'''request_url = 'http://api.worldbank.org/countries/all/indicators/SP.POP.TOTL?date=2000:2001'

req = urllib.request.Request(request_url)
#f = urllib.request.urlopen(req)
#webRequest = urllib.request.urlopen('https://api.change.org/v1/petitions/get_id?api_key=e8b1d567e935e45ae0e76ab087d898390f27f52eb96e84687c18fa5e085a1fa8&petition_url=https://www.change.org/p/stop-cbd-from-becoming-a-schedule-1-drug?source_location=petitions_share_skip').read()
html = urllib.request.urlopen(req).read().decode('utf-8')

responseJson = json.loads(html)

soup = BeautifulSoup(html, 'lxml')
print(responseJson)'''