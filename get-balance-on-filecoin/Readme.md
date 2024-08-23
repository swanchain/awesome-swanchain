.

## Get Started

If you want to run a "get-balance-on-filecoin" docker project, please follow the steps below

## Build  Image

###

```shell
cd get-balance
docker build -t get-balance .
```

## Start a instance

```shell
 docker run -p 7860:7860 get-balance
```

Open the web page at http://0.0.0.0:7860, if success you can the following response

```json
{
            "chain_name": <<chain_name>>,
            "provider": "Fogmeta",
            "wallet": <<wallet>>,
            "balance": <<wallet_balance>>
        }}
```
