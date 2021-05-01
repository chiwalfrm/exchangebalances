import json
import sys
from os import path
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
#pp = pprint.PrettyPrinter(width=41, compact=True)
if len(sys.argv) < 2:
        print("ERROR: Must specify apifile.")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {'limit':'10'}
headers = {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': my_api_key}
session = Session()
session.headers.update(headers)
try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)['data']
        for element in data:
                for key, value in element.items():
                        if key == 'quote':
                                price = value['USD']['price']
                        if key == 'symbol':
                                symbol = value
                print(symbol.ljust(4), '{:,.18f}'.format(float(price)).rjust(37).rstrip('0').rstrip('.'))
except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
