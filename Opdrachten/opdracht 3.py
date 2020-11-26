import base64
import requests

my_string = "opdracht 4 lijkt heel erg op opdracht 3"
my_bytes = my_string.encode("utf-8")


print(base64.b64encode(my_bytes).decode("utf-8"))

x = requests.post('http://185.115.217.205:1234/opdracht4/' + base64.b64encode(my_bytes).decode("utf-8"))

result = x.text
print(result)
