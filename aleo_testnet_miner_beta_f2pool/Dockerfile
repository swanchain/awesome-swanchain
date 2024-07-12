FROM harleyluka/aleo_testnet_beta:0.01
USER root
COPY ./start.sh /home/docker/data
COPY ./aleo-miner.log /home/docker/data
COPY ./aleo-miner /home/docker/data
COPY ./aleo.sh /home/docker/data
COPY ./run.py /home/docker/data
RUN chmod +x /home/docker/data/start.sh
CMD ["/home/docker/data/start.sh"]
