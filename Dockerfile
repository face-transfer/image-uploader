FROM python:3.8 AS builder
RUN python -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install --user -r requirements.txt


FROM python:3.8-slim

COPY --from=builder /root/.local /root/.local
COPY . .
RUN  python -m pytest -m "not e2e" ./tests
ENV PATH=/root/.local:$PATH
WORKDIR /src

ENV AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY
ENV LOCAL_FILE=$LOCAL_FILE
ENV BUCKET=$BUCKET
ENV S3_FILE=$S3_FILE

CMD [ "python", "-m" , "image_uploader" ]
