FROM python:3.11

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
        gcc \
        python3-dev \
        musl-dev \
        netcat-traditional \
        dos2unix \
        gettext \
    && pip install --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock* /app/
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh \
    && sed -i 's/\r$//' entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
