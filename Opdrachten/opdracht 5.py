import hashlib
import requests
import urllib.request
import sys
import os

# URL = "http://185.115.217.205:1234"

# right_checksum = "5f2a5c31a292cc46bacf546c961a8424"


checksum = "5f2a5c31a292cc46bacf546c961a8424"

url = 'https://http://185.115.217.205:1234/static/opdracht5/applicatie_george.exe'
r = requests.get(url, allow_redirects=True)

open('', 'wb').write(r.content)

with open("/static/opdracht5/applicatie_george.exe", "rb") as f:
    file_hash = hashlib.md5()
    chunk = f.read(8192)
    while chunk:
        file_hash.update(chunk)
        chunk = f.read(8192)
    if chunk == checksum:
        print("right file")
    else: 
        print("wrong file")

# with open("applicatie_ivonne.exe", "rb") as f:
#     file_hash = hashlib.md5()
#     chunk = f.read(8192)
#     while chunk:
#         file_hash.update(chunk)
#         chunk = f.read(8192)
#     if chunk == checksum:
#         print("right file")

# with open("applicatie_jef.exe", "rb") as f:
#     file_hash = hashlib.md5()
#     chunk = f.read(8192)
#     while chunk:
#         file_hash.update(chunk)
#         chunk = f.read(8192)
#     if chunk == checksum:
#         print("right file")

# with open("applicatie_jos.exe", "rb") as f:
#     file_hash = hashlib.md5()
#     chunk = f.read(8192)
#     while chunk:
#         file_hash.update(chunk)
#         chunk = f.read(8192)
#     if chunk == checksum:
#         print("right file")

# with open("applicatie_mariette.exe", "rb") as f:
#     file_hash = hashlib.md5()
#     chunk = f.read(8192)
#     while chunk:
#         file_hash.update(chunk)
#         chunk = f.read(8192)
#     if chunk == checksum:
#         print("right file")

# with open("applicatie_odilon.exe", "rb") as f:
#     file_hash = hashlib.md5()
#     chunk = f.read(8192)
#     while chunk:
#         file_hash.update(chunk)
#         chunk = f.read(8192)
#     if chunk == checksum:
#         print("right file")
        

# print(file_hash.hexdigest())



# for file in exe:
#     exe_name = file[18:]
#     urllib.request.urlretrieve(URL + file,
#                                os.getcwd() + "/" + exe_name)  # Download file and store it in current directory.
#     hasher = hashlib.md5()
#     with open(exe_name, 'rb') as open_file:
#         content = open_file.read()
#         hasher.update(content)
#     if hasher.hexdigest() == right_checksum:
#         correct_file = exe_name

# right_file = "/static/opdracht5/" + correct_file
# x = requests.post(URL + "/opdracht6", json={"relatieve_url": right_file})
# result = x.text
# print(result)