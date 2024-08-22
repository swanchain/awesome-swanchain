package router

import (
	v1 "chain-report-server/api/v1"
	"time"

	"github.com/cloudwego/hertz/pkg/app/server"
	"github.com/hertz-contrib/cors"
)

var Router *server.Hertz

func init() {
	Router = server.Default()
	Router.Use(cors.New(cors.Config{
		AllowOrigins:     []string{"*"},
		AllowMethods:     []string{"GET", "POST", "HEAD", "PUT", "PATCH", "DELETE", "OPTIONS"}, // Allowed request methods
		AllowCredentials: true,                                                                 // Whether cookies are attached
		MaxAge:           12 * time.Hour,                                                       // Maximum length of upload_file-side cache preflash requests (seconds)
	}))
	chain := new(v1.ChainApi)
	Router.POST("/chains", chain.Report)
	Router.GET("/chains", chain.ListChain)
	Router.GET("/chains/:id", chain.List)
	Router.Static("/static", "./")
	Router.Static("/static/css", "static/dist")
	Router.Static("/img", "static/dist")
	Router.StaticFile("/", "static/dist/index.html")
	Router.Static("/js", "static/dist")
	Router.Static("/css", "static/dist")
	Router.Static("/app.ec52c655ac1e83efa8a9.js", "static/dist")
	Router.Static("favicon.ico", "static/dist")
	// Router.GET("/", func(ctx context.Context, c *app.RequestContext) {
	// 	c.Redirect(consts.StatusMovedPermanently, []byte("/static/dist/index.html"))
	// })
}
