package main

import (
	"chain-report-server/router"
	"chain-report-server/service"
	"log"
)

func main() {
	log.SetFlags(log.LstdFlags | log.Lshortfile)
	service.StartCronService()
	router.Router.Spin()
}
