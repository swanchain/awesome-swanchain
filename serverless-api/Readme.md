## Get Started 

If you want to run a "serverless api" docker project, please follow the steps below

## Build  Image


###
```shell
cd serverless-api
docker build -t serverless-api .
```
## Start a instance

```shell
 docker run serverless-api
```

Open the web page at http://0.0.0.0:7860, if success you can the following response 

```json
{
    "ping": "pong"
}
```