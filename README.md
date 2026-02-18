# nazvanie
Гайд на запуск api
1 Клонировать репозиторий

2 Создать виртуальное окружение и активировать
python3 -m venv venv
source venv/bin/activate для WSL Ubuntu

3 Установить зависимости
pip install -r requirements.txt

4 Создать БД
python3 -m app.db.init_db

5 Запуск FastAPI
uvicorn app.main:app --reload

6 Проверить работу через http://127.0.0.1:8000/docs
и http://127.0.0.1:8000/health, в health должно выдать "status : ok"

