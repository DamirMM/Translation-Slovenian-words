import requests
import json


url = "https://random-words5.p.rapidapi.com/getMultipleRandom"

querystring = {"count":"7"}

headers = {
	"X-RapidAPI-Key": "a71fb91a78msh2b907940678c168p1c4174jsn9d851e261b05",
	"X-RapidAPI-Host": "random-words5.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text)

print(data)

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
headers = {
		"content-type": "application/x-www-form-urlencoded",
		"Accept-Encoding": "application/gzip",
		"X-RapidAPI-Key": "a71fb91a78msh2b907940678c168p1c4174jsn9d851e261b05",
		"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
	}
for word in data:
	payload = "q="+word + "&target=ru&source=en"
	response = requests.request("POST", url, data=payload.encode("utf-8"), headers=headers)
	data = json.loads(response.text)
	data = data["data"]["translations"][0]["translatedText"]
	print(data, end=" ")

	payload = "q=" + word + "&target=sl&source=en"
	response = requests.request("POST", url, data=payload.encode("utf-8"), headers=headers)
	data = json.loads(response.text)
	data = data["data"]["translations"][0]["translatedText"]
	print(data)