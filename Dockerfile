# Використовуємо офіційний образ Python
FROM python:3.11-slim

# Встановлюємо змінні середовища
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файл залежностей
COPY requirements.txt /app/

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проєкт у контейнер
COPY . /app/