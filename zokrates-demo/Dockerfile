FROM sxk1633/lag-cli:v0.2 as lag
WORKDIR /
RUN lag clone https://lagrangedao.org/spaces/0x129ddcdA5B114c05d4932CC553535Ef3cC9201D5/zokrates-demo && tar -zcf zokrates-demo.tar zokrates-demo
FROM python:3.9
ENV DEBIAN_FRONTEND=noninteractive
COPY --from=lag /zokrates-demo.tar /
RUN tar -xf zokrates-demo.tar && cd zokrates-demo
WORKDIR zokrates-demo
RUN pip install --no-cache-dir flask
EXPOSE 5002

ENTRYPOINT ["python", "app.py"]