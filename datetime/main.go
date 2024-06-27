package main

import (
	"html/template"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

func formatAsDate(t time.Time) string {
	return t.Format("2006-01-02 15:04:05 -0700 MST")
}

func main() {
	router := gin.Default()
	router.Delims("{[{", "}]}")
	router.SetFuncMap(template.FuncMap{
		"formatAsDate": formatAsDate,
	})
	router.LoadHTMLFiles("./raw.tmpl")

	router.GET("/", func(c *gin.Context) {
		c.HTML(http.StatusOK, "raw.tmpl", gin.H{
			"now": time.Now(),
		})
	})

	router.Run(":8080")
}
