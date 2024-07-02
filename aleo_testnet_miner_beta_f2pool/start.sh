#!/bin/bash
cd /home/docker/data
random_number=$((RANDOM *RANDOM))
export WORKERNAME=$random_number
nohup ./aleo-miner -u $MINER_URL -w $ACCOUNTNAME.$WORKERNAME -d 0 >> ./aleo-miner.log 2>&1 &
streamlit run run.py