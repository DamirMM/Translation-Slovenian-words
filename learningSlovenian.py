import requests
import json

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
text = input("enter the word : ")

payload = "q=" + text + "&target=ru&source=sl"
payload = "q=" + text + "&target=sl&source=ru"
headers = {
    "content-type": "application/x-www-form-urlencoded",
    "Accept-Encoding": "application/gzip",
    "X-RapidAPI-Key": "a71fb91a78msh2b907940678c168p1c4174jsn9d851e261b05",
    "X-RapidAPI-Host": "google-translate1.p.rapid.com"
}

response = requests.request("POST", url, data=payload.encode("utf-8"), headers=headers)
data = json.loads(response.text)
data = data["data"]["translations"][0]["translatedText"]
print(data)
