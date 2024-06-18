from ubuntu:22.04
RUN apt update
RUN apt install git -y 
RUN apt install python3 python3-pip -y
WORKDIR /app
RUN git clone https://github.com/lagrangedao/lagrange-cli.git
RUN cd lagrange-cli && pip install .
RUN rm -rf lagrange-cli 
COPY app.py .
RUN apt-get clean
ENTRYPOINT ["python3", "app.py"]
 

