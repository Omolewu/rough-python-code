import requests
import pdb
# r = requests.get('https://news.ycombinator.com/')
# print(r.status_code)
# print(r.ok)
# print(r.headers)
# r = requests.get('https://oichub.org')
# print(r.status_code)
# print(r.ok)
# print(r.headers)
# print(r.text)
url = 'https://icanhazdadjoke.com/'
# response =requests.get(url, headers={'Accept': 'text/plain'})
response =requests.get(url, headers={'Accept': 'application/json'})
print(response.status_code)
print(response.text)
print(response.json())
data =response.json()
print(data['joke'])
# print(response.text)