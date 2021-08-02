# import termcolor2, pyfiglet
# available_colors=['red', 'blue', 'yellow', 'white', 'green']
# user_statement=input("What do you have to say?")
# arttext=pyfiglet.figlet_format(user_statement)
# print("Available Colours: Red, Blue, Yellow, White, green")
# colour=input('PLease input your preferred colour')
# if colour in available_colors:
#     print(termcolor2.colored(arttext, colour))
# else:
#     print('The colour you entered is not available')
#     colour=input('PLease input your preferred colour')
#     print(termcolor2.colored(arttext, colour))

users_joke=input('Kindly enter your jokes term')
max_joke=input('Maximun jokes you want?')
import requests
response = requests.get('https://icanhazdadjoke.com/search',
                        headers={
                            'ACCept' : "application/json"
                        },
                        params={
                            'term':users_joke,
                            'limit': 10
                        })
joke=response.json()
jokes =joke['results']
i= 1
for joke in jokes:
    print(f"No {i}: {joke['joke']}")
    i=i+1

# print(f"Today's joke is: {joke['joke']} with id number: {joke['id']}")
# print(response.ok)
