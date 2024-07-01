FROM sxk1633/lag-cli:v0.2 as lag
WORKDIR /
RUN lag clone https://lagrangedao.org/spaces/0x2D1EcD1A88aeE9Fb4CeB1F34C9cd7bE965c78C8D/Json-view && tar -zcf json-view.tar Json-view
FROM sxk1633/nodejs:14.21.3 as npm
WORKDIR /
COPY --from=lag /json-view.tar /
RUN tar -xf json-view.tar && cd Json-view/ && npm install && npm run build && tar -zcf dist.tar dist
FROM sxk1633/nginx:latest
COPY --from=npm /Json-view/dist.tar /
RUN tar -xf /dist.tar -C /usr/share/nginx/html && mv /usr/share/nginx/html/dist/* /usr/share/nginx/html
EXPOSE 80
