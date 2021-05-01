import requests
import sys
from decimal import *
if len(sys.argv) < 2:
        print("ERROR: Must specify Ethereum address.")
        exit()
request = requests.get("https://api.dydx.exchange/v1/accounts/" + sys.argv[1]).json()
for key, value in request['accounts'][0]['confirmedBalances'].items():
        if key == '0':
                symbol = 'WETH'
        elif key == '1':
                symbol = 'SAI'
        elif key == '2':
                symbol = 'USDC'
        elif key == '3':
                symbol = 'DAI'
        if float(value['wei']) != 0:
                print(symbol.ljust(16), '{0:.18f}'.format(float(value['wei']) / float(Decimal(10 ** 18))).rjust(37).rstrip('0').rstrip('.'))
