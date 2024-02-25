FROM python:3.11

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y libpq-dev gcc python3-dev musl-dev netcat-traditional dos2unix gettext \
    flake8 locales

WORKDIR /app

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY . .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh \
    && sed -i 's/\r$//' entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]

