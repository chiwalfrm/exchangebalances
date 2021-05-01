from coinbase.wallet.client import Client
client = Client('MY_API_KEY', 'MY_API_SECRET')
for coin in client.get_accounts(limit=100)['data']:
        coinbalance = list(coin['balance'].values())
        if float(coinbalance[0]) != 0:
                print(coinbalance[1].ljust(16), '{0:.18f}'.format(float(coinbalance[0])).rjust(37).rstrip('0').rstrip('.'))
