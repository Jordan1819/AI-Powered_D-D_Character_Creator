FROM python:3.13-slim-bullseye

ARG POETRY_VERSION=1.8.2
ARG POETRY_DOWNLOAD_URL=https://install.python-poetry.org
ENV PATH="$PATH:/root/.local/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
  && apt-get install -y --no-install-recommends --no-install-suggests -y \
    curl \
    git \
    bash \
  && ln -sf /bin/bash /bin/sh \
  && curl -sSL $POETRY_DOWNLOAD_URL | python3 - --version $POETRY_VERSION

WORKDIR /app
COPY . .

RUN poetry add quart
RUN poetry install 

EXPOSE 80

CMD ["poetry", "run", "python", "web_app.py"]
