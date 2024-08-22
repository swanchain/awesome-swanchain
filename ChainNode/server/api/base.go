package api

import (
	"log/slog"
	"net/http"

	"chain-report-server/api/result"

	"github.com/cloudwego/hertz/pkg/app"
)

type BaseApi struct{}

func (a *BaseApi) UID(c *app.RequestContext) int {
	return c.GetInt("uid")
}

func (api *BaseApi) ParseReq(c *app.RequestContext, receiverPointer any) error {
	if err := c.BindAndValidate(receiverPointer); err != nil {
		slog.Error("validate", "error", err)
		c.AbortWithError(http.StatusBadRequest, err)
		return err
	}
	return nil
}

func (api *BaseApi) Response(c *app.RequestContext, data any) {
	api.response(c, result.Result{
		Code: result.Success,
		Data: data,
		Msg:  "success",
	})
}

func (api *BaseApi) response(c *app.RequestContext, data any, statusCode ...int) {
	code := http.StatusOK
	if len(statusCode) > 0 {
		code = statusCode[0]
	}
	c.JSON(code, data)
}

func (api *BaseApi) ErrResponse(c *app.RequestContext, code int, err error, statusCode ...int) {
	status := http.StatusBadRequest
	if len(statusCode) > 0 {
		status = statusCode[0]
	}
	res := result.Result{
		Code: code,
		Msg:  err.Error(),
	}
	api.response(c, res, status)
}

func (api *BaseApi) InnerErrResponse(c *app.RequestContext, code int, err error, statusCode ...int) {
	status := http.StatusInternalServerError
	if len(statusCode) > 0 {
		status = statusCode[0]
	}
	res := result.Result{
		Code: code,
		Msg:  err.Error(),
	}
	api.response(c, res, status)
}
