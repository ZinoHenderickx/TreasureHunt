import hashlib
import requests

input = 'Dit is een testbestand voor opdracht 4!'
hash = hashlib.sha512( str( input ).encode("utf-8") ).hexdigest()
print(hash)

sha512 =   {
        "sha512"   :   "f5769ebe4a14f646aaa7ddcb4d76327278ec671338bf577d9bb465d26e48f9311d031dccb3a8148c9abdaf48deabf9b068adafbb779f32c687dfcf5e92244faf"
    }

x = requests.post("http://185.115.217.205:1234/opdracht5", json=sha512)

print(x.text)