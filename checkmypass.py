import requests
import hashlib


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error Fetching: {res.status_code}, checking')
    return res


def pwned_api_check(password):
    # Check if it is in API
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    # sha1password = hashlib.sha1(password.encode('utf-8'))
    return sha1password


pwned_api_check('123')
