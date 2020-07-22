  import requests

r = requests.get('https://twitter.com/', timeout=0.5)

print(r.content)
print(r.status_code)
print(r.headers)