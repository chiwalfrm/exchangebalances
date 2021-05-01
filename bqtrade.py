from qtrade_client.api import QtradeAPI

# String is of the format "[key_id]:[key]"
hmac_keypair = "MY_API_KEY:MY_API_SECRET"
client = QtradeAPI("https://api.qtrade.io", key=hmac_keypair)
for element in client.balances_merged().items():
        if element[1] != 0:
                print(element[0].ljust(16), '{:.18f}'.format(element[1]).rjust(37).rstrip('0').rstrip('.'))
