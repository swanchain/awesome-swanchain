# zokrates-demo

**Lagrange RUN URL**
https://lagrangedao.org/spaces/0x129ddcdA5B114c05d4932CC553535Ef3cC9201D5/zokrates-demo/app
![image](https://github.com/blockchain315/awesome-swanchain/assets/173136503/e54ab99b-514c-4eaa-8a07-34b58f26b8c6)


ZoKrates is a toolbox for zkSNARKs on Ethereum. This is a proof-of-concept implementation. It has not been tested for production.

This is a demo for developer to use zokrates;

## Getting Started
Load the ZoKrates Plugin on [Remix](https://remix.ethereum.org) to write your first SNARK program!

Alternatively, you can install the ZoKrates CLI:

```bash
curl -LSfs get.zokrat.es | sh
```

Have a look at the [documentation](https://zokrates.github.io/) for more information about using ZoKrates.
[Get started](https://zokrates.github.io/gettingstarted.html), then try a [tutorial](https://zokrates.github.io/examples/rng_tutorial.html)!

## How to Run this Demo

```commandline
git clone https://github.com/example/repo.git
```

### Install Dependency
```commandline
curl -LSfs get.zokrat.es | sh
```
copy `zokrates` to `/usr/local/bin/`

```commandline
sudo apt update
sudo apt install python3
pip install --upgrade pip
pip install flask
```
### Start the process
```commandline
cd zok
python app.py
```
The zok service will listen `5002` port, you can visit `http://127.0.0.1:5002`
