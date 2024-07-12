FROM sxk1633/nodejs:20.2.0
#Installation env dependent.
RUN DEBIAN_FRONTEND=noninteractive && apt update && apt install tzdata git yarn -y && git clone https://github.com/zkemail/proof-of-twitter.git && cd proof-of-twitter/ && git checkout origin/ui-updates 
WORKDIR /proof-of-twitter/packages/app
RUN yarn
EXPOSE 3000

ENTRYPOINT ["yarn", "start", "--host", "0.0.0.0"]
