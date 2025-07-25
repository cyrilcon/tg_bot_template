FROM python:3.13-slim

WORKDIR /usr/src/app

COPY pyproject.toml uv.lock* ./

RUN pip install uv && uv pip install . --system

COPY . .
