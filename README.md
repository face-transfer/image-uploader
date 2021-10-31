# image_uploader-app

## build docker image
```
# docker build -t image_uploader-app .
```
## run docker image
```
# docker run  --env-file .env  -v ~/dev/tikal/reassigment/face-transfer-image-uploader/tests/resources/:/tests/resources/ image_uploader-app
```
