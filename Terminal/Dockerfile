FROM ubuntu:latest

RUN  apt update && apt install wget -y && wget https://github.com/tsl0922/ttyd/releases/download/1.4.0/ttyd_linux.x86_64 && mv ttyd* /usr/local/bin/ttyd && chmod +x /usr/local/bin/ttyd



EXPOSE 8080

ENTRYPOINT ["ttyd", "--port", "8080", "/bin/bash"]
