FROM golang:1.22
WORKDIR /usr/src/app
COPY . .
RUN go mod download && go mod verify
RUN go build -o app main.go
EXPOSE 8080
CMD ["./app"]