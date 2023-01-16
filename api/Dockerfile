# INSTRUCTION arguments
FROM python:3.10.8-slim-bullseye

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . /code

EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
