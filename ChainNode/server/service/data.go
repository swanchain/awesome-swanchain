package service

import "sync"

type ChainData struct {
	Name       string `json:"name"`
	Chain      string `json:"chain"`
	Net        string `json:"net"`
	ChainID    string `json:"chain_id"`
	Currency   string `json:"currency"`
	URL        string `json:"url"`
	Token      string `json:"token"`
	Height     int    `json:"height"`
	Latency    int    `json:"latency"`
	Status     int    `json:"status"`
	ActiveTime int64  `json:"active_time"`
}

var lotusDataMap sync.Map

const ChainIconPrefix = "/static/icons/"

var ChainIcons = map[string]string{
	"aptos":               "aptos.png",
	"arbitrum":            "arbitrum.svg",
	"avalanche":           "avalanche.png",
	"binance smart chain": "bsc.png",
	"ethereum":            "ethereum.png",
	"filecoin":            "filecoin.png",
	"near":                "near.png",
	"optimism":            "optimism.png",
	"pocket":              "pocket.png",
	"polygon":             "polygon.png",
	"sui":                 "sui.png",
	"bsc":                 "bsc.png",
}
