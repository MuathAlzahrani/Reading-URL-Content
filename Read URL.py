import requests

r = requests.get('https://s-m.com.sa/')

print(r.text)
file = open("url Data.text", "w")
file.write(r.text)
file.close()
