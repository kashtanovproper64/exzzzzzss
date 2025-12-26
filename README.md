# Django To-Do API

CRUD API для управления задачами с Django REST Framework

## Функциональность
- Создание, чтение, обновление, удаление задач
- Поля: название, описание, статус, приоритет, срок выполнения
- Фильтрация по статусу и приоритету
- Сортировка по различным полям

## Установка

1. Клонируйте репозиторий:
```bash
git clone <url-репозитория>
cd django-todo-api
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Примените миграции:
```bash
python manage.py migrate
```

5. Запустите сервер:
```bash
python manage.py runserver
```

## API Endpoints

- GET `/api/todos/` - список всех задач
- POST `/api/todos/` - создать задачу
- GET `/api/todos/{id}/` - получить задачу по ID
- PUT/PATCH `/api/todos/{id}/` - обновить задачу
- DELETE `/api/todos/{id}/` - удалить задачу

## Примеры запросов

Создание задачи:
```bash
curl -X POST http://localhost:8000/api/todos/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Тестовая задача"}'
```

Фильтрация по статусу:
```bash
curl "http://localhost:8000/api/todos/?status=completed"
```

## Автор
[Ваше имя]
