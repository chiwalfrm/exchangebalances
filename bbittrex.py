from bittrex.bittrex import *
my_bittrex = Bittrex("MY_API_KEY", "MY_API_SECRET", api_version="v2.0")
for element in my_bittrex.get_balances()['result']:
        coin = element['Balance'].items()
        coinname = ''
        for key, value in coin:
                if key == 'Currency':
                        coinname = value
                if coinname != 'BTXCRD' and key == 'Balance' and value != 0:
                        print(coinname.ljust(16), '{0:.18f}'.format(value).rjust(37).rstrip('0').rstrip('.'))
