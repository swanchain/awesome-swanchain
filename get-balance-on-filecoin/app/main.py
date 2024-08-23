from fastapi import FastAPI
import sys
from web3 import Web3, HTTPProvider
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    chain_name = "filecoin_testnet"
    try:
        w3 = Web3(HTTPProvider('https://rpc.ankr.com/' + chain_name))
    except:
        print("[!] WARNING: INVALID HTTPProvider ('web3' env variable)")
        sys.exit("NOPE")

    wallet = '0x96216849c49358B10257cb55b28eA603c874b05E'

    wallet_balance = w3.eth.get_balance(wallet)
    return {"data":
        {
            "chain_name": chain_name,
            "provider": "Fogmeta",
            "wallet": wallet,
            "balance": wallet_balance
        }}
