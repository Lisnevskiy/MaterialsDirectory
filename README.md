# Materials Directory API

## Описание

**Materials Directory API** — это REST API для управления справочником материалов и категорий. API позволяет:
- Создавать, читать, обновлять и удалять материалы и категории.
- Загрузить данные о материалах из файла `.xlsx`.
- Просматривать дерево категорий с подсчетом общей стоимости материалов.
- Получать категории в виде плоского списка.

## 🚀 Функциональные возможности

### 1. Материалы
- **CRUD-операции**: создание, чтение, обновление, удаление.
- **Загрузка из файла**: импорт данных материалов из `.xlsx`.

### 2. Категории
- **CRUD-операции**: создание, чтение, обновление, удаление.
- **Иерархическое представление**: категории в виде дерева с подсчетом общей стоимости материалов.
- **Плоское представление**: категории с материалами в виде списка.

## 📋 Технологический стек

- **Python**
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **openpyxl** (для работы с .xlsx)

## 🛠 Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/Lisnevskiy/MaterialsDirectory.git
```

### 2. Установка зависимостей

Убедитесь, что у вас установлен [Pipenv](https://pipenv.pypa.io/en/latest/). Установите зависимости:

```bash
pipenv install
```

### 3. Настройка переменных окружения

Создайте файл `.env` в корневой директории и добавьте необходимые переменные окружения, примеры которых, указаны в файле .env.sample

### 4. Применение миграций

Примените миграции базы данных:

```bash
python manage.py migrate
```

### 5. Запуск сервера

Запустите сервер разработки:

```bash
python manage.py runserver
```

Приложение будет доступно по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## 🔄 API Endpoints

Материалы

* GET /api/materials/ - Получить список всех материалов
* POST /api/materials/ - Создать новый материал
* GET /api/materials/{id}/ - Получить детали материала
* PUT /api/materials/{id}/ - Обновить материал
* DELETE /api/materials/{id}/ - Удалить материал
* POST /api/materials/upload/ - Загрузить данные из .xlsx

Категории
* GET /api/categories/ - Получить список категорий
* POST /api/categories/ - Создать новую категорию
* GET /api/categories/{id}/ - Получить детали категории
* PUT /api/categories/{id}/ - Обновить категорию
* DELETE /api/categories/{id}/ - Удалить категорию
* ET /api/categories/flat/ - Плоский список категорий
* GET /api/categories/tree/ - Дерево категорий с материалами

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь со мной по адресу [lisnevskiy14@gmail.com](mailto:lisnevskiy14@gmail.com).