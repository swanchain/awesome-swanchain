## Get Started 

If you want to run a "hello world" Docker project, please follow the steps below.

## Build Image

```shell
cd hello_world
docker build -t lad_hello_world .
```

## Start an Instance

```shell
docker run lad_hello_world
```
Open the web page at http://0.0.0.0:7860. If successful, you will see the following response:

```json
{
    "Hello": "World!"
}
```
