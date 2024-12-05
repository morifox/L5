# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы в контейнер
COPY . /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порты (например, 8001)
EXPOSE 8001

# Запускаем сервер Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
