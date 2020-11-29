FROM python:3.9
# Устанавливаем рабочую директорию
WORKDIR /app

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
ENV PORT 8001

# Копируются и устанавливаются необходимые зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
# Копируем в образ файлы
COPY . /app

CMD gunicorn main:app -b :$PORT -w 4 -k uvicorn.workers.UvicornH11Worker
