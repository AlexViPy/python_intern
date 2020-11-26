FROM python:3.9
# Устанавливаем рабочую директорию
WORKDIR /app

# Копируются и устанавливаются необходимые зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn requests
# Копируем в образ файлы
WORKDIR /app
COPY . /app

CMD ["uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8001"]
