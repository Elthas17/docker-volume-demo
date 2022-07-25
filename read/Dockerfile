FROM python:3.9.13-slim-bullseye
ARG SERVICENAME=NoServiceSet
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./app /app

RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r requirements.txt

CMD [ "python", "main.py"]