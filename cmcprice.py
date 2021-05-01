import json
import sys
from os import path
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
if len(sys.argv) < 4:
        print("ERROR: Must specify apifile, cryptocurrency, and base.")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
parameters = {'slug':sys.argv[2],'convert':sys.argv[3]}
headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': my_api_key}
session = Session()
session.headers.update(headers)
try:
        response = session.get(url, params=parameters)
        for key, value in json.loads(response.text)['data'].items():
                print(value['quote'][sys.argv[3]]['price'])
except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
