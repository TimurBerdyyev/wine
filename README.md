# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск

- Скачайте код
- Установите зависимости 
```
pip install requirements.txt
```
- Запустите сайт командой ```python3 main.py```
- Перейдите на сайт по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Формат данныхм
Программа ожидает данные в формате Exel.
Пример данных:
```
|категория    |Название           |Сорт            |Цена|Картинка                |Акция               |
|_____________|___________________|________________|____|________________________|____________________|
|Белые вина   |Белая леди         |Дамский пальчик |399 |belaya_ledi.png         |Выгодное предложение|
|Напитки      |Коньяк классический|                |350 |konyak_klassicheskyi.png|                    |
|Белые вина   |Ркацители          |Ркацители       |499 |rkaciteli.png           |                    |
|Красные вина |Черный лекарь      |Качич           |399 |chernyi_lekar.png       |                    |
|Красные вина |Хванчкара          |Александраули   |550 |hvanchkara.png          |                    |
|Белые вина   |Кокур              |Кокур           |450 |                        |                    |
|Красные вина |Киндзмараули       |Саперави        |550 |kindzmarauli.png        |                    |
|Напитки      |Чача               |                |299 |chacha.png              |Выгодное предложение|
|Напитки      |Коньяк кизиловый   |                |350 |konyak_kizilovyi.png    |                    |
|+++++++++++++|+++++++++++++++++++|++++++++++++++++|++++|++++++++++++++++++++++++|++++++++++++++++++++|
``` 
## Инструкция 
1. Скопируйте таблицу и заполните своими Данными 
2. сохраните таблицу в формате Exel под имнем ``` wine.xlsx ```
3. поместите полученный файл в папку `xlsx_file` , папка нодится в корне проекта 


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
