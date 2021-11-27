# Multistage Dockerfile

## On a M1:
```bash

# to build
docker build --platform linux/x86_64 . -t docker-image-tools:0.1

# to run
docker run --platform linux/x86_64 -dit docker-imate-tools:0.1


```