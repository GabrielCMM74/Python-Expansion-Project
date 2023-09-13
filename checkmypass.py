import requests

url = 'https://api.pwnedpasswords.com/range/' + 'passwords'
res = requests.get(url)
print(res)
