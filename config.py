import os

from dotenv import load_dotenv

from urllib.parse import urlparse


load_dotenv(override=True)

DEBUG = str(os.getenv("DEBUG", "false")) == "true"

# --- Конфигурация базы данных --- #
DB_HOST = str(os.getenv("DB_HOST"))
DB_PORT = str(os.getenv("DB_PORT"))
DB_USER = str(os.getenv("DB_USER"))
DB_PASS = str(os.getenv("DB_PASS"))
DB_NAME = str(os.getenv("DB_NAME"))

TRUSTED_ORIGINS = [
    url.strip() for url in str(
        os.getenv("TRUSTED_ORIGINS", "http://localhost:3000, http://127.0.0.1:3000, http://localhost:8000")
    ).split(",")
]

HOSTS = os.getenv("HOSTS", "localhost:8000").split(",")
ALLOWED_HOSTS = HOSTS if len(HOSTS) > 0 else [urlparse(url).hostname for url in TRUSTED_ORIGINS]
CSRF_TRUSTED_ORIGINS = TRUSTED_ORIGINS

EMAIL_HOST = str(os.getenv("EMAIL_HOST", "smtp.gmail.com"))
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_HOST_USER = str(os.getenv("EMAIL_HOST_USER"))
EMAIL_HOST_PASSWORD = str(os.getenv("EMAIL_HOST_PASSWORD"))

REDIS_HOST = str(os.getenv("REDIS_HOST", "localhost"))
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))