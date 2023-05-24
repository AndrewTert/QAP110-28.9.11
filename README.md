# QAP110-28.9.11

# Использование библиотеки Pydantic в автотестах

Было выбрано API сайта: https://ipapi.co

Описание директорий проекта:

    /tests      - располагается файл с тестами
    /api        - функции работы с API сайта
    /serilizers - класс для валидации ответа сайта


Для работы приложения нужно установить библиотеки: requests, pytest, pydantic:

    pip install requests 
    pip install pytest 
    pip install pydantic 
или

    pip install -r requirements.txt

# ВНИМАНИЕ: 
последний тест закомментирован т. к. его выполнение превысит бесплатную дневную норму запросов к сайту
