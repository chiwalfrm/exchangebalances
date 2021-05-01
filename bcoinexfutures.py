#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
from lib import CoinexPerpetualApi


# Replace it with your own API key.
access_id = 'xxx'
secret_key = 'xxx'


if __name__ == "__main__":
    robot = CoinexPerpetualApi(access_id, secret_key)
    for key, value in robot.query_account()['data'].items():
        sum = float(value['balance_total']) + float(value['margin']) + float(value['profit_unreal'])
        if float(sum) > 0:
            print(key.ljust(16), '{:.18f}'.format(sum).rjust(37).rstrip('0').rstrip('.'))
#
#    print(json.dumps(robot.ping(), indent=4))
#
#    print(json.dumps(robot.get_market_info(), indent=4))
#
#    result = robot.put_limit_order(
#        'BTCUSD',
#        robot.ORDER_DIRECTION_BUY,
#        10,
#        6000
#    )
#    print(json.dumps(result, indent=4))
