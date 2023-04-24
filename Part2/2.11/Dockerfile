FROM python:3.11-slim-bullseye

EXPOSE 80

WORKDIR /usr/src/app/

ADD ./requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "fibonacci:app", "--host", "0.0.0.0", "--reload"]