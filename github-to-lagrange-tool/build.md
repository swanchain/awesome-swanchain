[+] Building 1.7s (16/16) FINISHED                                                                                                     docker:default
 => [internal] load .dockerignore                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                  0.0s
 => [internal] load build definition from Dockerfile                                                                                             0.0s
 => => transferring dockerfile: 399B                                                                                                             0.0s
 => [internal] load metadata for docker.io/library/ubuntu:22.04                                                                                  1.1s
 => [auth] library/ubuntu:pull token for registry-1.docker.io                                                                                    0.0s
 => [ 1/10] FROM docker.io/library/ubuntu:22.04@sha256:a6d2b38300ce017add71440577d5b0a90460d0e57fd7aec21dd0d1b0761bbfb2                          0.0s
 => [internal] load build context                                                                                                                0.0s
 => => transferring context: 1.77kB                                                                                                              0.0s
 => CACHED [ 2/10] RUN apt update                                                                                                                0.0s
 => CACHED [ 3/10] RUN apt install git -y                                                                                                        0.0s
 => CACHED [ 4/10] RUN apt install python3 python3-pip -y                                                                                        0.0s
 => CACHED [ 5/10] WORKDIR /app                                                                                                                  0.0s
 => CACHED [ 6/10] RUN git clone https://github.com/lagrangedao/lagrange-cli.git                                                                 0.0s
 => CACHED [ 7/10] RUN cd lagrange-cli && pip install .                                                                                          0.0s
 => CACHED [ 8/10] RUN rm -rf lagrange-cli                                                                                                       0.0s
 => [ 9/10] COPY app.py .                                                                                                                        0.1s
 => [10/10] RUN apt-get clean                                                                                                                    0.3s
 => exporting to image                                                                                                                           0.1s
 => => exporting layers                                                                                                                          0.1s
 => => writing image sha256:f1b0d6e8abeecaf0d6a6e5c4644375dc180a4ae06f8257e5c973ab52119936b1                                                     0.0s
 => => naming to docker.io/library/github-to-lagrange-tool                                                                                       0.0s
