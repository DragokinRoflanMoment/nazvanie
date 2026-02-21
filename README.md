# nazvanie
Гайд на запуск api
1 Клонировать репозиторий

2 Создать виртуальное окружение и активировать
python3 -m venv venv
source venv/bin/activate для WSL Ubuntu

3 Установить зависимости
pip install -r requirements.txt

4 Заполнить файл .env по следующему шаблону:
DB_HOST=*хост*
DB_PORT=*порт*
DB_NAME=*название БД*
DB_USER=*имя пользователя*
DB_PASSWORD=*пароль*

5 Создать БД
python3 -m app.db.init_db

6 Запуск FastAPI
uvicorn app.main:app --reload

7 Проверить работу через http://127.0.0.1:8000/docs
и http://127.0.0.1:8000/health, в health должно выдать "status : ok"

