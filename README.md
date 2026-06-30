# Book API

Простое API для управления книгами и категориями

## Запуск

source venv/bin/activate - активировать виртуальное окружение
uvicorn app.main:app --reload - запустить сервер 

## Требования

- Python 3.8+
- PostgreSQL (установленный в WSL)
- Установленные зависимости из 'requirements.txt'

## Подробнее о запуске
Убедиться, что PostgreSQL запущен: sudo service postgresql start