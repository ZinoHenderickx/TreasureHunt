import hashlib
import requests
import urllib.request
import sys
import os

URL = "http://185.115.217.205:1234"

checksum = "5f2a5c31a292cc46bacf546c961a8424"

exes = ["/static/opdracht5/applicatie_jos.exe",
         "/static/opdracht5/applicatie_jef.exe",
         "/static/opdracht5/applicatie_odilon.exe",
         "/static/opdracht5/applicatie_george.exe",
         "/static/opdracht5/applicatie_mariette.exe",
         "/static/opdracht5/applicatie_ivonne.exe"]

for file in exes:
    application_name = file[18:]
    hasher = hashlib.md5()
    with open(application_name, 'rb') as open_file:
        content = open_file.read()
        hasher.update(content)
    if hasher.hexdigest() == checksum:
        right_exe = application_name

right_exe_path = "/static/opdracht5/" + right_exe
x = requests.post(URL + "/opdracht6", json={"relatieve_url": right_exe_path})
result = x.text
print(result)