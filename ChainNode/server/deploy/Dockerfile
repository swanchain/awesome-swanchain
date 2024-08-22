FROM ubuntu:22.04
RUN apt-get update && apt-get upgrade -y
RUN apt-get install libssl-dev
RUN apt-get install -y -q build-essential curl wget nginx
WORKDIR /lotus
RUN wget https://go.dev/dl/go1.21.1.linux-amd64.tar.gz
RUN rm -rf /usr/local/go && tar -C /usr/local -xzf go1.21.1.linux-amd64.tar.gz && rm -f go1.21.1.linux-amd64.tar.gz
ENV PATH /usr/local/go/bin:$PATH
ENV GOPATH /go
ENV PATH $GOPATH/bin:$PATH
COPY server server
RUN cp -r server/static .
RUN cp -r server/deploy/* .
RUN cd server && go mod tidy && go build -o ../chain-report-server && cd ../ && rm -rf server
EXPOSE 80
ENTRYPOINT ["bash", "./run.sh"]