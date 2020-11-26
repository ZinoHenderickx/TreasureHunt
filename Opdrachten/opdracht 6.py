import json
import hashlib
import requests
import secrets
import string

from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'Geheim bericht bestemd voor de docenten IoT aan de KdG'
key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)

print(data)
print(key.hex())
print(ciphertext.hex())
print(cipher.nonce.hex())

x = requests.post("http://185.115.217.205:1234/opdracht7", json={"bericht_versleuteld": ciphertext.hex(), "sleutel": key.hex(), "nonce": cipher.nonce.hex()})

result = x.text
print(result)

