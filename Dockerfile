FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y curl build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get clean
ENV PATH="/root/.local/bin:$PATH"
# Configure Poetry to not use virtual environments
RUN poetry config virtualenvs.create false

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

COPY . /app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
