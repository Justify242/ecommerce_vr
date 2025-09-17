FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHON UNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=ecommerce_vr.settings

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000