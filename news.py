import requests

response = requests.get('https://g1.globo.com/')

print('Status code', response.status_code)
print(' Header ')
print(response.headers)

print('\n Content ')
print(response.content)
