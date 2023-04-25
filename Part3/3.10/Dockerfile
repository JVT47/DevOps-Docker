FROM python:3.11-slim-bullseye

EXPOSE 80

WORKDIR /usr/src/app/

ADD ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    adduser appuser

COPY . .

USER appuser

CMD ["uvicorn", "fibonacci:app", "--host", "0.0.0.0", "--reload"]