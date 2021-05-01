import sys
import client2
from os import path
if len(sys.argv) < 2:
        print('ERROR: Must specify file containing api configuration.')
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
if my_api_subaccount != '':
        ftx = client2.FtxClient(api_key=my_api_key, api_secret=my_api_secret, subaccount_name=my_api_subaccount)
else:
        ftx = client2.FtxClient(api_key=my_api_key, api_secret=my_api_secret)
for element in ftx.get_balances():
        for key, value in element.items():
                if key == 'coin':
                        coin=value
                if key == 'total' and value != 0:
                        print(coin.ljust(16), '{0:.18f}'.format(value).rjust(37).rstrip('0').rstrip('.'))
