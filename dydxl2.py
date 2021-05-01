from dydx3 import Client
from dydx3 import private_key_to_public_key_pair_hex
from dydx3.constants import API_HOST_ROPSTEN, API_HOST_MAINNET
from dydx3.constants import NETWORK_ID_ROPSTEN, NETWORK_ID_MAINNET
from dydx3.errors import DydxApiError
from web3 import Web3
import pickle


if __name__ == "__main__":
################################# Settings ##############################################
    ETHEREUM_ADDRESS = "0xADDRESS"
    ETH_PRIVATE_KEY = "PRIVATEKEY"  # Set to None if you decide to use an ETH node instead of a private key

    #  geth --ropsten --syncmode "full" --http --rpc --rpcapi="db,eth,net,web3,personal,web3" --rpcaddr "localhost" --rpcport "8545"  # This *SHOULD* work for starting a local ETH node with GETH. run it in a command prompt seperately
    WEB_PROVIDER_URL = "http://localhost:8545"  # RPC connection, only needed when you are running a ETH node

#    testing = True  # Use the ropsten testing network instead of the main ETH network
    testing = False  # Use the ropsten testing network instead of the main ETH network
##########################################################################################

    if ETH_PRIVATE_KEY == "None":
        ETH_PRIVATE_KEY = None

    if testing:
        API_HOST = API_HOST_ROPSTEN
        NETWORK_ID = NETWORK_ID_ROPSTEN
    else:
        API_HOST = API_HOST_MAINNET
        NETWORK_ID = NETWORK_ID_MAINNET

    public_client1 = Client(
        host=API_HOST,
    )

    # print(public_client1.public.get_markets())  # Get DYDX exchange market info as a dictionary

    if ETH_PRIVATE_KEY:
        client = Client(
            network_id=NETWORK_ID,
            host=API_HOST,
            eth_private_key=ETH_PRIVATE_KEY,
            default_ethereum_address=ETHEREUM_ADDRESS,
        )
    else:
        client = Client(
            network_id=NETWORK_ID,
            host=API_HOST,
            default_ethereum_address=ETHEREUM_ADDRESS,
            web3=Web3(Web3.HTTPProvider(WEB_PROVIDER_URL)),
        )

    # Set STARK key.
    stark_private_key = client.onboarding.derive_stark_key()
    client.stark_private_key = stark_private_key
    public_x, public_y = private_key_to_public_key_pair_hex(stark_private_key)
    try:
        onboarded_users = pickle.load(open("onboarded_users.data", "rb"))
    except:
        onboarded_users = []

    if client.stark_private_key not in onboarded_users:
        # Onboard the account.
        try:
            onboarding_response = client.onboarding.create_user(
                stark_public_key=public_x,
                stark_public_key_y_coordinate=public_y,
            )
            #print('onboarding_response', onboarding_response)
            onboarded_users.append(client.stark_private_key)
            pickle.dump(onboarded_users, open("onboarded_users.data", "wb"))
        except Exception as e:
            if "User wallet has no transactions, Ethereum or USDC" in str(e):
                print("User wallet has no transactions, Ethereum or USDC")
                while True:
                    input()
            else:
#                print("User already created!\n\n")
                onboarded_users.append(client.stark_private_key)
                pickle.dump(onboarded_users, open("onboarded_users.data", "wb"))
    else:
#        print("User already created!\n\n")
        pass

    # Query a private endpoint.
    try:
        accounts_response = client.private.get_accounts()
        #print('accounts_response', accounts_response)

#        print("Accounts: \n")
        for account in accounts_response["accounts"]:
#            print("accountNumber: " + account["accountNumber"])
#            print("id: " + account["id"])
#            print("starkKey: " + account["starkKey"])
#            print("positionId: " + account["positionId"])
#            print("equity: " + account["equity"])
            print(account["equity"])
#            print("freeCollateral: " + account["freeCollateral"])
#            print("pendingDeposits: " + account["pendingDeposits"])
#            print("pendingWithdrawals: " + account["pendingWithdrawals"])
#            for open_pos in account["openPositions"]:
#                print(str(open_pos) + " : " + str(account["openPositions"][open_pos]))
#            print("quoteBalance: " + account["quoteBalance"])
#            print("\n" * 1)
    except DydxApiError:
        print("API key not found")
#    while True:
#        input()
