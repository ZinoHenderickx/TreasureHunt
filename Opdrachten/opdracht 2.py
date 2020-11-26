import requests

# opdracht 3

my_string = "opdracht 3"
my_bytes = bytearray(my_string, "utf-8")
byte_list = []

x = requests.post('http://185.115.217.205:1234/opdracht3/' + my_bytes.hex())

result = x.text
print(result)

