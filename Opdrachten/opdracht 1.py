import requests

opdracht =  {
        "nr1"   :   "Eerste regel",
        "nr2"   :   "Tweede regel",
        "nr3"   :   "Derde regel"
    }

x = requests.post("http://185.115.217.205:1234/opdracht2", json=opdracht)

print(x.text)