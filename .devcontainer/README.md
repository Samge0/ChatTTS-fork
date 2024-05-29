## docker of chattts-dev

### build docker
```shell
docker build . -t samge/chattts-dev-base -f .devcontainer/Dockerfile-dev-base --build-arg PROXY=http://192.168.50.48:7890
```

### upload
```shell
docker push samge/chattts-dev-base
```

### run .devcontainer/devcontainer.json