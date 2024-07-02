#!/bin/bash
cd /home/docker/data
random_number=$((RANDOM *RANDOM))
export WORKERNAME=$random_number
enableGPU=$enableGPU
if [ $enableGPU -eq 1 ]; then
    nohup ./aleo-miner -u $MINER_URL -w $ACCOUNTNAME.$WORKERNAME -d 0 >> ./aleo-miner.log 2>&1 &
    echo "nohup ./aleo-miner -u $MINER_URL -w $ACCOUNTNAME.$WORKERNAME -d 0 >> ./aleo-miner.log 2>&1 &" > ./aleo-miner.log
else
    nohup ./aleo-miner -u $MINER_URL -w $ACCOUNTNAME.$WORKERNAME  >> ./aleo-miner.log 2>&1 &
    echo "nohup ./aleo-miner -u $MINER_URL -w $ACCOUNTNAME.$WORKERNAME  >> ./aleo-miner.log 2>&1 &" > ./aleo-miner.log
fi
streamlit run run.py