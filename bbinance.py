import sys
from os import path
from binance.client import Client
if len(sys.argv) < 2:
        print("ERROR: Must specify file containing api configuration.")
        print("Optional arguments: 'crossmargin', 'isolatedmargin', 'futures'")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
bclient = Client(my_api_key, my_api_secret)
if len(sys.argv) > 2 and sys.argv[2] == 'crossmargin':
        crossassets = bclient.get_margin_account()
        for asset in crossassets['userAssets']:
                if float(asset['netAsset']) != 0:
                        print(asset['asset'], asset['netAsset'])
        print('totalNetAssetOfBtc:', crossassets['totalNetAssetOfBtc'], 'BTC')
elif len(sys.argv) > 2 and sys.argv[2] == 'isolatedmargin':
        assets=bclient.get_isolated_margin_account()['assets']
        if assets:
                print(assets[0]['baseAsset']['asset'], str(assets[0]['baseAsset']['netAsset'] + ' = ' + assets[0]['baseAsset']['netAssetOfBtc'] + ' BTC').rjust(30))
                print(assets[0]['quoteAsset']['asset'], str(assets[0]['quoteAsset']['netAsset'] + ' BTC').rjust(30))
                print('totalNetAssetOfBtc:', bclient.get_isolated_margin_account()['totalNetAssetOfBtc'], 'BTC')
        else:
                print('totalNetAssetOfBtc: 0 BTC')
elif len(sys.argv) > 2 and sys.argv[2] == 'futures':
        print('Futures totalMarginBalance:', '{:,}'.format(round(float(bclient.futures_account()['totalMarginBalance']),2)), 'USDT')
else:
        print('asset                         total 123456789012345678')
        for element in bclient.get_account()['balances']:
                if float(element.get('free')) > 0 or float(element.get('locked')) > 0 :
                        print(element.get('asset').ljust(16), '{0:.18f}'.format(float(element.get('free')) + float(element.get('locked'))).rjust(37).rstrip('0').rstrip('.'))
