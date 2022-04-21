# Генератор промо кодов
## Инструкция по развертыванию проекта

Склонировать репозиторий: 
```bash
git clone https://github.com/viktornikolaev1995/generator_promo_codes.git
```

### Настройка проекта

Перейти в папку проекта: `cd generator_promo_codes`

Внесите при необходимости корректировки в переменные окружения, находящиеся в файле `.env`

### Сборка образов и запуск контейнеров

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

При первом запуске данный процесс может занять несколько минут.

```bash
docker-compose exec app python manage.py createsuperuser
```

К API есть документация по адресу http://127.0.0.1:8000/redoc/, http://127.0.0.1:8000/swagger/

### Для просмотра запущенных контейнеров

```bash
docker-compose ps
```

### Для просмотра списка образов

```bash
docker-compose images
```

### Для просмотра журнала сервисов

```bash
docker-compose logs -f app
```

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

### Остановка контейнеров с последующим их удалением

Для остановки и удаления контейнеров выполните команду:

```bash
docker-compose down
```

***Нижеследующие команды выполняются при запущенных контейнерах и в той же директории, где запускались контейнеры***

Для генерации промо-кодов выполните команду, в которой после флага -a укажите количество промо-кодов, после флага -g - наименование группы:
```bash
python generating_promo_codes\generator_promo_codes.py -a 10 -g агенства
```
Для проверке существования промо-кода в созданном json файле выполните команду, в которой после флага -pc укажите промо-код:
```bash
python generating_promo_codes\existence_promo_code.py -pc af51e4bc-4d25-4ef0-92ba-37861bc22371
```

Для проверки генерации промо-кодов выполните команду:
```bash
python generating_promo_codes\test_generator_promo_codes.py
```

Для проверки на существование промо-кода в json файле выполните команду:
```bash
python generating_promo_codes\test_existence_promo_code.py
```
