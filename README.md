# taski-docker
### О проекте.
Небольшой веб сервис, где можно ставить записывать задачи, помечать их выполненными. Сервис доступен любому.
___
### Информация об авторах.
- Акчурин Лев Ливатович.<br>Студент курса Яндекс Практикума Python-разработчик плюс.<br>
___
### При создании проекта использовалось:
- язык программирования Python версии 3.9.13;
- фреймворк Django версии 3.2.16;
- фреймворк Django Rest Framework версии 3.12.4;
- библиотека django-cors-headers версии 3.13.0;
- базы данных выполнены на PostgreSQL;
- библиотека psycopg2-binary версии 2.9.3;
- API реализуется с использованием JSON;
- frontend выполнен с использованием языка программирования JavaScript.
___
### Как развернуть проект.
<br>**Проект рассчитан на операционную систему Linux.**<br>
Чтобы развернуть проект необходимо следующие:
- Форкнуть проект себе на репозиторий с:
```
https://github.com/levisserena/taski-docker
```

>*активная ссылка под этой кнопкой* -> [КНОПКА](https://github.com/levisserena/taski-docker)
- Клонировать репозиторий со своего GitHub и перейти в него в командной строке:

```
git clone https://github.com/<имя вашего акаунта>/taski-docker.git
```
<br>**Разворачивание проекта происходит с помощью [Docker](https://www.docker.com/).**<br>
<br>В терминале прейдите в директорию `taski-docker`, создайте файл `.env`. В этом файле будут прописаны ваши переменные окружения - подробнее смотрите в файле `.env.example`.<br>В системе с настроенным Docker введите в терминале (находясь в директории `taski-docker`) команду:
```
docker compose up
```
Будут собраны контейнеры и запущен проект.
<br>Также можно использовать команду:<br>
```
docker compose -f docker-compose.production.yml up 
```
Образы будут скачены с [docker
hub](https://hub.docker.com/), что гораздо удобнее, при разворачивание на удаленном сервере. Скачать файл `docker-compose.production.yml` можно, например, командой:
```
scp -i path_to_SSH/SSH_name docker-compose.production.yml \
    username@server_ip:/home/username/taski/docker-compose.production.yml 
```
Где:
  - path_to_SSH — путь к файлу с SSH-ключом;
  - SSH_name — имя файла с SSH-ключом (без расширения);
  - username — ваше имя пользователя на сервере;
  - server_ip — IP вашего сервера.

<br>Для запуска Docker Compose в режиме демона используем команду:<br>
```
sudo docker compose -f docker-compose.production.yml up -d
```
<br>*Каким из методом развертывания контейнеров пользоваться - решать вам.*<br>

После развертывания необходимо выполнить миграции:
```
docker compose exec backend python manage.py migrate
```
Собрать статику Django:
```
docker compose exec backend python manage.py collectstatic
```
```
docker compose exec backend cp -r /app/collected_static/. /backend_static/static/
```
После настройки внешнего прокси-сервера проект готов к работе. Внутрений прокси-сервер "слушает" порт 8000.

<br>*В папке `.github/workdlows` лежит файл `main.yml` - для работы GitHub Actions. Вы для своих целей можете настроить подобный, но разбираться придется самим.*<br>
### Эндпоинты.
Далее 127.0.0.1:8000 - при развертывание локально, в остальных случаях, необходим реальный IP или доменное имя.
- Главная страница.
```
http://127.0.0.1:8000/
```
- Для API запросов.
```
http://127.0.0.1:8000/api/tasks
```
- Доступ в админ зону.
```
http://127.0.0.1:8000/admin
```