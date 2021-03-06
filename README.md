# py-fts-tatar
Full Text Search проект по документам/ресурсам на татарском языке


# Мега-цель
* создать поисковик документов/ресурсов на татарском языке, который ищет внезависимости от используемого алфавита (кириллица или латиница)

# Миссия проекта
* сделать доступным ресурсы на татарском языке по всему миру среди татар, башкир и других кто интересуется татарским миром


# Полезные ссылки
* [Татарския язык, литература, музыка](http://www.kaefik.ru/2018/06/04/tatar/)
* [Проект: поисковая система по татарскому интернету](http://www.kaefik.ru/2018/06/14/search-for-tatar/)


# Планы
* сделать поиск слова в документах (дампа из википедии)
* сделать сложный поиск с использованием логических операторов

# Данные
* [Дамп википедии на татарском языке](https://dumps.wikimedia.org/ttwiki/)

# TODO
* научиться определять на каком языке страница на татарском на латинице или кириллица


## Структура проекта
1. split_wiki_dump.py  - разделение дампа вики на отдельные статьи.
2. analyzator.py - анализатор текста и создание инвертированного индекса 

[источник вдохновения](https://habr.com/ru/post/519024/)

Ядром FTS является структура данных, которая называется *инвертированный индекс*.
Он связывает каждое слово с документами, содержащими это слово.

Анализатор текста:

            <raw text> -> <tokenizer> -> <filters> -> <tokens>

1. **tokenizer**  - преобразование текста в список токенов (разбивает текст на гарницах слов и удаление знаков препинания.

2. **filters**    - возможно потребуется дополнительная нормализация данных:
    а. удаление общеупотребительных слов (таких например как a, I, the, таким образом заводим список стоп-слов)
    б. стемминг - из-за грамматических правил в документах встречаются разные формы слов. стемминг сводит их к основной форме

Построение инвертированного индекса - думаю что подойдет словарь, где ключом будет токен (строка),
а значением - список идентификаторов документов