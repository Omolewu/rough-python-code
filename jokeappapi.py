import requests
from termcolor import colored
import pyfiglet

arttext=pyfiglet.figlet_format('Dad joke Arena')
joke=input('Enter your prefer joke ')
limit=input('How many jokes? ')
welcome=colored(arttext, color='green')
print(welcome)

response = requests.get('https://icanhazdadjoke.com/search',
                        headers={'Accept': 'application/json'},
                        params={
                            'term': joke,
                            'limit': '2'
                      })
apiquery=response.json()

# print(apiquery['results'])
i=1
for jokelist in apiquery['results']:
    if jokelist['joke']:
        print(f"\n{i} {jokelist['joke']}")
    else:
        print('No joke related to your searched word')
     