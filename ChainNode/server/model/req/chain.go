package req

type ChainReportReq struct {
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
}
