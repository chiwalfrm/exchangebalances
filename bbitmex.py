import bitmex
client = bitmex.bitmex(test=False, api_key='YOUR_API_KEY', api_secret='YOUR_API_SECRET')
print('Futures marginBalance:', float(client.User.User_getMargin().result()[0]['marginBalance']/100000000), 'BTC')
