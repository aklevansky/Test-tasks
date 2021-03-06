Необходимо реализовать 2 API, со следующими методами:

# Партнерское API 

- получение списка анкет (с сортировкой и фильтрами)
- просмотр анкеты по ID
- создание анкеты
- отправка заявки в кредитные организации

# API кредитной организации:

- получение списка заявок (с сортировкой и фильтрами)
- просмотр заявки по ID

# Виды пользователей

В системе должно быть 3 вида пользователей (можно реализовать на django.contrib.auth.models, можно придумать свою):

- суперпользователи
    - имеют доступ ко всем видам API;
    - имеют доступы ко всем заявкам и анкетам
    - могут удалять и редактировать анкеты и заявки (операции
каскадируются)
- партнеры
    - имеют доступ только к 1-му API,
    - не могут удалять и редактировать анкеты и заявки
- кредитные организации
    - не могут удалять и редактировать ничего
    - при просмотре заявки по ID статус заявки меняется на RECIEVED

# Информационная модель

## Предложение

- дата и время создания
- дата и время изменения
- дата и время начала ротации
- дата и время окончания ротации
- название предложения
- тип предложения (потреб, ипотека, автокредит, КМСБ)
- минимальный скоринговый балл
- максимальный скоринговый балл
- кредитная организация - foreign key

## Анкета клиента

- дата и время создания
- дата и время изменения
- ФИО
- дата рождения
- номер телефона
- номер паспорта
- скоринговый балл

## Заявка в кредитную организацию

- дата и время создания
- дата и время отправки
- анкета клиента foreign key
- предложение foreign key
- статус (NEW, SENT)

Все модели должны быть доступны для редактирования в админке:
- Фильтры по дате от до или иерархический фильтр
- Текстовый поиск

Всё что не указано в тестовом задании - на усмотрение кандидата. При выполнении тестового задания будет учитываться:
- качество кода, его организация и читаемость
- применение готовых решений, стремление избежать "костылей" и "велосипедов"
- удобство API и админки
- наличие документации, пояснений и комментариев приветствуется

Технологии:
python django, rest framework

Вы можете использовать свои технологии, тогда решение нужно будет обосновать. Желаем успеха в решении тестового задания.
