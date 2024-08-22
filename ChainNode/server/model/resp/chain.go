package resp

type ChainDataResp struct {
	Name     string `json:"name"`
	Chain    string `json:"chain"`
	Net      string `json:"net"`
	ChainID  string `json:"chain_id"`
	Currency string `json:"currency"`
	URL      string `json:"url"`
	Token    string `json:"token"`
	Height   int    `json:"height"`
	Latency  int    `json:"latency"`
	Status   int    `json:"status"`
	Icon     string `json:"icon"`
}

type ChainResp struct {
	Chain    string `json:"chain"`
	Net      string `json:"net"`
	ChainID  string `json:"chain_id"`
	Currency string `json:"currency"`
	Icon     string `json:"icon"`
}
