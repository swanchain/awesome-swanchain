.

## Get Started

If you want to run a "hello world" docker project, please follow the steps below

## Build  Image

###

```shell
cd hello_world
docker build -t lad_hello_world .
```

## Start a instance

```shell
 docker run -p 7860:7860 lad_hello_world 
```

Open the web page at http://0.0.0.0:7860, if success you can the following response

```json
{
  "Hello": "World!"
}
```
