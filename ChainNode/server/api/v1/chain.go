package v1

import (
	"chain-report-server/api"
	"chain-report-server/model/req"
	"chain-report-server/model/resp"
	"chain-report-server/service"
	"context"
	"net/http"
	"strings"
	"time"

	"github.com/cloudwego/hertz/pkg/app"
)

var chainService = new(service.ChainService)

type ChainApi struct {
	api.BaseApi
}

func (api *ChainApi) Report(c context.Context, ctx *app.RequestContext) {
	var req req.ChainReportReq
	if err := api.ParseReq(ctx, &req); err != nil {
		return
	}
	err := chainService.Report(&service.ChainData{
		Name:       req.Name,
		Chain:      req.Chain,
		Net:        req.Net,
		ChainID:    req.ChainID,
		Currency:   req.Currency,
		URL:        req.URL,
		Token:      req.Token,
		Height:     req.Height,
		Latency:    req.Latency,
		Status:     req.Status,
		ActiveTime: time.Now().Unix(),
	})
	if err != nil {
		api.ErrResponse(ctx, http.StatusInternalServerError, err)
		return
	}
	ctx.Response.SetStatusCode(http.StatusOK)
}

func (api *ChainApi) List(c context.Context, ctx *app.RequestContext) {
	id, _ := ctx.Params.Get("id")
	dataList, err := chainService.List(id)
	if err != nil {
		api.ErrResponse(ctx, http.StatusInternalServerError, err)
		return
	}
	list := make([]*resp.ChainDataResp, 0, len(dataList))
	for _, data := range dataList {
		name := strings.ToLower(data.Chain)
		list = append(list, &resp.ChainDataResp{
			Name:     data.Name,
			Chain:    data.Chain,
			Net:      data.Net,
			ChainID:  data.ChainID,
			Currency: data.Currency,
			URL:      data.URL,
			Token:    data.Token,
			Height:   data.Height,
			Latency:  data.Latency,
			Status:   data.Status,
			Icon:     service.ChainIconPrefix + service.ChainIcons[name],
		})
	}
	api.Response(ctx, list)
}

func (api *ChainApi) ListChain(c context.Context, ctx *app.RequestContext) {
	dataList, err := chainService.ListChain()
	if err != nil {
		api.ErrResponse(ctx, http.StatusInternalServerError, err)
		return
	}
	list := make([]*resp.ChainResp, 0, len(dataList))
	for _, data := range dataList {
		name := strings.ToLower(data.Chain)
		list = append(list, &resp.ChainResp{
			Chain:    data.Chain,
			Net:      data.Net,
			ChainID:  data.ChainID,
			Currency: data.Currency,
			Icon:     service.ChainIconPrefix + service.ChainIcons[name],
		})
	}
	api.Response(ctx, list)
}
