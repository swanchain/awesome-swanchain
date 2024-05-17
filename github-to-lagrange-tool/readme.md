Build docker image


`docker build . -t github-to-lagrange-tool`

exec : 

`docker run -it --rm  github-to-lagrange-tool `

result :

```Error: Incorrect number of arguments
[+] Usage: docker run -it --rm github-to-lagrange-tool <wallet> <lagrange-api> <lagrange-space>   <github-url>

[+] ex: docker run -it --rm github-to-lagrange-tool 0x72b4952E1b1e6D318101314acB4517bA99264e70 xxxx awesome-swanchain https://github.com/swanchain/awesome-swanchain
```

clone awsesome-swanchain from github to lagrange

`docker run -it --rm github-to-lagrange-tool 0x72b4952E1b1e6D318101314acB4517bA99264e70 xxxxxx awesome-swanchain https://github.com/swanchain/awesome-swanchain`


```[+] wallet: 0x72b4952E1b1e6D318101314acB4517bA99264e70

[+] Lagrange API: xxxxxx

[+] Lagrange Space: awesome-swanchain

[+] GitHub URL: https://github.com/swanchain/awesome-swanchain

[+] configure lagrange-cli

[+] donwload github repo

Cloning into 'workshop'...

remote: Enumerating objects: 138, done.

remote: Counting objects: 100% (138/138), done.

remote: Compressing objects: 100% (115/115), done.

remote: Total 138 (delta 49), reused 55 (delta 10), pack-reused 0

Receiving objects: 100% (138/138), 128.65 KiB | 1.04 MiB/s, done.

Resolving deltas: 100% (49/49), done.

[+] init lagrange repo

Cloning awesome-swanchain into current directory...

[+] copy files to lagrange dir

[+] remove git file

[+] add and commit

[+] push to lagrange

Uploading files to space...

Push to awesome-swanchain complete.

```


done !!!

url :

`https://lagrangedao.org/spaces/0x72b4952E1b1e6D318101314acB4517bA99264e70/awesome-swanchain/files`
