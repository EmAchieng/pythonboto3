FROM python:3.13.0rc2-slim AS base

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS test
CMD ["pytest", "./tests"]

FROM base AS prod

EXPOSE 80
CMD ["python", "./modules/main.py"]
