# BDC-Geoserver-Spec

## Build Documentation

### Requirements

- [NodeJS 8+](https://nodejs.org/en/)
- [ReDoc](https://github.com/Redocly/redoc)
- [Docker](https://docs.docker.com/get-started/) (OPTIONAL)

Execute the following command to install `node modules` dependencies:

```bash
npm install
```

After that, generate BDC_Geoserver documentation:

```bash
npm run build
```

It will create folder `dist` with a bundled file `index.html`. You may serve this file with HTTP Server.

### Docker

You can also run the documentation with docker.

To serve documentation, use the following command:

```bash
docker run --interactive \
           --tty \
           --rm \
           --name redoc \
           --publish 8080:80 \
           --volume $(pwd)/api/v1.0/bdc_geoserver.yaml:/usr/share/nginx/html/bdc_geoserver.yaml \
           --env SPEC_URL=bdc_geoserver.yaml redocly/redoc
```

To generate documentation, you must build `redoc-cli` manually. Open in another terminal and run the following commands:

```bash
git clone https://github.com/Redocly/redoc/
cd redoc/cli
docker build --network=host --tag redoc-cli .
exit
```

After that, execute the following commands (**Make sure** you are in `geoserver/spec` folder):

```bash
docker run --rm \
           --interactive \
           --tty \
           --name redoccli \
           --volume $(pwd)/api/v1.0/bdc_geoserver.yaml:/bdc_geoserver.yaml \
           --volume $(pwd)/dist:/dist redoc-cli bundle /bdc_geoserver.yaml --output /dist/index.html
```

**Note** that the generated folder `dist` may have root permission. In order to fix it, use:

```bash
sudo chown ${USER}:${USER} -R dist
```
