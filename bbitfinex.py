import asyncio
import sys
from bfxapi import Client


async def get_wallets(bfx_api):
    sumwallets = 0
    wallets = await bfx_api.rest.get_wallets()
    positions = await bfx_api.rest.get_active_position()
    print("w / type / currency / balance / unsettled_interest / available")
    for my_wallet in wallets:
#        print("Type: " + str(my_wallet.type) + " Currency: " + str(my_wallet.currency) + " Balance: " + str(my_wallet.balance) + " Unsettled Interest: " + str(my_wallet.unsettled_interest))
        if len(sys.argv) > 1 and sys.argv[1] == 'futures':
            if my_wallet.type == 'margin':
                print("w / " + str(my_wallet.type).ljust(8) + " / " + str(my_wallet.currency).ljust(5) + " / " + str(my_wallet.balance).ljust(10) + " / " + str(my_wallet.unsettled_interest) + " / X")
                sumwallets = sumwallets + my_wallet.balance
        else:
            if my_wallet.type != 'margin':
                print("w / " + str(my_wallet.type).ljust(8) + " / " + str(my_wallet.currency).ljust(5) + " / " + str(my_wallet.balance).ljust(10) + " / " + str(my_wallet.unsettled_interest) + " / X")
                sumwallets = sumwallets + my_wallet.balance
    if len(sys.argv) > 1 and sys.argv[1] == 'futures':
        print()
        print("p / symbol / status / amount / base_price / margin_funding / margin_funding_type / profit_loss / profit_loss_percentage / liquidation_price / leverage / id / mts_create / mts_update / type / collateral / collateral_min / meta /  timestamp")
        for my_position in positions:
#            print("Active: " + str(my_position.status) + " Symbol: " + str(my_position.symbol) + " Amount: " + str(my_position.amount) + " Base Price: " + str(my_position.base_price) + " Profit/Loss: " + str(my_position.profit_loss))
            print("p / " + str(my_position.symbol) + " / " + str(my_position.status) + " / " + str(my_position.amount) + " / " + str(my_position.base_price) + " / " + str(my_position.margin_funding) + " / " + str(my_position.margin_funding_type) + " / " + str(my_position.profit_loss) + " / " + str(my_position.profit_loss_percentage) + " / " + str(my_position.liquidation_price) + " / " + str(my_position.leverage) + " / " + str(my_position.id) + " / " + str(my_position.mts_create) + " / " + str(my_position.mts_update) + " / " + str(my_position.type) + " / " + str(my_position.collateral) + " / " + str(my_position.collateral_min) + " / " + str(my_position.meta) + " / X")
            sumwallets = sumwallets + my_position.profit_loss
        print()
        print("Balance:", '{0:.18f}'.format(float(sumwallets)).rstrip('0').rstrip('.'))


bfx = Client("API_KEY_GOES_HERE", "API_SECRET_GOES_HERE")
async_run = asyncio.ensure_future(get_wallets(bfx))
asyncio.get_event_loop().run_until_complete(async_run)
