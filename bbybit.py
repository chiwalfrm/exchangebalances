import bybit
client = bybit.bybit(test=False, api_key='YOUR_API_KEY', api_secret='YOUR_API_SECRET')
symbols = []
for element in client.Symbol.Symbol_get().result()[0]['result']:
        symbols.append(element.get('base_currency'))
symbols = sorted(list(set(symbols)))
for element in symbols:
        equity = client.Wallet.Wallet_getBalance(coin=element).result()[0]['result']
        if str(equity) != "None":
                equity2 = equity.get(element).get('equity')
                if equity2 != 0:
                        print(element.ljust(16), '{:.18f}'.format(equity2).rjust(37).rstrip('0').rstrip('.'))
